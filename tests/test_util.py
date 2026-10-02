from __future__ import annotations

import json

import pytest

from research_bot.util import (
    extract_json,
    html_to_text,
    is_recent,
    norm_url,
    parse_date,
    slugify,
    stable_id,
    truncate,
)


def test_extract_json_plain():
    assert extract_json('{"a": 1}') == {"a": 1}


def test_extract_json_fenced_and_prose():
    text = 'Here you go:\n```json\n{"a": [1, 2], "b": "x"}\n```\nthanks'
    assert extract_json(text) == {"a": [1, 2], "b": "x"}


def test_extract_json_trailing_comma():
    assert extract_json('{"a": 1, "b": [1,2,],}') == {"a": 1, "b": [1, 2]}


def test_extract_json_raises():
    with pytest.raises(ValueError):
        extract_json("no json here at all")


def test_html_to_text_strips_scripts_and_tags():
    raw = "<html><head><script>var x=1;</script><title>T</title></head><body><h1>Hi</h1><p>Hello&nbsp;<b>world</b></p></body></html>"
    text = html_to_text(raw)
    assert "var x" not in text
    assert "Hello" in text and "world" in text


def test_norm_url_dedup():
    a = norm_url("https://www.Example.com/path/?utm_source=x&b=2")
    b = norm_url("https://example.com/path?b=2")
    assert a == b


def test_slugify_and_truncate():
    assert slugify("Vision-Language-Action 模型") == "vision-language-action-模型"
    assert len(truncate("x" * 100, 10)) == 10


def test_stable_id_deterministic():
    assert stable_id("a", "b") == stable_id("a", "b")
    assert stable_id("a", "b") != stable_id("a", "c")


def test_parse_date_and_recent():
    assert parse_date("2026-10-02").year == 2026
    assert is_recent("2026-10-01", 30) is True
    assert is_recent("2001-01-01", 30) is False
    assert is_recent(None, 30) is True


def test_json_dumps_roundtrip():
    payload = {"名字": "值", "n": 1}
    assert json.loads(json.dumps(payload, ensure_ascii=False)) == payload
