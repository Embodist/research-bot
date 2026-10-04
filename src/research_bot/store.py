"""SQLite topic knowledge base.

Persists, across runs, a multi-level topic tree, the history of reports, the
knowledge items seen in each report, and a push ledger. Two jobs:

* **Increment tracking** — diffing this run's items against everything seen
  before, so a ``watch`` run can report only what is new or changed.
* **Dedup** — the push ledger lets a caller skip re-delivering knowledge that
  has already been sent (``should_push`` / ``record_push``).

Stdlib only (``sqlite3``). Recipient addresses are never stored — pushes keep a
recipient *count*, not the address — so the DB holds no personal data.
"""

from __future__ import annotations

import hashlib
import json
import logging
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .util import now_utc, slugify

log = logging.getLogger(__name__)

_SCHEMA = """
CREATE TABLE IF NOT EXISTS topics (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL UNIQUE,
    title      TEXT NOT NULL DEFAULT '',
    mode       TEXT NOT NULL DEFAULT '',
    parent_id  INTEGER REFERENCES topics(id),
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reports (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id      INTEGER NOT NULL REFERENCES topics(id),
    report_key    TEXT NOT NULL,
    mode          TEXT NOT NULL DEFAULT '',
    depth         TEXT NOT NULL DEFAULT '',
    md_path       TEXT NOT NULL DEFAULT '',
    json_path     TEXT NOT NULL DEFAULT '',
    coverage      REAL,
    source_count  INTEGER,
    finding_count INTEGER,
    run_url       TEXT NOT NULL DEFAULT '',
    created_at    TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS reports_topic_key ON reports(topic_id, report_key);
CREATE TABLE IF NOT EXISTS items (
    topic_id          INTEGER NOT NULL REFERENCES topics(id),
    norm_key          TEXT NOT NULL,
    title             TEXT NOT NULL DEFAULT '',
    kind              TEXT NOT NULL DEFAULT '',
    url               TEXT NOT NULL DEFAULT '',
    payload_hash      TEXT NOT NULL DEFAULT '',
    payload           TEXT NOT NULL DEFAULT '{}',
    first_seen_report INTEGER,
    last_seen_report  INTEGER,
    seen_count        INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (topic_id, norm_key)
);
CREATE TABLE IF NOT EXISTS pushes (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id   INTEGER NOT NULL REFERENCES topics(id),
    report_id  INTEGER,
    dedup_key  TEXT NOT NULL,
    channel    TEXT NOT NULL DEFAULT 'email',
    recipients INTEGER NOT NULL DEFAULT 0,
    subject    TEXT NOT NULL DEFAULT '',
    sent_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS pushes_dedup ON pushes(topic_id, dedup_key);
"""

_ITEM_GROUPS = (
    ("key_papers", "paper"),
    ("key_projects", "project"),
    ("key_datasets", "dataset"),
)


def norm_key(title: str, url: str = "") -> str:
    """Stable dedup key for an item: a slug of its title (falling back to URL)."""
    base = (title or "").strip() or (url or "").strip()
    key = slugify(base, 120)
    if key == "report" and url:
        key = slugify(url, 120)
    return key


def _canonical(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str)


def payload_hash(payload: Any) -> str:
    return hashlib.sha1(_canonical(payload).encode("utf-8", "ignore")).hexdigest()[:16]


def items_from_result(result: Any) -> list[dict[str, Any]]:
    """Flatten a :class:`ResearchResult` into dedup-able knowledge items."""
    items: list[dict[str, Any]] = []
    for sub in getattr(result, "subquestions", []) or []:
        ex = getattr(sub, "extraction", {}) or {}
        for finding in ex.get("findings") or []:
            point = (str(finding.get("point") or "")).strip()
            if not point:
                continue
            items.append(
                {
                    "title": point,
                    "kind": "finding",
                    "payload": {"evidence": finding.get("evidence", ""), "sources": finding.get("sources", [])},
                }
            )
        for field_name, kind in _ITEM_GROUPS:
            for entry in ex.get(field_name) or []:
                if isinstance(entry, str):
                    title, url = entry.strip(), ""
                    payload: Any = {"title": title}
                elif isinstance(entry, dict):
                    title = str(entry.get("title") or entry.get("name") or "").strip()
                    url = str(entry.get("url") or entry.get("link") or "").strip()
                    payload = entry
                else:
                    continue
                if title or url:
                    items.append({"title": title or url, "kind": kind, "url": url, "payload": payload})
        for problem in ex.get("open_problems") or []:
            text = str(problem or "").strip()
            if text:
                items.append({"title": text, "kind": "problem", "payload": {}})
    return items


