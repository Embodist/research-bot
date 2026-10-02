"""Concrete search backends.

Design notes
------------
* Structured academic APIs (arXiv, OpenAlex, Crossref, Semantic Scholar) and the
  GitHub API are the primary *evidence* sources: they return metadata we can cite
  (year, venue, authors, citation counts, stars).
* HTML metasearch engines (Bing/Sogou/360/SearXNG) widen recall for news, blogs,
  docs and non-indexed pages. Their parsers are intentionally forgiving.
* Every engine is best-effort and never raises out of ``search`` — the router
  isolates failures so one blocked provider cannot kill a research run.
"""

from __future__ import annotations

import html as html_mod
import logging
import re
import threading
import time
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Any

from ..util import http_get, truncate
from .base import Engine, SearchResult

log = logging.getLogger(__name__)

_ATOM = "{http://www.w3.org/2005/Atom}"
_ARXIV = "{http://arxiv.org/schemas/atom}"
_TAG_RE = re.compile(r"<[^>]+>")


def _clean(text: str | None) -> str:
    if not text:
        return ""
    return html_mod.unescape(_TAG_RE.sub(" ", text)).strip()


def _abs_url(base: str, href: str) -> str:
    if not href:
        return ""
    if href.startswith("//"):
        return "https:" + href
    return urllib.parse.urljoin(base, href)


# ---------------------------------------------------------------------------
# Academic / structured APIs
# ---------------------------------------------------------------------------
class ArxivEngine(Engine):
    name = "arxiv"
    kind = "paper"

    # arXiv asks clients to make at most one request every ~3 seconds; the router
    # fans out in parallel, so serialise here (process-wide).
    _lock = threading.Lock()
    _last = 0.0
    _min_interval = 3.5

    def _fetch(self, search_query: str, limit: int, sort: str) -> list[SearchResult]:
        with ArxivEngine._lock:
            wait = ArxivEngine._min_interval - (time.time() - ArxivEngine._last)
            if wait > 0:
                time.sleep(wait)
            try:
                resp = http_get(
                    "https://export.arxiv.org/api/query",
                    params={
                        "search_query": search_query,
                        "start": 0,
                        "max_results": limit,
                        "sortBy": sort,
                        "sortOrder": "descending",
                    },
                    timeout=max(float(self.cfg.timeout), 30.0),
                    user_agent=self.cfg.user_agent,
                    retries=1,
                    backoff=4.0,
                )
                if resp.status_code == 429:
                    log.info("arxiv rate-limited; skipping %r", search_query)
                    return []
                resp.raise_for_status()
            except Exception as exc:  # noqa: BLE001 - never kill the run
                log.info("arxiv unavailable (%s); skipping %r", exc, search_query)
                return []
            finally:
                ArxivEngine._last = time.time()
        return self._parse(resp.text)

    def _parse(self, xml_text: str) -> list[SearchResult]:
        root = ET.fromstring(xml_text)
        out: list[SearchResult] = []
        for entry in root.findall(f"{_ATOM}entry"):
            title = _clean(entry.findtext(f"{_ATOM}title"))
            link = entry.findtext(f"{_ATOM}id") or ""
            summary = _clean(entry.findtext(f"{_ATOM}summary"))
            published = (entry.findtext(f"{_ATOM}published") or "")[:10]
            authors = [a.findtext(f"{_ATOM}name") or "" for a in entry.findall(f"{_ATOM}author")]
            primary = entry.find(f"{_ARXIV}primary_category")
            venue = primary.get("term") if primary is not None else None
            out.append(
                SearchResult(
                    title=title,
                    url=link,
                    snippet=truncate(summary, 600),
                    engine=self.name,
                    kind="paper",
                    published=published or None,
                    authors=[a for a in authors if a],
                    venue=venue,
                    extra={"arxiv_id": link.rsplit("/", 1)[-1] if link else ""},
                )
            )
        return out

    def search(self, query: str, limit: int) -> list[SearchResult]:
        # arXiv treats space-separated terms as OR, which destroys precision.
        # Short queries get an exact-phrase attempt first; longer planner queries
        # go straight to an OR query ranked by relevance (one request, not two).
        q = query.strip()
        if re.search(r"\b(all|ti|abs|au|cat):", q):
            return self._fetch(q, limit, "relevance")
        if len(q.split()) <= 4:
            phrase = self._fetch(f'all:"{q}"', limit, "relevance")
            if phrase:
                return phrase
        return self._fetch(f"all:{q}", limit, "relevance")


