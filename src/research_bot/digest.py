"""Increment digest for ``watch`` runs.

A watch run is a *subscription*, not a daily full snapshot: it reports only what
moved — the newest works (new papers / projects / datasets) and the items that
keep recurring (trending) — and writes a feed (JSON + Atom + JSONL) that can be
subscribed to. The full 7-facet report is still archived under ``report/``.

Stdlib only; no new dependencies.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape as xml_escape
from xml.sax.saxutils import quoteattr

from .util import now_utc, slugify

log = logging.getLogger(__name__)

_WORK_KINDS = ("paper", "project", "dataset")


def _kinds_label(kind: str) -> str:
    return {"paper": "论文", "project": "项目", "dataset": "数据集", "finding": "发现", "problem": "问题"}.get(
        kind, kind or "-"
    )


def _year_num(raw: str) -> int:
    for token in str(raw or "").replace("/", "-").replace(".", "-").split("-"):
        token = token.strip()
        if len(token) == 4 and token.isdigit():
            return int(token)
    return 0


def _load_payload(raw: Any) -> dict[str, Any]:
    if isinstance(raw, dict):
        return raw
    try:
        data = json.loads(raw or "{}")
        return data if isinstance(data, dict) else {}
    except (TypeError, ValueError):
        return {}


def _name(item: dict[str, Any], payload: dict[str, Any]) -> str:
    return str(payload.get("title") or payload.get("name") or item.get("title") or item.get("url") or "").strip()


def _raw_feed_url(topic: str, ext: str) -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not repo:
        return ""
    branch = os.environ.get("GITHUB_REF_NAME") or "main"
    slug = slugify(topic, 80) or "topic"
    return f"https://raw.githubusercontent.com/{repo}/{branch}/report/feed/{slug}.{ext}"


def _hot_from_result(result: Any, limit: int) -> list[dict[str, Any]]:
    """Fallback "trending" for early runs: the current run's works that carry heat."""
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for sub in getattr(result, "subquestions", []) or []:
        ex = getattr(sub, "extraction", {}) or {}
        for group, kind in (("key_papers", "paper"), ("key_projects", "project"), ("key_datasets", "dataset")):
            for entry in ex.get(group) or []:
                if not isinstance(entry, dict):
                    continue
                payload = entry
                name = _name(entry, payload)
                key = slugify(name, 120)
                if not name or key in seen or not (payload.get("heat") or payload.get("attention")):
                    continue
                seen.add(key)
                out.append(
                    {
                        "key": key,
                        "title": name,
                        "kind": kind,
                        "url": str(payload.get("url") or payload.get("link") or ""),
                        "seen_count": 1,
                        "why": str(payload.get("why") or payload.get("heat") or ""),
                    }
                )
    return out[:limit]


def build_digest(
    store: Any,
    topic_id: int | None,
    result: Any,
    increment: Any,
    *,
    run_url: str = "",
    report_path: str = "",
    window: int = 7,
    max_items: int = 12,
) -> dict[str, Any]:
    """Assemble the increment payload for one watch run."""
    new_works: list[dict[str, Any]] = []
    for item in increment.new:
        if item.get("kind") not in _WORK_KINDS:
            continue
        payload = item.get("payload") or {}
        name = _name(item, payload)
        year = str(payload.get("year") or payload.get("published") or "")
        new_works.append(
            {
                "key": item.get("norm_key", ""),
                "title": name,
                "kind": item.get("kind", ""),
                "url": str(item.get("url") or payload.get("url") or payload.get("link") or ""),
                "year": year,
                "_year": _year_num(year),
                "why": str(payload.get("why") or ""),
                "heat": str(payload.get("heat") or ""),
                "authority": str(payload.get("authority") or ""),
                "attention": str(payload.get("attention") or ""),
                "recommendation": str(payload.get("recommendation") or ""),
            }
        )
    new_works.sort(key=lambda w: (w["_year"], w["title"]), reverse=True)
    new_works = new_works[:max_items]

    trending: list[dict[str, Any]] = []
    if topic_id is not None:
        for row in store.trending(topic_id, window=window, min_seen=2, limit=max_items):
            payload = _load_payload(row.get("payload"))
            trending.append(
                {
                    "key": row.get("norm_key", ""),
                    "title": _name(row, payload),
                    "kind": row.get("kind", ""),
                    "url": str(row.get("url") or payload.get("url") or payload.get("link") or ""),
                    "seen_count": int(row.get("seen_count") or 1),
                    "why": str(payload.get("why") or ""),
                }
            )
    if not trending:
        trending = _hot_from_result(result, max_items)
    trending = trending[:max_items]

    return {
        "topic": getattr(result, "topic", ""),
        "title": getattr(result, "title", getattr(result, "topic", "")),
        "generated_at": now_utc().replace(microsecond=0).isoformat(),
        "run_url": run_url,
        "report_path": report_path,
        "increment": {
            "new": len(increment.new),
            "updated": len(increment.updated),
            "known": increment.known,
            "changed": increment.changed,
        },
        "new_works": new_works,
        "trending": trending,
        "sources": len(getattr(result, "references", []) or []),
    }


def _cell(value: Any) -> str:
    return str(value or "-").replace("|", "\\|").replace("\n", " ")


