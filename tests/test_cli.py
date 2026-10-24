import argparse
import copy
from pathlib import Path
from types import SimpleNamespace

import pytest

import research_bot.cli as cli
from research_bot.config import DEFAULTS, _wrap


def _namespace(**over):
    base = dict(
        config=None, no_fetch=False, depth="quick", query="", rounds=None, topic=["vla"],
        knowledge=False, watch=False, kb=False, email=False, no_email=False,
        dry_run_email=False, json=False,
    )
    base.update(over)
    return argparse.Namespace(**base)


class _FakeEngine:
    def __init__(self, cfg, home):
        self.router = SimpleNamespace(engine_names=["fake"])
        self.skills = [SimpleNamespace(name="deep-research")]

    def run(self, topic, query="", depth=None, rounds=None, progress=None):
        return SimpleNamespace(
            topic=topic.name,
            title=topic.title,
            report_md="# report",
            references=[{"n": 1, "title": "src", "url": "https://example.org"}],
            subquestions=[
                SimpleNamespace(
                    extraction={
                        "key_papers": [
                            {"title": "Paper A", "url": "https://a", "year": "2025", "heat": "10 cites"}
                        ]
                    }
                )
            ],
        )


@pytest.fixture
def patched(monkeypatch):
    cfg = _wrap(copy.deepcopy(DEFAULTS))
    cfg.email.enabled = False  # as in CI, where no config.yaml exists
    cfg.kb.enabled = False
    monkeypatch.setattr(cli, "load_config", lambda *a, **k: (cfg, Path("/tmp/fake-home")))
    monkeypatch.setattr(cli, "DeepResearchEngine", _FakeEngine)
    monkeypatch.setattr(cli, "load_topics", lambda home: {})
    monkeypatch.setattr(cli, "resolve_topics", lambda topics, names: [SimpleNamespace(name="vla", title="VLA")])
    monkeypatch.setattr(cli, "git_metadata", lambda home: {})
    monkeypatch.setattr(
        cli, "save_report",
        lambda home, cfg, result, run_meta=None: (
            {
                "id": "2026-10-04-vla", "topic": "vla", "depth": "quick",
                "report_path": "report/latest/vla.md", "json_path": "report/latest/vla.json",
                "sources": 1, "findings": 1, "duration_s": 1.0,
            },
            Path("/tmp/fake-home/report/latest/vla.md"),
        ),
    )
    monkeypatch.setattr(cli, "record_email", lambda *a, **k: None)
    calls: list[str] = []

    def fake_send(cfg_email, result, report_path=None, dry_run=False):
        calls.append(result.topic)
        return {"sent": True, "to": ["x@y.z"], "error": None}

    monkeypatch.setattr(cli, "send_report", fake_send)
    return cfg, calls


def test_email_flag_forces_delivery_when_config_disabled(patched):
    cfg, calls = patched
    assert cli.cmd_run(_namespace(email=True)) == 0
    assert cfg.email.enabled is True
    assert calls == ["vla"]


def test_without_email_flag_disabled_config_sends_nothing(patched):
    cfg, calls = patched
    assert cli.cmd_run(_namespace(email=False)) == 0
    assert cfg.email.enabled is False
    assert calls == []


def test_watch_run_sends_increment_digest_and_writes_feed(monkeypatch, tmp_path):
    cfg = _wrap(copy.deepcopy(DEFAULTS))
    cfg.email.enabled = False
    cfg.kb.enabled = False
    cfg.kb.path = str(tmp_path / "kb.db")

    monkeypatch.setattr(cli, "load_config", lambda *a, **k: (cfg, tmp_path))
    monkeypatch.setattr(cli, "DeepResearchEngine", _FakeEngine)
    monkeypatch.setattr(cli, "git_metadata", lambda home: {})
    monkeypatch.setattr(
        cli,
        "save_report",
        lambda home, cfg, result, run_meta=None: (
            {
                "id": f"2026-10-04-{result.topic}",
                "topic": result.topic,
                "depth": "quick",
                "report_path": f"report/latest/{result.topic}.md",
                "json_path": "",
                "sources": 1,
                "findings": 1,
                "duration_s": 1.0,
                "run_url": "",
            },
            home / f"report/latest/{result.topic}.md",
        ),
    )
    monkeypatch.setattr(cli, "record_email", lambda *a, **k: None)
    sent: list[dict] = []

    def fake_increment(cfg_email, digest, dry_run=False):
        sent.append(digest)
        return {"sent": True, "to": ["x@y.z"], "error": None, "dry_run": dry_run, "kind": "increment"}

    monkeypatch.setattr(cli, "send_increment", fake_increment)

    assert cli.cmd_run(_namespace(email=True, watch=True, query="demo", kb=True)) == 0
    assert sent and sent[0]["topic"] == "demo"
    assert sent[0]["new_works"][0]["title"] == "Paper A"
    assert list((tmp_path / "report" / "feed").glob("*.json"))
