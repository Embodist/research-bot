"""Small shared helpers: HTTP, HTML→text, JSON extraction, slugs, dates."""

from __future__ import annotations

import hashlib
import html as html_mod
import json
import re
import time
import unicodedata
import urllib.parse
from datetime import datetime, timedelta, timezone
from typing import Any

import httpx

DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime | None = None) -> str:
    return (dt or now_utc()).astimezone(timezone.utc).replace(microsecond=0).isoformat()


def date_stamp(dt: datetime | None = None) -> str:
    return (dt or now_utc()).strftime("%Y-%m-%d")


def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text or "")
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return (text[:max_len].strip("-")) or "report"


def stable_id(*parts: str) -> str:
    return hashlib.sha1("||".join(parts).encode("utf-8", "ignore")).hexdigest()[:12]


def truncate(text: str, limit: int, ellipsis: str = "…") -> str:
    text = text or ""
    if limit <= 0 or len(text) <= limit:
        return text
    return text[: max(0, limit - len(ellipsis))].rstrip() + ellipsis


def http_get(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    params: dict[str, Any] | None = None,
    timeout: float = 20,
    retries: int = 2,
    backoff: float = 1.0,
    user_agent: str = DEFAULT_UA,
    follow_redirects: bool = True,
) -> httpx.Response:
    """GET with retries. Raises the last exception if all attempts fail."""
    merged = {"User-Agent": user_agent, "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8"}
    if headers:
        merged.update(headers)
    last: Exception | None = None
    for attempt in range(retries + 1):
        try:
            resp = httpx.get(
                url,
                headers=merged,
                params=params,
                timeout=timeout,
                follow_redirects=follow_redirects,
            )
            if (resp.status_code >= 500 or resp.status_code == 429) and attempt < retries:
                raise httpx.HTTPStatusError("retryable error", request=resp.request, response=resp)
            return resp
        except Exception as exc:  # noqa: BLE001 - retried below
            last = exc
            if attempt < retries:
                time.sleep(backoff * (2**attempt))
    assert last is not None
    raise last


_SCRIPT_RE = re.compile(r"<(script|style|noscript|svg|template)[^>]*>.*?</\1>", re.I | re.S)
_TAG_RE = re.compile(r"<[^>]+>")
_BLOCK_RE = re.compile(r"</(p|div|li|h[1-6]|tr|section|article|br)>", re.I)
_WS_RE = re.compile(r"[ \t\f\v]+")
_NL_RE = re.compile(r"\n{3,}")
_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)


def html_to_text(raw: str, *, max_chars: int = 6000) -> str:
    """Very small, dependency-free HTML → readable text."""
    if not raw:
        return ""
    text = _SCRIPT_RE.sub(" ", raw)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = _BLOCK_RE.sub("\n", text)
    text = _TAG_RE.sub(" ", text)
    text = html_mod.unescape(text)
    text = _WS_RE.sub(" ", text)
    text = "\n".join(line.strip() for line in text.splitlines())
    text = _NL_RE.sub("\n\n", text).strip()
    return truncate(text, max_chars)


def extract_title(raw: str) -> str:
    m = _TITLE_RE.search(raw or "")
    if not m:
        return ""
    return html_mod.unescape(_TAG_RE.sub("", m.group(1))).strip()


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)```", re.I | re.S)


def extract_json(text: str) -> Any:
    """Pull the first JSON object/array out of an LLM response.

    Tolerates code fences, prose around the payload and trailing commas.
    """
    if text is None:
        raise ValueError("empty LLM response")
    candidate = text.strip()
    fence = _JSON_FENCE_RE.search(candidate)
    if fence:
        candidate = fence.group(1).strip()
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass
    # Find a balanced {...} or [...] span.
    for opener, closer in (("{", "}"), ("[", "]")):
        start = candidate.find(opener)
        if start == -1:
            continue
        depth = 0
        in_str = False
        esc = False
        for idx in range(start, len(candidate)):
            ch = candidate[idx]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == opener:
                depth += 1
            elif ch == closer:
                depth -= 1
                if depth == 0:
                    chunk = candidate[start : idx + 1]
                    chunk = re.sub(r",\s*([}\]])", r"\1", chunk)
                    try:
                        return json.loads(chunk)
                    except json.JSONDecodeError:
                        break
    raise ValueError(f"no JSON found in LLM response: {truncate(text, 200)!r}")


def norm_url(url: str) -> str:
    """Normalise a URL for de-duplication."""
    if not url:
        return ""
    url = url.strip()
    if url.startswith("//"):
        url = "https:" + url
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return url
    query = urllib.parse.parse_qsl(parts.query, keep_blank_values=False)
    drop = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "ref", "fbclid", "gclid"}
    query = [(k, v) for k, v in query if k.lower() not in drop]
    netloc = parts.netloc.lower().replace("www.", "")
    path = parts.path.rstrip("/") or "/"
    return urllib.parse.urlunsplit((parts.scheme or "https", netloc, path, urllib.parse.urlencode(query), ""))


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    value = str(value).strip()
    fmts = ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%Y/%m/%d", "%Y-%m", "%Y")
    for fmt in fmts:
        try:
            dt = datetime.strptime(value[: len(fmt) + 2] if fmt.endswith("Z") else value, fmt)
            return dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def is_recent(value: str | None, days: int) -> bool:
    dt = parse_date(value)
    if dt is None:
        return True  # unknown → don't penalise
    return dt >= now_utc() - timedelta(days=days)
