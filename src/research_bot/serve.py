"""HTTP service — turn research-bot into a ready-to-run web service.

Zero new dependencies: the server is built on the stdlib ``http.server``.

    rb serve --host 0.0.0.0 --port 8080 --workers 2

A request (free-text ``query`` or a known ``topic``, plus optional ``config``
overrides) is parsed into a :class:`~research_bot.topics.Topic` and a merged
config, then the deep-research pipeline runs **asynchronously** in a bounded
worker pool. ``mode`` selects the report frame: ``research`` (default, a topic
run), ``knowledge`` (learn a domain), or ``watch`` (track a domain's change).
The latter two also return a deterministic ``coverage`` report for the frame.
Clients poll for the report:

    GET  /healthz                 liveness + queue depth
    GET  /topics                  the built-in topics
    POST /research                start a job -> 202 {job_id, status}
    GET  /research/{id}           status + progress + result (+ coverage)
    GET  /research/{id}/report    the markdown report
    DELETE /research/{id}         cancel a queued job

Auth: when ``RESEARCH_BOT_API_TOKEN`` is set, every endpoint except ``/healthz``
requires ``Authorization: Bearer <token>``. If unset the service is OPEN (a
warning is logged at startup) — keep it on a trusted network or behind a proxy.
"""

from __future__ import annotations

import hmac
import json
import logging
import os
import queue
import signal
import threading
import uuid
from dataclasses import dataclass, field
from enum import Enum
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from . import __version__
from .config import DEFAULTS, _wrap, deep_merge, expand_env, find_home, load_config
from .emailer import is_configured, send_report
from .engine import DeepResearchEngine, ResearchResult
from .knowledge import FRAMES, build_knowledge_topic, evaluate_coverage, get_frame
from .report import save_report
from .topics import Topic, load_topics, topic_from_query
from .util import now_utc

log = logging.getLogger("research_bot.serve")

MAX_BODY = 256 * 1024  # 256 KB request cap
MAX_PROGRESS = 200  # keep the tail of the progress log per job
MAX_JOBS = 200  # prune oldest finished jobs beyond this

_REPORT_LOCK = threading.Lock()  # serialize report/index writes across workers


class JobStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class Job:
    id: str
    request: dict[str, Any]
    status: JobStatus = JobStatus.QUEUED
    topic: str = ""
    progress: list[str] = field(default_factory=list)
    result: ResearchResult | None = None
    coverage: dict[str, Any] | None = None
    error: str = ""
    created_at: str = ""
    finished_at: str = ""

    def summary(self, *, include_result: bool = True) -> dict[str, Any]:
        data: dict[str, Any] = {
            "job_id": self.id,
            "status": self.status.value,
            "topic": self.topic,
            "progress": self.progress[-20:],
            "created_at": self.created_at,
            "finished_at": self.finished_at,
        }
        if self.error:
            data["error"] = self.error
        if include_result and self.result is not None:
            data["result"] = self.result.to_dict()
            data["report_url"] = f"/research/{self.id}/report"
        if self.coverage is not None:
            data["coverage"] = self.coverage
        return data


