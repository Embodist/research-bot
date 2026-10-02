"""Web page reader: fetch a URL and turn it into clean text for the LLM."""

from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass

from .util import extract_title, html_to_text, http_get

log = logging.getLogger(__name__)

_SKIP_SUFFIXES = (".pdf", ".zip", ".gz", ".tar", ".png", ".jpg", ".jpeg", ".gif", ".mp4", ".webp", ".svg")


@dataclass
class Page:
    url: str
    title: str = ""
    text: str = ""
    status: int = 0
    error: str = ""

    def to_dict(self) -> dict:
        return {"url": self.url, "title": self.title, "text": self.text, "status": self.status, "error": self.error}


def fetch_page(url: str, *, timeout: float = 20, max_chars: int = 6000, user_agent: str = "") -> Page:
    if not url or url.lower().endswith(_SKIP_SUFFIXES):
        return Page(url=url, error="skipped (unsupported content type)")
    try:
        resp = http_get(url, timeout=timeout, retries=1, user_agent=user_agent or "")
        ctype = resp.headers.get("content-type", "")
        if "html" not in ctype and "xml" not in ctype and "json" not in ctype and ctype:
            return Page(url=url, status=resp.status_code, error=f"unsupported content-type: {ctype}")
        raw = resp.text
        title = extract_title(raw)
        text = html_to_text(raw, max_chars=max_chars)
        return Page(url=url, title=title, text=text, status=resp.status_code)
    except Exception as exc:  # noqa: BLE001
        return Page(url=url, error=str(exc))


def fetch_many(urls: list[str], *, timeout: float = 20, max_chars: int = 6000, user_agent: str = "", workers: int = 4) -> dict[str, Page]:
    out: dict[str, Page] = {}
    uniq = list(dict.fromkeys(u for u in urls if u))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(fetch_page, u, timeout=timeout, max_chars=max_chars, user_agent=user_agent): u for u in uniq}
        for fut in as_completed(futures):
            page = fut.result()
            out[page.url] = page
    return out
