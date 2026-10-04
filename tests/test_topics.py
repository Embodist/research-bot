from __future__ import annotations

from research_bot.topics import topic_from_dict, topic_from_query


def test_topic_from_query_fallback_offline():
    # llm=None -> deterministic fallback, no network
    t = topic_from_query("C++ RAII 的核心思想与边界", llm=None)
    assert t.name  # non-empty slug
    assert t.title.startswith("C++ RAII")
    assert t.seed_queries == ["C++ RAII 的核心思想与边界"]
    assert t.keywords  # some usable keywords
    assert "的核心思想与边界" not in t.keywords  # long CJK blob filtered


def test_topic_from_query_empty_is_still_runnable():
    t = topic_from_query("", llm=None)
    assert t.name == "topic"
    assert t.seed_queries == []


def test_fallback_keywords_drop_generic_and_blobs():
    t = topic_from_query("the core idea of how 研究 knowledge", llm=None)
    for junk in ("the", "core", "idea", "how", "研究"):
        assert junk not in t.keywords
    assert "knowledge" in t.keywords  # a real term survives


def test_topic_from_dict_roundtrip():
    data = {
        "name": "my-topic",
        "title": "My Topic",
        "description": "desc",
        "keywords": ["a", "b"],
        "venues": ["NeurIPS"],
        "seed_queries": ["q1", "q2"],
        "sections": ["S1", "S2"],
    }
    t = topic_from_dict(data)
    assert t.name == "my-topic"
    assert t.keywords == ["a", "b"]
    assert t.sections == ["S1", "S2"]
    assert t.to_dict()["title"] == "My Topic"


def test_topic_from_dict_derives_name_from_title():
    t = topic_from_dict({"title": "Some Fancy Domain"})
    assert t.name == "some-fancy-domain"