class JobRegistry:
    """Bounded, in-memory job queue backed by a small worker pool."""

    def __init__(self, home: Path, base_cfg: Any, *, workers: int = 2) -> None:
        self.home = Path(home)
        self.base_cfg = base_cfg
        self.workers = max(1, int(workers))
        self._jobs: dict[str, Job] = {}
        self._lock = threading.Lock()
        self._queue: queue.Queue[str | None] = queue.Queue()
        self._threads: list[threading.Thread] = []

    # -- lifecycle ----------------------------------------------------------
    def start(self) -> None:
        for i in range(self.workers):
            t = threading.Thread(target=self._worker, name=f"rb-worker-{i}", daemon=True)
            t.start()
            self._threads.append(t)

    def stop(self) -> None:
        for _ in self._threads:
            self._queue.put(None)
        for t in self._threads:
            t.join(timeout=5)

    # -- public API ---------------------------------------------------------
    def create(self, request: dict[str, Any]) -> Job:
        job = Job(id=uuid.uuid4().hex, request=request, created_at=now_utc().isoformat())
        with self._lock:
            self._jobs[job.id] = job
            self._prune_locked()
        self._queue.put(job.id)
        return job

    def get(self, job_id: str) -> Job | None:
        with self._lock:
            return self._jobs.get(job_id)

    def counts(self) -> dict[str, int]:
        with self._lock:
            jobs = list(self._jobs.values())
        return {
            "total": len(jobs),
            "queued": sum(j.status == JobStatus.QUEUED for j in jobs),
            "running": sum(j.status == JobStatus.RUNNING for j in jobs),
            "done": sum(j.status == JobStatus.DONE for j in jobs),
            "failed": sum(j.status == JobStatus.FAILED for j in jobs),
        }

    def cancel(self, job_id: str) -> str | None:
        """Return a status string, or None if the job does not exist."""
        with self._lock:
            job = self._jobs.get(job_id)
            if job is None:
                return None
            if job.status == JobStatus.QUEUED:
                job.status = JobStatus.CANCELLED
                job.finished_at = now_utc().isoformat()
            return job.status.value

    # -- internals ----------------------------------------------------------
    def _prune_locked(self) -> None:
        if len(self._jobs) <= MAX_JOBS:
            return
        finished = [j for j in self._jobs.values() if j.status in (JobStatus.DONE, JobStatus.FAILED, JobStatus.CANCELLED)]
        finished.sort(key=lambda j: j.created_at)
        for job in finished[: len(self._jobs) - MAX_JOBS]:
            self._jobs.pop(job.id, None)

    def _worker(self) -> None:
        while True:
            job_id = self._queue.get()
            if job_id is None:  # shutdown sentinel
                return
            job = self.get(job_id)
            if job is None or job.status == JobStatus.CANCELLED:
                continue
            job.status = JobStatus.RUNNING

            def progress(msg: str, _job: Job = job) -> None:
                _job.progress.append(msg)
                if len(_job.progress) > MAX_PROGRESS:
                    del _job.progress[: len(_job.progress) - MAX_PROGRESS]

            try:
                self._execute(job, progress)
                if job.status != JobStatus.CANCELLED:
                    job.status = JobStatus.DONE
            except Exception as exc:  # noqa: BLE001 - a bad job must not kill the worker
                log.exception("job %s failed", job.id)
                job.error = f"{type(exc).__name__}: {exc}"
                job.status = JobStatus.FAILED
            finally:
                job.finished_at = now_utc().isoformat()

    def _execute(self, job: Job, progress: Any) -> None:
        cfg, topic, rounds, want_email = self._prepare(job.request)
        engine = DeepResearchEngine(cfg, self.home)
        job.topic = topic.name
        result = engine.run(topic, query=str(job.request.get("query") or ""), depth=cfg.research.depth,
                            rounds=rounds, progress=progress)

        mode = str(job.request.get("mode") or "research").lower()
        coverage = None
        if mode in FRAMES:
            coverage = evaluate_coverage(result, frame=mode).to_dict()

        with _REPORT_LOCK:
            record, md_path = save_report(self.home, cfg, result, run_meta={})
            if want_email and is_configured(cfg.email):
                rec = send_report(cfg.email, result, report_path=md_path)
                log.info("job %s email: sent=%s to=%s", job.id, rec.get("sent"), rec.get("to"))

        job.result = result
        job.coverage = coverage
        job.request["_record"] = record.get("id", "")

    def _prepare(self, request: dict[str, Any]) -> tuple[Any, Topic, int | None, bool]:
        overrides = request.get("config") or {}
        cfg = _wrap(expand_env(deep_merge(self.base_cfg, _expand_dotted(overrides))))

        depth = request.get("depth")
        if depth:
            cfg.research.depth = str(depth)
        language = request.get("language")
        if language:
            cfg.research.language = str(language)
        if request.get("fetch") is False:
            cfg.search.fetch_pages = False

        mode = str(request.get("mode") or "research").lower()
        if mode in FRAMES:
            skill = get_frame(mode).skill
            names = list(cfg.research.skills or [])
            if skill not in names:
                cfg.research.skills = [*names, skill]

        query = str(request.get("query") or "").strip()
        topic_name = str(request.get("topic") or "").strip()

        if mode in FRAMES:
            topic = build_knowledge_topic(query or topic_name, frame=mode, language=str(cfg.research.language))
        elif topic_name and topic_name in load_topics(self.home):
            topic = load_topics(self.home)[topic_name]
        else:
            seed = query or topic_name
            topic = topic_from_query(seed, llm=_parse_llm(cfg))

        rounds = request.get("rounds")
        rounds = int(rounds) if isinstance(rounds, int) and rounds > 0 else None
        want_email = bool(request.get("email"))
        return cfg, topic, rounds, want_email


