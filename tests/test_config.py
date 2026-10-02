from __future__ import annotations

from pathlib import Path

from research_bot.config import DotDict, deep_merge, expand_env, find_home, load_config


def test_expand_env_default_and_value(monkeypatch):
    monkeypatch.setenv("RB_TEST_X", "hello")
    assert expand_env("${RB_TEST_X}") == "hello"
    assert expand_env("${RB_TEST_MISSING:-fallback}") == "fallback"
    assert expand_env("${RB_TEST_MISSING}") == ""
    assert expand_env(["${RB_TEST_X}", 1]) == ["hello", 1]
    assert expand_env({"k": "${RB_TEST_X}"}) == {"k": "hello"}


def test_deep_merge_nested():
    base = {"a": {"b": 1, "c": 2}, "d": 3}
    override = {"a": {"b": 9}}
    assert deep_merge(base, override) == {"a": {"b": 9, "c": 2}, "d": 3}
    assert base["a"]["b"] == 1  # not mutated


def test_dotdict_access():
    d = DotDict({"llm": {"model": "m"}})
    assert d.llm.model == "m"
    assert d.get_path("llm.model") == "m"
    assert d.get_path("nope.x", "def") == "def"


def test_load_config_missing_file_uses_defaults(tmp_path):
    cfg, home = load_config(path=tmp_path / "nope.yaml", home=tmp_path)
    assert cfg.llm.base_url
    assert "arxiv" in cfg.search.engines
    assert home == tmp_path


def test_load_config_reads_and_expands(tmp_path, monkeypatch):
    monkeypatch.setenv("MY_KEY", "secret")
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "config.yaml").write_text(
        "llm:\n  api_key: ${MY_KEY}\n  model: test-model\nresearch:\n  depth: deep\n", encoding="utf-8"
    )
    cfg, _ = load_config(home=tmp_path)
    assert cfg.llm.api_key == "secret"
    assert cfg.llm.model == "test-model"
    assert cfg.research.depth == "deep"
    assert cfg.search.timeout  # default preserved


def test_find_home(tmp_path, monkeypatch):
    monkeypatch.delenv("RESEARCH_BOT_HOME", raising=False)
    (tmp_path / "topics").mkdir()
    (tmp_path / "skills").mkdir()
    sub = tmp_path / "a" / "b"
    sub.mkdir(parents=True)
    assert find_home(sub) == tmp_path.resolve()


def test_find_home_env_override(tmp_path, monkeypatch):
    monkeypatch.setenv("RESEARCH_BOT_HOME", str(tmp_path))
    assert find_home(Path("/")) == tmp_path.resolve()
