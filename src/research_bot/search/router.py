"""Search engine registry and multi-source fusion router.

The router fans out to every enabled engine in parallel, normalises the results,
de-duplicates by URL/title and fuses the rankings with Reciprocal Rank Fusion
(RRF). Structured/academic engines (arXiv, OpenAlex, Crossref, Semantic Scholar,
GitHub) are first-class because they return reliable metadata for evidence.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

from .base import Engine, SearchResult
from .engines import (
    ArxivEngine,
    BingEngine,
    CrossrefEngine,
    GithubEngine,
    OpenAlexEngine,
    SearxngEngine,
    SemanticScholarEngine,
    So360Engine,
    SogouEngine,
)

log = logging.getLogger(__name__)

ENGINE_REGISTRY: dict[str, Callable[[Any], Engine]] = {
    "arxiv": ArxivEngine,
    "openalex": OpenAlexEngine,
    "crossref": CrossrefEngine,
    "semantic_scholar": SemanticScholarEngine,
    "github": GithubEngine,
    "bing": BingEngine,
    "sogou": SogouEngine,
    "so360": So360Engine,
    "searxng": SearxngEngine,
}

# RRF trust weights. Structured/academic engines match the query server-side and
# return citable metadata, so they should outrank broad-recall HTML engines —
# which are noisy (homonym collisions like ROS → "reactive oxygen species") even
# when they match the same rank.
ENGINE_WEIGHTS: dict[str, float] = {
    "arxiv": 1.5,
    "openalex": 1.4,
    "semantic_scholar": 1.4,
    "crossref": 1.2,
    "github": 1.2,
    "searxng": 0.9,
    "bing": 0.6,
    "sogou": 0.6,
    "so360": 0.5,
}
DEFAULT_ENGINE_WEIGHT = 0.7


class SearchRouter:
    def __init__(self, cfg: Any) -> None:
        self.cfg = cfg
        # Circuit breaker: an engine that fails repeatedly (anti-spider 403s,
        # timeouts, blocks) is disabled for the remainder of the run so it stops
        # costing wall-clock time on every query.
        self.failure_threshold = 2
        self._failures: dict[str, int] = {}
        self._disabled: set[str] = set()
        enabled = list(getattr(cfg, "engines", []) or [])
        self.engines: list[Engine] = []
        for name in enabled:
            factory = ENGINE_REGISTRY.get(name)
            if factory is None:
                log.warning("unknown search engine %r (ignored)", name)
                continue
            try:
                engine = factory(cfg)
            except Exception as exc:  # noqa: BLE001
                log.warning("failed to init engine %s: %s", name, exc)
                continue
            if engine.available():
                self.engines.append(engine)
        if not self.engines:
            log.warning("no search engines enabled; using arxiv+openalex fallbacks")
            self.engines = [ArxivEngine(cfg), OpenAlexEngine(cfg)]

    @property
    def engine_names(self) -> list[str]:
        return [e.name for e in self.engines]

    @property
    def disabled_engines(self) -> list[str]:
        return sorted(self._disabled)

    def _run_one(self, engine: Engine, query: str, limit: int) -> list[SearchResult]:
        if engine.name in self._disabled:
            return []
        try:
            results = engine.search(query, limit)
            for r in results:
                r.engine = r.engine or engine.name
                if r.kind == "web" and engine.kind != "web":
                    r.kind = engine.kind
            return results
        except Exception as exc:  # noqa: BLE001 - one engine must not kill the run
            count = self._failures.get(engine.name, 0) + 1
            self._failures[engine.name] = count
            if count >= self.failure_threshold:
                self._disabled.add(engine.name)
                log.warning("engine %s disabled for this run after %d failures (%s)", engine.name, count, exc)
            else:
                log.warning("engine %s failed for query %r: %s", engine.name, query, exc)
            return []

    def search(self, query: str, *, per_engine: int | None = None, max_workers: int | None = None) -> list[SearchResult]:
        """Fan out one query to all engines and return RRF-fused unique results."""
        per_engine = per_engine or int(self.cfg.max_results_per_engine)
        results: list[tuple[str, SearchResult, int]] = []  # (source, result, rank)
        with ThreadPoolExecutor(max_workers=max_workers or min(8, len(self.engines) or 1)) as pool:
            futures = {pool.submit(self._run_one, e, query, per_engine): e for e in self.engines}
            for fut in as_completed(futures):
                engine = futures[fut]
                for rank, res in enumerate(fut.result()):
                    results.append((engine.name, res, rank))
        return rrf_fuse(results)

    def search_many(self, queries: list[str], *, per_engine: int | None = None) -> list[SearchResult]:
        """Run several queries (e.g. one per sub-question) and fuse everything."""
        all_pairs: list[tuple[str, SearchResult, int]] = []
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {pool.submit(self.search, q, per_engine=per_engine): q for q in queries}
            for fut in as_completed(futures):
                for rank, res in enumerate(fut.result()):
                    all_pairs.append((res.engine, res, rank))
        return rrf_fuse(all_pairs)


def _dedup_key(res: SearchResult) -> str:
    from ..util import norm_url

    url = norm_url(res.url)
    if url and url != "/":
        return url
    return (res.title or "").strip().lower()[:120]


def rrf_fuse(pairs: list[tuple[str, SearchResult, int]], k: int = 60, cap: int = 80) -> list[SearchResult]:
    """Reciprocal Rank Fusion with per-URL de-duplication, best fields kept."""
    scores: dict[str, float] = {}
    best: dict[str, SearchResult] = {}
    for _source, res, rank in pairs:
        if not res.title and not res.url:
            continue
        key = _dedup_key(res)
        weight = ENGINE_WEIGHTS.get(_source, DEFAULT_ENGINE_WEIGHT)
        scores[key] = scores.get(key, 0.0) + weight / (k + rank + 1)
        cur = best.get(key)
        if cur is None:
            best[key] = res
            continue
        # Merge: keep the most informative variant.
        if len(res.snippet or "") > len(cur.snippet or ""):
            cur.snippet = res.snippet
        if not cur.url and res.url:
            cur.url = res.url
        if not cur.published and res.published:
            cur.published = res.published
        if not cur.authors and res.authors:
            cur.authors = res.authors
        if not cur.venue and res.venue:
            cur.venue = res.venue
        if cur.citations is None and res.citations is not None:
            cur.citations = res.citations
        if cur.stars is None and res.stars is not None:
            cur.stars = res.stars
        if cur.kind == "web" and res.kind != "web":
            cur.kind = res.kind
        cur.extra.setdefault("also_seen_on", [])
        if res.engine and res.engine != cur.engine:
            cur.extra["also_seen_on"].append(res.engine)

    ordered = sorted(best.items(), key=lambda kv: scores[kv[0]], reverse=True)[:cap]
    out: list[SearchResult] = []
    for key, res in ordered:
        res.extra["rrf_score"] = round(scores[key], 6)
        out.append(res)
    return out
