from __future__ import annotations

from pathlib import Path

from research_bot.config import load_config
from research_bot.engine import DeepResearchEngine, SourceRegistry, SubQuestion
from research_bot.search.base import SearchResult
from research_bot.topics import load_topic_file

REPO = Path(__file__).resolve().parents[1]


def _engine():
    cfg, home = load_config(path=REPO / "config" / "does-not-exist.yaml", home=REPO)
    cfg.search.engines = []  # avoid touching the network at construction
    return DeepResearchEngine(cfg, home)


def test_source_registry_dedup_and_numbering():
    reg = SourceRegistry()
    a = SearchResult(title="A", url="https://a.com/p?utm_source=x")
    b = SearchResult(title="B", url="https://b.com/p")
    assert reg.add(a) == 1
    assert reg.add(b) == 2
    assert reg.add(SearchResult(title="A2", url="https://www.a.com/p")) == 1  # same normalised url
    refs = reg.reference_list()
    assert [r["n"] for r in refs] == [1, 2]


def test_source_registry_index_of():
    reg = SourceRegistry()
    r = SearchResult(title="A", url="https://a.com/p")
    reg.add(r)
    assert reg.index_of(r) == 1
    assert reg.index_of(SearchResult(title="zzz", url="https://zzz.com")) is None


def test_normalise_plan_filters_and_fills():
    engine = _engine()
    topic = load_topic_file(REPO / "topics" / "vla.yaml")
    data = {
        "title": "T",
        "subquestions": [
            {"id": "q1", "question": "Q1", "queries": ["a", "b"]},
            {"question": "Q2"},  # missing queries -> filled from question
            {"queries": ["no question"]},  # dropped
        ],
    }
    plan = engine._normalise_plan(data, topic, "", 6)
    assert plan["title"] == "T"
    assert [s["question"] for s in plan["subquestions"]] == ["Q1", "Q2"]
    assert plan["subquestions"][1]["queries"] == ["Q2"]


def test_fallback_plan_uses_seed_queries():
    engine = _engine()
    topic = load_topic_file(REPO / "topics" / "ros2.yaml")
    plan = engine._fallback_plan(topic, "", 3)
    assert len(plan["subquestions"]) == 3
    assert plan["subquestions"][0]["queries"] == [topic.seed_queries[0]]
    plan2 = engine._fallback_plan(topic, "extra focus", 3)
    assert plan2["subquestions"][0]["queries"][0] == "extra focus"


def test_rank_results_prefers_preferred_engine_and_kind():
    engine = _engine()
    sub = SubQuestion(id="q1", question="q", prefer=["arxiv"])
    r1 = SearchResult(title="web", url="https://web.com/1", engine="bing", kind="web", extra={"rrf_score": 0.5})
    r2 = SearchResult(title="paper", url="https://arxiv.org/1", engine="arxiv", kind="paper", extra={"rrf_score": 0.5})
    ranked = engine._rank_results([r1, r2], sub, max_keep=5, recency_days=9999)
    assert ranked[0].title == "paper"


def test_candidate_block_contains_citation_numbers():
    engine = _engine()
    reg = SourceRegistry()
    res = SearchResult(title="Title", url="https://a.com", snippet="snip", engine="arxiv", kind="paper")
    reg.add(res)
    sub = SubQuestion(id="q1", question="q", results=[res])
    block = engine._candidate_block(sub, reg)
    assert "[1]" in block
    assert "https://a.com" in block