def _parse_llm(cfg: Any):
    """An LLM for free-text->topic parsing; None if no key (uses fallback)."""
    try:
        from .llm import LLM

        llm = LLM(cfg.llm)
        return llm if llm.api_key else None
    except Exception:  # noqa: BLE001
        return None


def _expand_dotted(overrides: dict[str, Any]) -> dict[str, Any]:
    """Accept both nested and dotted keys: {'llm.model': x} -> {'llm': {'model': x}}."""
    out: dict[str, Any] = {}
    for key, value in (overrides or {}).items():
        if not isinstance(key, str):
            continue
        parts = key.split(".")
        node = out
        for part in parts[:-1]:
            node = node.setdefault(part, {})
            if not isinstance(node, dict):  # pragma: no cover - conflict
                break
        else:
            if isinstance(node, dict):
                node[parts[-1]] = value
    return out


def _validate_overrides(overrides: Any) -> str | None:
    if overrides is None:
        return None
    if not isinstance(overrides, dict):
        return "'config' must be an object"
    for key in overrides:
        top = str(key).split(".", 1)[0]
        if top not in DEFAULTS:
            return f"unknown config section: {top!r} (allowed: {', '.join(sorted(DEFAULTS))})"
    return None


# ---------------------------------------------------------------------------
# HTTP handler
# ---------------------------------------------------------------------------
class _Handler(BaseHTTPRequestHandler):
    server_version = f"research-bot/{__version__}"
    registry: JobRegistry  # bound by run_server()
    api_token: str | None = ""

    # -- helpers ------------------------------------------------------------
    def log_message(self, fmt: str, *args: Any) -> None:  # route to logging
        log.info("%s - %s", self.address_string(), fmt % args)

    def _send_json(self, code: int, payload: Any, *, headers: dict[str, str] | None = None) -> None:
        body = json.dumps(payload, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _send_text(self, code: int, text: str) -> None:
        body = text.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/markdown; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _authed(self) -> bool:
        token = self.api_token
        if not token:
            return True
        header = self.headers.get("Authorization", "")
        prefix = "Bearer "
        presented = header[len(prefix):] if header.startswith(prefix) else ""
        if presented and hmac.compare_digest(presented, token):
            return True
        self._send_json(401, {"error": "unauthorized"}, headers={"WWW-Authenticate": "Bearer"})
        return False

    def _read_body(self) -> dict[str, Any] | None:
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            self._send_json(400, {"error": "invalid Content-Length"})
            return None
        if length <= 0:
            self._send_json(400, {"error": "empty body"})
            return None
        if length > MAX_BODY:
            self._send_json(413, {"error": f"body too large (>{MAX_BODY} bytes)"})
            return None
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError) as exc:
            self._send_json(400, {"error": f"invalid JSON: {exc}"})
            return None
        if not isinstance(data, dict):
            self._send_json(400, {"error": "body must be a JSON object"})
            return None
        return data

    # -- routing ------------------------------------------------------------
    def do_GET(self) -> None:  # noqa: N802
        path = urlsplit(self.path).path.rstrip("/") or "/"
        if path == "/healthz":
            counts = self.registry.counts()
            self._send_json(200, {"ok": True, "version": __version__, **counts})
            return
        if not self._authed():
            return
        if path == "/topics":
            topics = load_topics(self.registry.home)
            self._send_json(200, [t.to_dict() for t in topics.values()])
            return
        parts = path.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "research":
            job = self.registry.get(parts[1])
            if job is None:
                self._send_json(404, {"error": "job not found"})
                return
            self._send_json(200, job.summary())
            return
        if len(parts) == 3 and parts[0] == "research" and parts[2] == "report":
            job = self.registry.get(parts[1])
            if job is None:
                self._send_json(404, {"error": "job not found"})
                return
            if job.result is None:
                self._send_json(409, {"error": f"report not ready (status={job.status.value})"})
                return
            self._send_text(200, job.result.report_md)
            return
        self._send_json(404, {"error": "not found"})

    def do_POST(self) -> None:  # noqa: N802
        path = urlsplit(self.path).path.rstrip("/") or "/"
        if not self._authed():
            return
        if path != "/research":
            self._send_json(404, {"error": "not found"})
            return
        body = self._read_body()
        if body is None:
            return
        query = str(body.get("query") or "").strip()
        topic = str(body.get("topic") or "").strip()
        mode = str(body.get("mode") or "research").lower()
        if not query and not topic:
            self._send_json(422, {"error": "provide 'query' (free text) or 'topic' (name)"})
            return
        if mode not in ("research", *FRAMES):
            self._send_json(422, {"error": f"mode must be one of: research, {', '.join(FRAMES)}"})
            return
        err = _validate_overrides(body.get("config"))
        if err:
            self._send_json(400, {"error": err})
            return
        job = self.registry.create(body)
        self._send_json(202, {"job_id": job.id, "status": job.status.value})

    def do_DELETE(self) -> None:  # noqa: N802
        path = urlsplit(self.path).path.rstrip("/") or "/"
        if not self._authed():
            return
        parts = path.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "research":
            status = self.registry.cancel(parts[1])
            if status is None:
                self._send_json(404, {"error": "job not found"})
            elif status == "cancelled":
                self._send_json(202, {"job_id": parts[1], "status": status})
            else:
                self._send_json(409, {"error": f"cannot cancel (status={status})"})
            return
        self._send_json(404, {"error": "not found"})


