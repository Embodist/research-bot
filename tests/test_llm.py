from __future__ import annotations

import json

import pytest

from research_bot.config import DotDict
from research_bot.llm import LLM, LLMError


class FakeResp:
    def __init__(self, status: int, payload: dict):
        self.status_code = status
        self._payload = payload
        self.text = json.dumps(payload)
        self.headers = {"content-type": "application/json"}

    def json(self):
        return self._payload


def _cfg(**over):
    base = {
        "base_url": "https://example.test/v1",
        "api_key": "k",
        "model": "primary",
        "fallback_models": ["backup"],
        "tiers": {},
        "temperature": 0.3,
        "max_tokens": 128,
        "timeout": 5,
        "max_retries": 0,
    }
    base.update(over)
    return DotDict(base)


def test_chat_success(monkeypatch):
    monkeypatch.setattr(
        "research_bot.llm.httpx.post",
        lambda *a, **k: FakeResp(200, {"choices": [{"message": {"content": "hello"}, "finish_reason": "stop"}], "usage": {}}),
    )
    llm = LLM(_cfg())
    assert llm.chat([{"role": "user", "content": "hi"}]) == "hello"
    assert llm.calls == 1


def test_model_fallback_on_not_found(monkeypatch):
    seen: list[str] = []

    def fake_post(url, headers, json, timeout):
        seen.append(json["model"])
        if json["model"] == "primary":
            return FakeResp(404, {"error": {"message": "No available channel for model primary", "type": "new_api_error"}})
        return FakeResp(200, {"choices": [{"message": {"content": "from backup"}, "finish_reason": "stop"}], "usage": {}})

    monkeypatch.setattr("research_bot.llm.httpx.post", fake_post)
    llm = LLM(_cfg())
    assert llm.chat([{"role": "user", "content": "hi"}]) == "from backup"
    assert seen == ["primary", "backup"]


def test_missing_api_key_raises():
    llm = LLM(_cfg(api_key=""))
    with pytest.raises(LLMError):
        llm.chat([{"role": "user", "content": "hi"}])


def test_finish_length_without_content_raises(monkeypatch):
    monkeypatch.setattr(
        "research_bot.llm.httpx.post",
        lambda *a, **k: FakeResp(200, {"choices": [{"message": {"content": ""}, "finish_reason": "length"}], "usage": {}}),
    )
    llm = LLM(_cfg(max_retries=0))
    with pytest.raises(LLMError):
        llm.chat([{"role": "user", "content": "hi"}])


def test_usage_is_accumulated(monkeypatch):
    monkeypatch.setattr(
        "research_bot.llm.httpx.post",
        lambda *a, **k: FakeResp(
            200,
            {
                "choices": [{"message": {"content": "x"}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 5},
            },
        ),
    )
    llm = LLM(_cfg())
    llm.chat([{"role": "user", "content": "hi"}])
    stats = llm.stats()
    assert stats["prompt_tokens"] == 10
    assert stats["completion_tokens"] == 5