class OpenAlexEngine(Engine):
    name = "openalex"
    kind = "paper"

    def search(self, query: str, limit: int) -> list[SearchResult]:
        resp = http_get(
            "https://api.openalex.org/works",
            params={
                "filter": f"title_and_abstract.search:{query}",
                "per-page": limit,
                "mailto": "research-bot@users.noreply.github.com",
            },
            timeout=float(self.cfg.timeout),
            user_agent=self.cfg.user_agent,
        )
        resp.raise_for_status()
        out: list[SearchResult] = []
        for work in (resp.json().get("results") or []):
            title = work.get("display_name") or work.get("title") or ""
            url = work.get("doi") or work.get("id") or ""
            abstract = work.get("abstract") or ""
            if not abstract:
                abstract = _reconstruct_abstract(work.get("abstract_inverted_index"))
            authors = [
                (a.get("author") or {}).get("display_name", "")
                for a in (work.get("authorships") or [])
            ]
            venue = None
            primary = work.get("primary_location") or {}
            if isinstance(primary.get("source"), dict):
                venue = primary["source"].get("display_name")
            out.append(
                SearchResult(
                    title=title,
                    url=url,
                    snippet=truncate(abstract, 600),
                    engine=self.name,
                    kind="paper",
                    published=(work.get("publication_date") or "")[:10] or None,
                    authors=[a for a in authors if a][:12],
                    venue=venue,
                    citations=work.get("cited_by_count"),
                    extra={"openalex_id": work.get("id", "")},
                )
            )
        return out


def _reconstruct_abstract(inverted: dict[str, list[int]] | None) -> str:
    if not inverted:
        return ""
    positions: list[tuple[int, str]] = []
    for word, idxs in inverted.items():
        for idx in idxs:
            positions.append((idx, word))
    positions.sort()
    return " ".join(word for _, word in positions)


class CrossrefEngine(Engine):
    name = "crossref"
    kind = "paper"

    def search(self, query: str, limit: int) -> list[SearchResult]:
        resp = http_get(
            "https://api.crossref.org/works",
            params={
                "query.bibliographic": query,
                "rows": limit,
                "sort": "relevance",
                "order": "desc",
                "select": "DOI,title,container-title,published,author,is-referenced-by-count,abstract,URL,type",
            },
            timeout=float(self.cfg.timeout),
            user_agent=self.cfg.user_agent,
        )
        resp.raise_for_status()
        out: list[SearchResult] = []
        for item in ((resp.json().get("message") or {}).get("items") or []):
            titles = item.get("title") or []
            title = titles[0] if titles else ""
            doi = item.get("DOI") or ""
            url = f"https://doi.org/{doi}" if doi else (item.get("URL") or "")
            published = _crossref_date(item.get("published"))
            authors = [
                " ".join(filter(None, [a.get("given"), a.get("family")]))
                for a in (item.get("author") or [])
            ]
            containers = item.get("container-title") or []
            out.append(
                SearchResult(
                    title=title,
                    url=url,
                    snippet=truncate(_clean(item.get("abstract")), 600),
                    engine=self.name,
                    kind="paper",
                    published=published,
                    authors=[a for a in authors if a][:12],
                    venue=containers[0] if containers else None,
                    citations=item.get("is-referenced-by-count"),
                    extra={"doi": doi, "type": item.get("type", "")},
                )
            )
        return out


def _crossref_date(node: Any) -> str | None:
    if not isinstance(node, dict):
        return None
    parts = (node.get("date-parts") or [[None]])[0]
    if not parts or parts[0] is None:
        return None
    year = parts[0]
    month = parts[1] if len(parts) > 1 else 1
    day = parts[2] if len(parts) > 2 else 1
    try:
        return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
    except (TypeError, ValueError):
        return str(year)


class SemanticScholarEngine(Engine):
    name = "semantic_scholar"
    kind = "paper"

    def search(self, query: str, limit: int) -> list[SearchResult]:
        fields = "title,abstract,url,year,venue,authors,citationCount,externalIds,publicationDate"
        resp = http_get(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params={"query": query, "limit": limit, "fields": fields},
            timeout=float(self.cfg.timeout),
            user_agent=self.cfg.user_agent,
            retries=0,  # 429s are common; don't hammer
        )
        if resp.status_code == 429:
            log.info("semantic_scholar rate-limited; skipping")
            return []
        resp.raise_for_status()
        out: list[SearchResult] = []
        for paper in (resp.json().get("data") or []):
            url = paper.get("url") or ""
            ext = paper.get("externalIds") or {}
            if ext.get("ArXiv"):
                url = f"https://arxiv.org/abs/{ext['ArXiv']}"
            elif ext.get("DOI"):
                url = f"https://doi.org/{ext['DOI']}"
            out.append(
                SearchResult(
                    title=paper.get("title") or "",
                    url=url,
                    snippet=truncate(paper.get("abstract") or "", 600),
                    engine=self.name,
                    kind="paper",
                    published=paper.get("publicationDate") or (str(paper.get("year")) if paper.get("year") else None),
                    authors=[a.get("name", "") for a in (paper.get("authors") or [])][:12],
                    venue=paper.get("venue") or None,
                    citations=paper.get("citationCount"),
                )
            )
        return out


