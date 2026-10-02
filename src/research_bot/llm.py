"""Minimal OpenAI-compatible chat client (works with the whnetsea gateway)."""

from __future__ import annotations

import json
import logging
import time
from typing import Any

import httpx

from .util import extract_json, now_utc, truncate

log = logging.getLogger(__name__)


class LLMError(RuntimeError):
    pass


class LLM:
    def __init__(self, cfg: Any) -> None:
        self.base_url = str(cfg.base_url).rstrip("/")
        self.api_key = cfg.api_key or ""
        self.model = cfg.model
        self.tiers = dict(getattr(cfg, "tiers", {}) or {})
        self.fallback_models = [m for m in (getattr(cfg, "fallback_models", None) or []) if m]
        self.temperature = float(cfg.temperature)
        self.max_tokens = int(cfg.max_tokens)
        self.timeout = float(cfg.timeout)
        self.max_retries = int(cfg.max_retries)
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.calls = 0

    # -- model helpers ------------------------------------------------------
    def resolve_model(self, tier: str | None) -> str:
        if not tier:
            return self.model
        return self.tiers.get(tier, self.model)

    # -- core call ----------------------------------------------------------
    def chat(
        self,
        messages: list[dict[str, str]],
        *,
        tier: str | None = None,
        model: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
        json_mode: bool = False,
    ) -> str:
        if not self.api_key:
            raise LLMError("LLM api_key is empty (set llm.api_key or $LLM_API_KEY)")
        base_model = model or self.resolve_model(tier)
        candidates = [base_model] + [m for m in self.fallback_models if m and m != base_model]
        last_err: Exception | None = None
        for candidate in candidates:
            try:
                return self._chat_once(
                    candidate, messages, temperature=temperature, max_tokens=max_tokens, json_mode=json_mode
                )
            except LLMError as exc:
                last_err = exc
                text = str(exc).lower()
                unavailable = (
                    "model_not_found" in text
                    or "no available channel" in text
                    or "does not exist" in text
                    or "unknown model" in text
                )
                if unavailable and candidate != candidates[-1]:
                    log.warning("LLM model %r unavailable (%s); trying fallback model", candidate, exc)
                    continue
                raise
        assert last_err is not None
        raise last_err

    def _chat_once(
        self,
        model: str,
        messages: list[dict[str, str]],
        *,
        temperature: float | None,
        max_tokens: int | None,
        json_mode: bool,
    ) -> str:
        payload: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": self.temperature if temperature is None else temperature,
            "max_tokens": self.max_tokens if max_tokens is None else max_tokens,
        }
        if json_mode:
            payload["response_format"] = {"type": "json_object"}

        url = f"{self.base_url}/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        last: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                resp = httpx.post(url, headers=headers, json=payload, timeout=self.timeout)
                if resp.status_code >= 400:
                    # Retry on 429/5xx; fail fast on auth/validation errors.
                    raise LLMError(f"HTTP {resp.status_code}: {truncate(resp.text, 300)}")
                data = resp.json()
                self.calls += 1
                usage = data.get("usage") or {}
                self.total_prompt_tokens += int(usage.get("prompt_tokens") or 0)
                self.total_completion_tokens += int(usage.get("completion_tokens") or 0)
                choice = (data.get("choices") or [{}])[0]
                message = choice.get("message") or {}
                content = message.get("content") or ""
                if not content and message.get("reasoning_content"):
                    # Some gateways put everything in reasoning_content when max_tokens is tight.
                    content = message["reasoning_content"]
                finish = choice.get("finish_reason")
                if not content.strip() and finish == "length":
                    raise LLMError("model hit max_tokens before producing content; increase llm.max_tokens")
                return content
            except Exception as exc:  # noqa: BLE001
                last = exc
                # Don't waste retries on a definitively missing model.
                if "model_not_found" in str(exc).lower() or "no available channel" in str(exc).lower():
                    raise LLMError(str(exc)) from exc
                if attempt < self.max_retries:
                    time.sleep(min(2**attempt, 8))
                    continue
        raise LLMError(f"chat failed after {self.max_retries + 1} attempts: {last}")

    # -- JSON helper --------------------------------------------------------
    def json(
        self,
        messages: list[dict[str, str]],
        *,
        tier: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
        retries: int = 2,
    ) -> Any:
        attempt = 0
        last_err: Exception | None = None
        convo = list(messages)
        while attempt <= retries:
            raw = self.chat(convo, tier=tier, temperature=temperature, max_tokens=max_tokens, json_mode=True)
            try:
                return extract_json(raw)
            except ValueError as exc:
                last_err = exc
                convo = list(messages) + [
                    {"role": "assistant", "content": truncate(raw, 2000)},
                    {
                        "role": "user",
                        "content": "Your previous reply was not valid JSON. Reply with ONLY a single valid JSON "
                        "object and nothing else.",
                    },
                ]
                attempt += 1
        raise LLMError(f"could not obtain valid JSON: {last_err}")

    def stats(self) -> dict[str, Any]:
        return {
            "calls": self.calls,
            "prompt_tokens": self.total_prompt_tokens,
            "completion_tokens": self.total_completion_tokens,
            "generated_at": now_utc().isoformat(),
        }


def llm_from_config(cfg: Any) -> LLM:
    return LLM(cfg)


def dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)
