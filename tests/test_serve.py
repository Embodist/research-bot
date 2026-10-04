from __future__ import annotations

import json
import threading
import time
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

from research_bot.config import load_config
from research_bot.engine import DeepResearchEngine, ResearchResult
from research_bot.serve import JobRegistry, _expand_dotted, _Handler, _validate_overrides

REPO = Path(__file__).resolve().parents[1]

_REPORT = """# Demo

1. 定位与背景（Positioning）
- 是什么、不是什么 [1]

2. 问题域（Problem Space）
- 核心问题与约束 [1]

3. 历史与演进（Evolution）
- 第一代解决 X，代价是 Y [1]

4. 核心机制（Mechanism）
- 原理；适用边界：仅当 Z 成立，反例…… [1]

5. 证据与评估（Evaluation）
- 基准指标 [1]

6. 实践与生态（Practice）
- 工具与学习路径 [1]

7. 关联与元层（Meta）
- 相邻领域与开放问题 [1]

## 参考来源
- [1] A — https://a
"""


def _fake_run(self, topic, *, query="", depth=None, rounds=None, progress=None):  # noqa: ANN001
    if progress:
        progress("plan ok")
        progress("retrieve ok")
    return ResearchResult(
        topic=topic.name,
        title=topic.title,
        query=query,
        depth=depth or "quick",
        language="bilingual",
        started_at="2026-01-01T00:00:00Z",
        report_md=_REPORT,
        references=[{"n": 1, "title": "A", "url": "https://a"}],
    )


@pytest.fixture()
def server(tmp_path, monkeypatch):
    monkeypatch.setattr(DeepResearchEngine, "run", _fake_run)
    cfg, home = load_config(REPO / "config" / "does-not-exist.yaml", tmp_path)
    cfg.search.engines = []  # never touch the network at construction
    cfg.llm.api_key = ""  # force the deterministic (no-LLM) topic path
    reg = JobRegistry(home, cfg, workers=1)
    reg.start()
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), type("H", (_Handler,), {"registry": reg, "api_token": ""}))
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        yield reg, port
    finally:
        httpd.shutdown()
        httpd.server_close()
        reg.stop()


def _req(port, method, path, body=None, token=None):  # noqa: ANN001
    conn = HTTPConnection("127.0.0.1", port, timeout=5)
    headers = {}
    data = None
    if body is not None:
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    conn.request(method, path, body=data, headers=headers)
    resp = conn.getresponse()
    raw = resp.read()
    conn.close()
    return resp.status, raw


def _wait(port, job_id, timeout=5.0):  # noqa: ANN001
    deadline = time.time() + timeout
    while time.time() < deadline:
        status, raw = _req(port, "GET", f"/research/{job_id}")
        data = json.loads(raw)
        if data["status"] in ("done", "failed"):
            return data
        time.sleep(0.02)
    raise AssertionError("job did not finish in time")


def test_healthz_open(server):
    _, port = server
    status, raw = _req(port, "GET", "/healthz")
    assert status == 200
    body = json.loads(raw)
    assert body["ok"] is True
    assert "queued" in body


def test_topics_listing(server):
    _, port = server
    status, raw = _req(port, "GET", "/topics")
    assert status == 200
    assert isinstance(json.loads(raw), list)


def test_knowledge_job_end_to_end(server):
    reg, port = server
    status, raw = _req(port, "POST", "/research", {"query": "C++ RAII 核心思想", "mode": "knowledge"})
    assert status == 202
    job_id = json.loads(raw)["job_id"]

    data = _wait(port, job_id)
    assert data["status"] == "done", data
    assert data["result"]["report_md"].startswith("#")
    assert data["coverage"]["score"] > 0
    assert len(data["coverage"]["facets"]) == 7

    status, raw = _req(port, "GET", f"/research/{job_id}/report")
    assert status == 200
    assert b"#" in raw


def test_research_job_free_text(server):
    _, port = server
    status, raw = _req(port, "POST", "/research", {"query": "vision language action models", "depth": "quick"})
    assert status == 202
    job_id = json.loads(raw)["job_id"]
    data = _wait(port, job_id)
    assert data["status"] == "done"
    assert data.get("coverage") is None  # research mode carries no coverage


def test_neither_query_nor_topic_is_422(server):
    _, port = server
    status, _ = _req(port, "POST", "/research", {"depth": "quick"})
    assert status == 422


def test_unknown_config_section_is_400(server):
    _, port = server
    status, raw = _req(port, "POST", "/research", {"query": "x", "config": {"bogus": 1}})
    assert status == 400
    assert "unknown config section" in json.loads(raw)["error"]


def test_bad_json_is_400(server):
    _, port = server
    status, _ = _req(port, "POST", "/research", b"{not json")
    assert status == 400


def test_report_not_ready_is_409(server):
    _, port = server
    status, raw = _req(port, "POST", "/research", {"query": "wait", "mode": "knowledge"})
    job_id = json.loads(raw)["job_id"]
    # immediately: may be queued/running, report should not be a 200 yet
    status, _ = _req(port, "GET", f"/research/{job_id}/report")
    assert status in (409, 200)  # 409 unless the worker finished first


def test_unknown_job_is_404(server):
    _, port = server
    status, _ = _req(port, "GET", "/research/deadbeef")
    assert status == 404


def test_auth_required_when_token_set(tmp_path, monkeypatch):
    monkeypatch.setattr(DeepResearchEngine, "run", _fake_run)
    cfg, home = load_config(REPO / "config" / "does-not-exist.yaml", tmp_path)
    cfg.search.engines = []
    cfg.llm.api_key = ""
    reg = JobRegistry(home, cfg, workers=1)
    reg.start()
    handler = type("H", (_Handler,), {"registry": reg, "api_token": "s3cret"})
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        assert _req(port, "GET", "/healthz")[0] == 200  # always open
        assert _req(port, "GET", "/topics")[0] == 401
        assert _req(port, "GET", "/topics", token="wrong")[0] == 401
        assert _req(port, "GET", "/topics", token="s3cret")[0] == 200
    finally:
        httpd.shutdown()
        httpd.server_close()
        reg.stop()


# -- unit tests for the config-parsing helpers ------------------------------
def test_expand_dotted_keys():
    assert _expand_dotted({"llm.model": "m", "research": {"depth": "deep"}}) == {
        "llm": {"model": "m"},
        "research": {"depth": "deep"},
    }


def test_validate_overrides():
    assert _validate_overrides(None) is None
    assert _validate_overrides({"llm": {}, "research.depth": "x"}) is None
    assert "unknown config section" in _validate_overrides({"nope": 1})
    assert _validate_overrides([1, 2]) is not None


def test_cancel_queued_job():
    reg = JobRegistry(Path("/tmp"), {"research": {}, "search": {}}, workers=1)
    job = reg.create({"query": "x"})  # no worker started -> stays QUEUED
    assert reg.cancel(job.id) == "cancelled"
    assert reg.cancel("missing") is None
