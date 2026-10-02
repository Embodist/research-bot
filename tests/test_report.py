from __future__ import annotations

import json
from pathlib import Path

from research_bot.config import load_config
from research_bot.engine import ResearchResult, SubQuestion
from research_bot.report import load_index, record_email, save_report


def _cfg(tmp_path: Path):
    cfg, _ = load_config(path=tmp_path / "nope.yaml", home=tmp_path)
    cfg.report.dir = "report"
    return cfg


def _result() -> ResearchResult:
    sub = SubQuestion(
        id="q1",
        question="What is new in VLA?",
        queries=["vla"],
        extraction={"findings": [{"point": "p", "sources": [1]}, {"point": "p2", "sources": [2]}]},
    )
    return ResearchResult(
        topic="vla",
        title="VLA frontier",
        query="",
        depth="quick",
        language="bilingual",
        started_at="2026-10-02T00:00:00+00:00",
        finished_at="2026-10-02T00:01:00+00:00",
        duration_s=60.0,
        rounds=1,
        plan={"title": "VLA frontier", "summary": "s"},
        subquestions=[sub],
        report_md="# VLA frontier\n\nSome findings [1].",
        references=[
            {"n": 1, "title": "A", "url": "https://a.com", "kind": "paper"},
            {"n": 2, "title": "B", "url": "https://b.com", "kind": "project"},
        ],
        engines=["arxiv", "github"],
        skills=["deep-research"],
        models={"primary": "deepseek-v4-flash"},
    )


def test_save_report_writes_artifacts_and_index(tmp_path):
    cfg = _cfg(tmp_path)
    result = _result()
    record, md_path = save_report(tmp_path, cfg, result)
    assert md_path.is_file()
    assert "参考来源" in md_path.read_text(encoding="utf-8")
    assert (tmp_path / "report" / "latest" / "vla.md").is_file()
    json_path = tmp_path / record["json_path"]
    assert json_path.is_file()
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    assert payload["topic"] == "vla"
    assert len(payload["references"]) == 2
    index = load_index(tmp_path, cfg)
    assert index[0]["id"] == record["id"]
    assert index[0]["sources"] == 2
    assert index[0]["findings"] == 2


def test_record_email_updates_index_and_push_log(tmp_path):
    cfg = _cfg(tmp_path)
    record, _ = save_report(tmp_path, cfg, _result())
    record_email(tmp_path, cfg, record, {"sent": True, "to": ["a@b.c"], "ts": "now", "error": None})
    index = load_index(tmp_path, cfg)
    assert index[0]["email"]["sent"] is True
    log = tmp_path / "report" / "push-log.jsonl"
    assert log.is_file()
    entry = json.loads(log.read_text(encoding="utf-8").strip().splitlines()[0])
    assert entry["email"]["sent"] is True


def test_index_is_newest_first_and_deduped(tmp_path):
    cfg = _cfg(tmp_path)
    r1 = _result()
    r1.topic = "vla"
    save_report(tmp_path, cfg, r1)
    r2 = _result()
    r2.topic = "ros2"
    save_report(tmp_path, cfg, r2)
    index = load_index(tmp_path, cfg)
    assert [r["topic"] for r in index] == ["ros2", "vla"]
