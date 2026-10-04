from __future__ import annotations

from types import SimpleNamespace

from research_bot.store import (
    Increment,
    KnowledgeStore,
    items_from_result,
    norm_key,
    payload_hash,
)


def _store(tmp_path) -> KnowledgeStore:
    return KnowledgeStore(tmp_path / "kb.db")


def test_norm_key_prefers_title_then_url():
    assert norm_key("YuE: Scaling Open Foundation Models for Music") == norm_key(
        "YuE: Scaling Open Foundation Models for Music"
    )
    assert norm_key("", "https://arxiv.org/abs/2503.00301") == "httpsarxivorgabs250300301"


def test_payload_hash_stable_and_sensitive():
    assert payload_hash({"a": 1, "b": 2}) == payload_hash({"b": 2, "a": 1})
    assert payload_hash({"a": 1}) != payload_hash({"a": 2})


def test_record_items_new_then_known(tmp_path):
    s = _store(tmp_path)
    tid = s.upsert_topic("ai-music")
    r1 = s.record_report(tid, report_key="2026-10-04-ai-music")
    items = [{"title": "YuE", "kind": "paper", "payload": {"year": 2025}}]

    first = s.record_items(tid, r1, items)
    assert len(first.new) == 1 and first.updated == [] and first.known == 0

    r2 = s.record_report(tid, report_key="2026-10-05-ai-music")
    second = s.record_items(tid, r2, items)
    assert second.new == [] and second.updated == [] and second.known == 1
    assert s.new_items(tid) == []  # seen twice now
    s.close()


def test_record_items_detects_update(tmp_path):
    s = _store(tmp_path)
    tid = s.upsert_topic("ai-music")
    rid = s.record_report(tid, report_key="k1")
    s.record_items(tid, rid, [{"title": "YuE", "payload": {"citations": 10}}])
    inc = s.record_items(tid, rid, [{"title": "YuE", "payload": {"citations": 99}}])
    assert len(inc.updated) == 1 and inc.new == []
    s.close()


def test_push_ledger_dedup_and_no_pii(tmp_path):
    s = _store(tmp_path)
    tid = s.upsert_topic("ai-music")
    key = Increment(new=[{"norm_key": "yue"}]).dedup_key()
    assert s.should_push(tid, key) is True
    s.record_push(tid, None, key, recipients=2, subject="hello")
    assert s.should_push(tid, key) is False
    row = s.conn.execute("SELECT recipients, subject FROM pushes").fetchone()
    assert row["recipients"] == 2  # a count, never an address
    s.close()


def test_hierarchy_links_children(tmp_path):
    s = _store(tmp_path)
    parent = s.upsert_topic("music")
    child = s.upsert_topic("ai-music", parent="music", mode="watch")
    tree = s.hierarchy()
    assert [t["name"] for t in tree] == ["music"]
    assert tree[0]["children"][0]["name"] == "ai-music"
    assert s.topic_id("music") == parent and s.topic_id("ai-music") == child
    s.close()


def test_items_from_result_flattens_extraction():
    result = SimpleNamespace(
        subquestions=[
            SimpleNamespace(
                extraction={
                    "findings": [{"point": "YuE is open", "evidence": "e", "sources": [1]}],
                    "key_papers": [{"title": "YuE", "url": "https://arxiv.org/abs/2503.00301"}],
                    "key_projects": ["ACE-Step"],
                    "key_datasets": [],
                    "open_problems": ["licensing unclear"],
                }
            )
        ]
    )
    items = items_from_result(result)
    kinds = {it["kind"] for it in items}
    assert kinds == {"finding", "paper", "project", "problem"}
    assert any(it.get("url", "").endswith("2503.00301") for it in items)
