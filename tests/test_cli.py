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
        return SimpleNamespace(topic=topic.name, title=topic.title, report_md="# report")


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