@dataclass
class Increment:
    """Result of diffing a report's items against the store."""

    new: list[dict[str, Any]] = field(default_factory=list)
    updated: list[dict[str, Any]] = field(default_factory=list)
    known: int = 0

    @property
    def changed(self) -> int:
        return len(self.new) + len(self.updated)

    def dedup_key(self) -> str:
        keys = sorted(str(it.get("norm_key", "")) for it in self.new)
        return hashlib.sha1("|".join(keys).encode("utf-8", "ignore")).hexdigest()[:16]

    def to_dict(self) -> dict[str, Any]:
        return {
            "new": len(self.new),
            "updated": len(self.updated),
            "known": self.known,
            "changed": self.changed,
            "new_titles": [it.get("title", "") for it in self.new][:20],
        }


class KnowledgeStore:
    """A SQLite-backed knowledge base rooted at ``path``."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        if self.path.parent and str(self.path.parent) not in ("", "."):
            self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.executescript(_SCHEMA)
        self.conn.commit()

    def __enter__(self) -> KnowledgeStore:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def close(self) -> None:
        self.conn.close()

    # -- topics ---------------------------------------------------------------
    def upsert_topic(self, name: str, *, title: str = "", mode: str = "", parent: str | None = None) -> int:
        row = self.conn.execute("SELECT id FROM topics WHERE name = ?", (name,)).fetchone()
        parent_id = self.upsert_topic(parent) if parent else None
        stamp = now_utc().replace(microsecond=0).isoformat()
        if row:
            self.conn.execute(
                "UPDATE topics SET title = CASE WHEN ? <> '' THEN ? ELSE title END,"
                " mode = CASE WHEN ? <> '' THEN ? ELSE mode END,"
                " parent_id = COALESCE(?, parent_id) WHERE id = ?",
                (title, title, mode, mode, parent_id, row["id"]),
            )
            self.conn.commit()
            return int(row["id"])
        cur = self.conn.execute(
            "INSERT INTO topics(name, title, mode, parent_id, created_at) VALUES(?,?,?,?,?)",
            (name, title, mode, parent_id, stamp),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def topic_id(self, name: str) -> int | None:
        row = self.conn.execute("SELECT id FROM topics WHERE name = ?", (name,)).fetchone()
        return int(row["id"]) if row else None

    def topics(self) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT t.id, t.name, t.title, t.mode, t.parent_id, t.created_at,"
            " (SELECT COUNT(*) FROM reports r WHERE r.topic_id = t.id) AS reports,"
            " (SELECT COUNT(*) FROM items i WHERE i.topic_id = t.id) AS items"
            " FROM topics t ORDER BY t.id"
        ).fetchall()
        return [dict(r) for r in rows]

    def hierarchy(self, parent_id: int | None = None) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for t in self.topics():
            if t["parent_id"] == parent_id:
                node = dict(t)
                node["children"] = self.hierarchy(t["id"])
                out.append(node)
        return out

    # -- reports & items ------------------------------------------------------
    def record_report(
        self,
        topic_id: int,
        *,
        report_key: str,
        mode: str = "",
        depth: str = "",
        md_path: str = "",
        json_path: str = "",
        coverage: float | None = None,
        source_count: int | None = None,
        finding_count: int | None = None,
        run_url: str = "",
    ) -> int:
        stamp = now_utc().replace(microsecond=0).isoformat()
        cur = self.conn.execute(
            "INSERT INTO reports(topic_id, report_key, mode, depth, md_path, json_path, coverage,"
            " source_count, finding_count, run_url, created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            " ON CONFLICT(topic_id, report_key) DO UPDATE SET mode=excluded.mode, depth=excluded.depth,"
            " md_path=excluded.md_path, json_path=excluded.json_path, coverage=excluded.coverage,"
            " source_count=excluded.source_count, finding_count=excluded.finding_count, run_url=excluded.run_url",
            (
                topic_id, report_key, mode, depth, md_path, json_path, coverage,
                source_count, finding_count, run_url, stamp,
            ),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def record_items(self, topic_id: int, report_id: int, items: list[dict[str, Any]]) -> Increment:
        inc = Increment()
        for item in items:
            key = norm_key(str(item.get("title", "")), str(item.get("url", "")))
            phash = payload_hash(item.get("payload") or {"title": item.get("title", "")})
            rec = {
                "norm_key": key,
                "title": item.get("title", ""),
                "kind": item.get("kind", ""),
                "url": item.get("url", ""),
            }
            row = self.conn.execute(
                "SELECT payload_hash FROM items WHERE topic_id = ? AND norm_key = ?", (topic_id, key)
            ).fetchone()
            if row is None:
                self.conn.execute(
                    "INSERT INTO items(topic_id, norm_key, title, kind, url, payload_hash, payload,"
                    " first_seen_report, last_seen_report, seen_count) VALUES(?,?,?,?,?,?,?,?,?,1)",
                    (
                        topic_id, key, item.get("title", ""), item.get("kind", ""), item.get("url", ""),
                        phash, _canonical(item.get("payload") or {}), report_id, report_id,
                    ),
                )
                inc.new.append(rec)
            elif row["payload_hash"] != phash:
                self.conn.execute(
                    "UPDATE items SET payload_hash=?, payload=?, title=?, kind=?, url=?,"
                    " last_seen_report=?, seen_count=seen_count+1 WHERE topic_id=? AND norm_key=?",
                    (
                        phash, _canonical(item.get("payload") or {}), item.get("title", ""),
                        item.get("kind", ""), item.get("url", ""), report_id, topic_id, key,
                    ),
                )
                inc.updated.append(rec)
            else:
                self.conn.execute(
                    "UPDATE items SET last_seen_report=?, seen_count=seen_count+1"
                    " WHERE topic_id=? AND norm_key=?",
                    (report_id, topic_id, key),
                )
                inc.known += 1
        self.conn.commit()
        return inc

    def new_items(self, topic_id: int, limit: int = 50) -> list[dict[str, Any]]:
        """Items that have only ever been seen once (candidates for a fresh push)."""
        rows = self.conn.execute(
            "SELECT norm_key, title, kind, url, first_seen_report, seen_count FROM items"
            " WHERE topic_id = ? AND seen_count = 1 ORDER BY last_seen_report DESC LIMIT ?",
            (topic_id, limit),
        ).fetchall()
        return [dict(r) for r in rows]

    def recent_reports(self, limit: int = 20) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT r.id, r.report_key, r.mode, r.depth, r.coverage, r.source_count, r.created_at,"
            " t.name AS topic FROM reports r JOIN topics t ON t.id = r.topic_id"
            " ORDER BY r.id DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]

    # -- push ledger ----------------------------------------------------------
    def should_push(self, topic_id: int, dedup_key: str) -> bool:
        row = self.conn.execute(
            "SELECT 1 FROM pushes WHERE topic_id = ? AND dedup_key = ? LIMIT 1", (topic_id, dedup_key)
        ).fetchone()
        return row is None

    def record_push(
        self,
        topic_id: int,
        report_id: int | None,
        dedup_key: str,
        *,
        channel: str = "email",
        recipients: int = 0,
        subject: str = "",
    ) -> int:
        cur = self.conn.execute(
            "INSERT INTO pushes(topic_id, report_id, dedup_key, channel, recipients, subject, sent_at)"
            " VALUES(?,?,?,?,?,?,?)",
            (topic_id, report_id, dedup_key, channel, int(recipients or 0), subject,
             now_utc().replace(microsecond=0).isoformat()),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def stats(self) -> dict[str, Any]:
        one = lambda sql: self.conn.execute(sql).fetchone()[0]  # noqa: E731
        return {
            "path": str(self.path),
            "topics": one("SELECT COUNT(*) FROM topics"),
            "reports": one("SELECT COUNT(*) FROM reports"),
            "items": one("SELECT COUNT(*) FROM items"),
            "pushes": one("SELECT COUNT(*) FROM pushes"),
        }


def open_store(home: Path, cfg: Any) -> KnowledgeStore:
    """Open the store configured at ``cfg.kb.path`` (relative paths are under ``home``)."""
    path = Path(str(getattr(getattr(cfg, "kb", None), "path", "report/knowledge.db")))
    if not path.is_absolute():
        path = home / path
    return KnowledgeStore(path)
