from __future__ import annotations

from research_bot.config import load_config
from research_bot.search import rrf_fuse
from research_bot.search.base import Engine, SearchResult
from research_bot.search.engines import _crossref_date, _parse_bing, _reconstruct_abstract
from research_bot.search.router import SearchRouter


def _res(title, url, engine="arxiv", kind="paper", **kw):
    return SearchResult(title=title, url=url, engine=engine, kind=kind, **kw)


def test_rrf_fuse_orders_by_rank():
    pairs = [
        ("arxiv", _res("A", "https://a.com/1"), 0),
        ("arxiv", _res("B", "https://b.com/1"), 1),
        ("bing", _res("B", "https://b.com/1"), 0),
        ("bing", _res("C", "https://c.com/1"), 1),
    ]
    out = rrf_fuse(pairs)
    assert out[0].title == "B"  # appears high in two engines
    titles = [r.title for r in out]
    assert set(titles) == {"A", "B", "C"}


def test_rrf_fuse_merges_duplicate_urls():
    pairs = [
        ("arxiv", _res("Same", "https://x.com/p", snippet="short"), 0),
        ("bing", _res("Same", "https://www.x.com/p/", snippet="a much longer snippet"), 0),
    ]
    out = rrf_fuse(pairs)
    assert len(out) == 1
    assert out[0].snippet == "a much longer snippet"
    assert "also_seen_on" in out[0].extra


def test_rrf_fuse_skips_empty():
    out = rrf_fuse([("x", SearchResult(title="", url=""), 0)])
    assert out == []


def test_rrf_weights_academic_engines_above_html():
    # Same rank on each engine; the arXiv hit must outrank the so360 hit.
    pairs = [
        ("so360", _res("Junk", "https://so.com/junk"), 0),
        ("arxiv", _res("Paper", "https://arxiv.org/abs/1"), 0),
    ]
    out = rrf_fuse(pairs)
    assert [r.title for r in out] == ["Paper", "Junk"]


def test_parse_bing_html():
    html = """
    <li class="b_algo"><h2><a href="https://arxiv.org/abs/2406.09246">OpenVLA: An Open-Source VLA</a></h2>
    <p>We introduce OpenVLA, a 7B open-source vision-language-action model.</p></li>
    <li class="b_algo"><h2><a href="https://example.com/x">Another result</a></h2><p>snippet</p></li>
    """
    out = _parse_bing(html, 5)
    assert len(out) == 2
    assert out[0].url == "https://arxiv.org/abs/2406.09246"
    assert "OpenVLA" in out[0].title
    assert out[0].snippet.startswith("We introduce")


def test_reconstruct_abstract():
    inv = {"hello": [0], "world": [1]}
    assert _reconstruct_abstract(inv) == "hello world"
    assert _reconstruct_abstract(None) == ""


def test_crossref_date():
    assert _crossref_date({"date-parts": [[2024, 6, 9]]}) == "2024-06-09"
    assert _crossref_date({"date-parts": [[2024]]}) == "2024-01-01"
    assert _crossref_date(None) is None


class _FlakyEngine(Engine):
    name = "flaky"
    kind = "web"

    def __init__(self):
        self.calls = 0

    def search(self, query, limit):
        self.calls += 1
        raise RuntimeError("blocked")


class _GoodEngine(Engine):
    name = "good"
    kind = "web"

    def search(self, query, limit):
        return [SearchResult(title="t", url="https://good.example/1", engine="good")]


def test_router_circuit_breaker_disables_flaky_engine(tmp_path):
    cfg, _ = load_config(path="/nonexistent.yaml", home=tmp_path)
    router = SearchRouter(cfg.search)
    flaky, good = _FlakyEngine(), _GoodEngine(cfg.search)
    router.engines = [flaky, good]
    assert router.search("q1")
    assert router.search("q2")
    assert flaky.calls == router.failure_threshold
    assert "flaky" in router.disabled_engines
    router.search("q3")
    assert flaky.calls == router.failure_threshold
