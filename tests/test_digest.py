from __future__ import annotations

from types import SimpleNamespace
from xml.etree import ElementTree as ET

from research_bot.config import _wrap
from research_bot.digest import build_digest, render_atom, render_markdown, write_feed
from research_bot.emailer import send_increment
from research_bot.store import KnowledgeStore, items_from_result


def _result(topic: str, papers: list[dict]) -> SimpleNamespace:
    return SimpleNamespace(
        topic=topic,
        title=f"{topic} report",
        references=[{}],
        subquestions=[SimpleNamespace(extraction={"key_papers": papers})],
    )


def _cfg() -> SimpleNamespace:
    return SimpleNamespace(report=SimpleNamespace(dir="report"))


def test_build_digest_splits_new_works_and_trending(tmp_path):
    store = KnowledgeStore(tmp_path / "kb.db")
    tid = store.upsert_topic("demo")
    alpha = {"title": "Alpha", "url": "https://a", "year": "2024", "heat": "10 cites", "authority": "NeurIPS"}
    beta = {"title": "Beta", "url": "https://b", "year": "2025", "heat": "5 cites"}

    r1 = store.record_report(tid, report_key="k1")
    store.record_items(tid, r1, items_from_result(_result("demo", [alpha])))
    r2 = store.record_report(tid, report_key="k2")
    inc = store.record_items(tid, r2, items_from_result(_result("demo", [alpha, beta])))

    digest = build_digest(store, tid, _result("demo", [alpha, beta]), inc)
    assert [w["title"] for w in digest["new_works"]] == ["Beta"]
    assert "Alpha" in [t["title"] for t in digest["trending"]]
    assert digest["increment"] == {"new": 1, "updated": 0, "known": 1, "changed": 1}

    md = render_markdown(digest)
    assert "最近新作" in md and "Trending" in md and "Beta" in md and "Alpha" in md
    root = ET.fromstring(render_atom(digest))
    assert root.tag.endswith("feed")
    store.close()


def test_write_feed_writes_json_xml_and_appends_jsonl(tmp_path):
    digest = {
        "topic": "demo",
        "title": "Demo",
        "generated_at": "2026-10-04T00:00:00",
        "run_url": "",
        "report_path": "report/latest/demo.md",
        "increment": {"new": 1, "updated": 0, "known": 0, "changed": 1},
        "new_works": [
            {
                "key": "beta",
                "title": "Beta",
                "kind": "paper",
                "url": "https://b",
                "year": "2025",
                "why": "",
                "heat": "",
                "authority": "",
                "attention": "",
                "recommendation": "",
            }
        ],
        "trending": [],
        "sources": 1,
    }
    paths = write_feed(tmp_path, _cfg(), digest)
    assert paths["json"].is_file() and paths["xml"].is_file() and paths["jsonl"].is_file()
    assert paths["json"].parent == tmp_path / "report" / "feed"
    write_feed(tmp_path, _cfg(), digest)
    assert len(paths["jsonl"].read_text(encoding="utf-8").splitlines()) == 2


def test_send_increment_dry_run():
    cfg = _wrap(
        {
            "enabled": True,
            "to": ["x@y.z"],
            "subject_prefix": "[rb]",
            "from": "a@b.c",
            "smtp_host": "h",
            "username": "u",
            "password": "p",
            "smtp_port": 465,
            "smtp_ssl": True,
        }
    )
    digest = {
        "topic": "demo",
        "title": "Demo",
        "generated_at": "2026-10-04T00:00:00",
        "increment": {"new": 0, "updated": 0, "known": 0, "changed": 0},
        "new_works": [],
        "trending": [],
    }
    rec = send_increment(cfg, digest, dry_run=True)
    assert rec["sent"] is True and rec["kind"] == "increment"