def render_markdown(digest: dict[str, Any]) -> str:
    """Compact delta email body (never the full snapshot)."""
    day = str(digest.get("generated_at", ""))[:10]
    inc = digest.get("increment", {})
    works = digest.get("new_works") or []
    trending = digest.get("trending") or []
    lines = [
        f"# {digest.get('title') or digest.get('topic')} · 增量 {day}",
        "",
        f"> 增量订阅：只报**新作 + 趋势**。本期 +{inc.get('new', 0)} new · "
        f"~{inc.get('updated', 0)} updated · {inc.get('known', 0)} known。完整快照见归档。",
        "",
        f"## 🆕 最近新作（{len(works)}）",
        "",
    ]
    if works:
        lines.append("| 名称 | 类型 | 年份 | 热度 | 权威 | 关注度 | 推荐度 | 链接 |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for w in works:
            link = w.get("url") or ""
            cell = f"[{_cell(w.get('title'))}]({link})" if link else _cell(w.get("title"))
            lines.append(
                f"| {cell} | {_kinds_label(w.get('kind', ''))} | {_cell(w.get('year'))} | "
                f"{_cell(w.get('heat'))} | {_cell(w.get('authority'))} | {_cell(w.get('attention'))} | "
                f"{_cell(w.get('recommendation'))} | {link or '-'} |"
            )
    else:
        lines.append("_本期没有首次出现的新论文 / 项目 / 数据集。_")
    lines += ["", f"## 📈 Trending（{len(trending)}）", ""]
    if trending:
        lines.append("| 名称 | 类型 | 出现次数 | 链接 | 说明 |")
        lines.append("| --- | --- | --- | --- | --- |")
        for t in trending:
            link = t.get("url") or ""
            cell = f"[{_cell(t.get('title'))}]({link})" if link else _cell(t.get("title"))
            lines.append(
                f"| {cell} | {_kinds_label(t.get('kind', ''))} | {t.get('seen_count', 1)} | "
                f"{link or '-'} | {_cell(t.get('why'))} |"
            )
    else:
        lines.append("_暂无跨期重复出现的条目。_")
    lines.append("")
    if digest.get("report_path"):
        lines.append(f"完整快照：`{digest['report_path']}`")
    if digest.get("run_url"):
        lines.append(f"运行记录：{digest['run_url']}")
    lines.append("")
    lines.append("_订阅说明：本邮件为增量订阅，无新增/变化时当天不发；趋势取近几期重复出现的条目。_")
    return "\n".join(lines)


def render_atom(digest: dict[str, Any], *, feed_url: str = "") -> str:
    """Atom 1.0 feed so the increment stream can be added to any feed reader."""
    topic = str(digest.get("topic", "topic"))
    title = str(digest.get("title") or topic)
    updated = str(digest.get("generated_at", "")) or now_utc().replace(microsecond=0).isoformat()
    entries = [
        {
            "id": f"urn:research-bot:{topic}:{w.get('key') or slugify(w.get('title', ''), 120)}",
            "title": w.get("title", ""),
            "url": w.get("url", ""),
            "summary": " · ".join(x for x in (w.get("why"), w.get("heat")) if x) or _kinds_label(w.get("kind", "")),
        }
        for w in digest.get("new_works") or []
    ]
    if not entries:
        entries = [
            {
                "id": f"urn:research-bot:{topic}:trend:{t.get('key') or slugify(t.get('title', ''), 120)}",
                "title": f"[Trending] {t.get('title', '')}",
                "url": t.get("url", ""),
                "summary": t.get("why", "") or f"出现 {t.get('seen_count', 1)} 次",
            }
            for t in digest.get("trending") or []
        ]
    out = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        f"  <title>{xml_escape(title)} · 增量</title>",
        f"  <id>urn:research-bot:{xml_escape(topic)}</id>",
        f"  <updated>{xml_escape(updated)}</updated>",
        "  <author><name>research-bot</name></author>",
    ]
    if feed_url:
        out.append(f"  <link rel=\"self\" href={quoteattr(feed_url)}/>")
    for e in entries:
        out.append("  <entry>")
        out.append(f"    <id>{xml_escape(e['id'])}</id>")
        out.append(f"    <title>{xml_escape(e['title'])}</title>")
        if e.get("url"):
            out.append(f"    <link href={quoteattr(e['url'])}/>")
        out.append(f"    <updated>{xml_escape(updated)}</updated>")
        out.append(f"    <summary>{xml_escape(e['summary'])}</summary>")
        out.append("  </entry>")
    out.append("</feed>")
    return "\n".join(out) + "\n"


def write_feed(home: Path, cfg: Any, digest: dict[str, Any]) -> dict[str, Path]:
    """Write ``report/feed/<topic>.{json,xml,jsonl}`` for subscription."""
    feed_dir = home / str(cfg.report.dir) / "feed"
    feed_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(digest.get("topic", ""), 80) or "topic"
    json_path = feed_dir / f"{slug}.json"
    xml_path = feed_dir / f"{slug}.xml"
    jsonl_path = feed_dir / f"{slug}.jsonl"
    json_path.write_text(json.dumps(digest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    xml_path.write_text(render_atom(digest, feed_url=_raw_feed_url(digest.get("topic", ""), "xml")), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(digest, ensure_ascii=False) + "\n")
    return {"json": json_path, "xml": xml_path, "jsonl": jsonl_path}