def run_server(
    *,
    host: str = "127.0.0.1",
    port: int = 8080,
    workers: int = 2,
    home: Path | None = None,
    config_path: str | None = None,
) -> int:
    home = Path(home) if home else find_home()
    base_cfg, home = load_config(config_path, home)
    registry = JobRegistry(home, base_cfg, workers=workers)
    registry.start()

    token = os.environ.get("RESEARCH_BOT_API_TOKEN") or None
    handler = type("_BoundHandler", (_Handler,), {"registry": registry, "api_token": token or ""})

    httpd = ThreadingHTTPServer((host, int(port)), handler)
    httpd.daemon_threads = True

    if token:
        log.info("auth: bearer token required (RESEARCH_BOT_API_TOKEN is set)")
    else:
        log.warning("auth: DISABLED — service is OPEN. Set RESEARCH_BOT_API_TOKEN to require a bearer token.")

    def _shutdown(signum: int, _frame: Any) -> None:
        log.info("received signal %s; shutting down", signum)
        threading.Thread(target=httpd.shutdown, daemon=True).start()

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            signal.signal(sig, _shutdown)
        except (ValueError, OSError):  # pragma: no cover - non-main thread
            pass

    log.info("research-bot %s serving on http://%s:%s (workers=%d, home=%s)", __version__, host, port, workers, home)
    try:
        httpd.serve_forever()
    finally:
        httpd.server_close()
        registry.stop()
    return 0