class GithubEngine(Engine):
    name = "github"
    kind = "project"

    def search(self, query: str, limit: int) -> list[SearchResult]:
        headers = {"Accept": "application/vnd.github+json"}
        token = getattr(self.cfg, "github_token", "") or ""
        if token:
            headers["Authorization"] = f"Bearer {token}"
        resp = http_get(
            "https://api.github.com/search/repositories",
            params={"q": query, "sort": "stars", "order": "desc", "per_page": limit},
            headers=headers,
            timeout=float(self.cfg.timeout),
            user_agent=self.cfg.user_agent,
        )
        if resp.status_code in (403, 429):
            log.info("github rate-limited; skipping")
            return []
        resp.raise_for_status()
        out: list[SearchResult] = []
        for repo in (resp.json().get("items") or []):
            out.append(
                SearchResult(
                    title=repo.get("full_name") or "",
                    url=repo.get("html_url") or "",
                    snippet=truncate(repo.get("description") or "", 400),
                    engine=self.name,
                    kind="project",
                    published=(repo.get("pushed_at") or "")[:10] or None,
                    stars=repo.get("stargazers_count"),
                    extra={
                        "language": repo.get("language"),
                        "topics": (repo.get("topics") or [])[:8],
                        "forks": repo.get("forks_count"),
                    },
                )
            )
        return out


# ---------------------------------------------------------------------------
# HTML metasearch engines
# ---------------------------------------------------------------------------
class BingEngine(Engine):
    name = "bing"
    kind = "web"

    def search(self, query: str, limit: int) -> list[SearchResult]:
        resp = http_get(
            "https://cn.bing.com/search",
            params={"q": query, "count": max(limit, 10), "setlang": "en"},
            timeout=float(self.cfg.timeout),
            user_agent=self.cfg.user_agent,
        )
        resp.raise_for_status()
        return _parse_bing(resp.text, limit)


def _parse_bing(html: str, limit: int) -> list[SearchResult]:
    blocks = re.split(r'<li class="b_algo"', html)[1:]
    out: list[SearchResult] = []
    for block in blocks:
        m = re.search(r"<h2[^>]*>\s*<a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", block, re.S)
        if not m:
            continue
        url, title = m.group(1), _clean(m.group(2))
        if url.startswith("/") or "bing.com" in url:
            continue
        snippet = ""
        sm = re.search(r"<p[^>]*>(.*?)</p>", block, re.S)
        if not sm:
            sm = re.search(r'class="b_lineclamp[^"]*"[^>]*>(.*?)</', block, re.S)
        if sm:
            snippet = _clean(sm.group(1))
        out.append(SearchResult(title=title, url=url, snippet=truncate(snippet, 320), engine="bing"))
        if len(out) >= limit:
            break
    return out


class SogouEngine(Engine):
    name = "sogou"
    kind = "web"

    def search(self, query: str, limit: int) -> list[SearchResult]:
        resp = http_get(
            "https://www.sogou.com/web",
            params={"query": query},
            timeout=float(self.cfg.timeout),
            user_agent=self.cfg.user_agent,
        )
        resp.raise_for_status()
        html = resp.text
        out: list[SearchResult] = []
        for m in re.finditer(r"<h3[^>]*>\s*<a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", html, re.S):
            href, title = html_mod.unescape(m.group(1)), _clean(m.group(2))
            if not title:
                continue
            url = _abs_url("https://www.sogou.com", href)
            # Sogou wraps outbound links in /link?url=... redirects.
            if "/link?" in url:
                q = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
                if q.get("url"):
                    url = q["url"][0]
            out.append(SearchResult(title=title, url=url, snippet="", engine="sogou"))
            if len(out) >= limit:
                break
        return out


class So360Engine(Engine):
    name = "so360"
    kind = "web"

    def search(self, query: str, limit: int) -> list[SearchResult]:
        resp = http_get(
            "https://www.so.com/s",
            params={"q": query},
            timeout=float(self.cfg.timeout),
            user_agent=self.cfg.user_agent,
        )
        resp.raise_for_status()
        html = resp.text
        out: list[SearchResult] = []
        pattern = re.compile(r'<h3[^>]*class="res-title[^"]*"[^>]*>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>(.*?)</h3>', re.S)
        for m in pattern.finditer(html):
            href, title = m.group(1), _clean(m.group(2))
            url = _abs_url("https://www.so.com", href)
            out.append(SearchResult(title=title, url=url, snippet="", engine="so360"))
            if len(out) >= limit:
                break
        if not out:  # older/alternate markup
            for m in re.finditer(r'<a[^>]*href="(https?://[^"]+)"[^>]*class="[^"]*res-title[^"]*"[^>]*>(.*?)</a>', html, re.S):
                out.append(SearchResult(title=_clean(m.group(2)), url=m.group(1), engine="so360"))
                if len(out) >= limit:
                    break
        # 360 wraps outbound links in so.com/link?m=... redirect pages that only
        # reveal the target through `window.location.replace(...)`.
        out = self._resolve_links(out)
        return out

    def _resolve_links(self, results: list[SearchResult]) -> list[SearchResult]:
        from concurrent.futures import ThreadPoolExecutor

        targets = [r for r in results if "so.com/link" in r.url]
        if not targets:
            return results
        with ThreadPoolExecutor(max_workers=min(6, len(targets))) as pool:
            final = list(pool.map(self._resolve_one, targets))
        for res, url in zip(targets, final, strict=False):
            res.url = url
        return results

    def _resolve_one(self, res: SearchResult) -> str:
        try:
            resp = http_get(res.url, timeout=8, retries=0, user_agent=self.cfg.user_agent)
            m = re.search(r"window\.location\.replace\((['\"])(.*?)\1\)", resp.text)
            if not m:
                m = re.search(r"URL=['\"]([^'\"]+)['\"]", resp.text, re.I)
            if m:
                return html_mod.unescape(m.group(m.lastindex or 2))
        except Exception:  # noqa: BLE001
            pass
        return res.url


class SearxngEngine(Engine):
    name = "searxng"
    kind = "web"

    def __init__(self, cfg: Any) -> None:
        super().__init__(cfg)
        self.base = str(getattr(cfg, "searxng_url", "") or "").rstrip("/")

    def available(self) -> bool:
        if not self.base:
            return False
        try:
            resp = http_get(self.base + "/", timeout=2.0, retries=0)
            return resp.status_code < 500
        except Exception:  # noqa: BLE001
            log.info("searxng not reachable at %s (skipped)", self.base)
            return False

    def search(self, query: str, limit: int) -> list[SearchResult]:
        # Prefer the JSON API; many SearXNG deployments disable it, in which case
        # we parse the (always available) HTML result page instead.
        try:
            resp = http_get(
                f"{self.base}/search",
                params={"q": query, "format": "json", "safesearch": 0},
                headers={"Accept": "application/json"},
                timeout=float(self.cfg.timeout),
                user_agent=self.cfg.user_agent,
            )
            if resp.status_code == 200 and "json" in resp.headers.get("content-type", ""):
                return self._parse_json(resp.json(), limit)
        except Exception as exc:  # noqa: BLE001 - fall through to HTML
            log.debug("searxng json failed (%s); trying html", exc)
        return self._search_html(query, limit)

    def _parse_json(self, data: dict[str, Any], limit: int) -> list[SearchResult]:
        out: list[SearchResult] = []
        for item in (data.get("results") or [])[:limit]:
            out.append(
                SearchResult(
                    title=item.get("title") or "",
                    url=item.get("url") or "",
                    snippet=truncate(item.get("content") or "", 320),
                    engine="searxng",
                    published=(item.get("publishedDate") or "")[:10] or None,
                )
            )
        return out

    def _search_html(self, query: str, limit: int) -> list[SearchResult]:
        resp = http_get(
            f"{self.base}/search",
            params={"q": query, "safesearch": 0},
            timeout=float(self.cfg.timeout),
            user_agent=self.cfg.user_agent,
        )
        resp.raise_for_status()
        html = resp.text
        out: list[SearchResult] = []
        for block in re.split(r'<article[^>]*class="result', html)[1:]:
            m = re.search(r'<h3>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
            if not m:
                continue
            url = html_mod.unescape(m.group(1))
            title = _clean(m.group(2))
            if not title or not url.startswith("http"):
                continue
            snippet = ""
            sm = re.search(r'<p class="content">(.*?)</p>', block, re.S)
            if sm:
                snippet = _clean(sm.group(1))
            out.append(SearchResult(title=title, url=url, snippet=truncate(snippet, 320), engine="searxng"))
            if len(out) >= limit:
                break
        return out
