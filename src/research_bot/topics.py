"""Topic definitions — the standing research beats this bot tracks daily.

Each topic lives in ``topics/<name>.yaml`` and combines: seed queries, target
venues, recurring keywords and a curated seed catalogue (classic papers,
projects, datasets). The planner uses it to bias decomposition; the synthesiser
uses it as the required report structure; the seed catalogue guarantees a useful
report even if every network source is unavailable.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .util import slugify

log = logging.getLogger(__name__)


@dataclass
class Topic:
    name: str
    title: str
    description: str = ""
    keywords: list[str] = field(default_factory=list)
    venues: list[str] = field(default_factory=list)
    seed_queries: list[str] = field(default_factory=list)
    sections: list[str] = field(default_factory=list)
    seed_resources: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    path: Path | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "keywords": self.keywords,
            "venues": self.venues,
            "seed_queries": self.seed_queries,
            "sections": self.sections,
            "seed_resources": self.seed_resources,
        }


def load_topic_file(path: Path) -> Topic:
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    name = str(data.get("name") or path.stem)
    return Topic(
        name=name,
        title=str(data.get("title") or name),
        description=str(data.get("description") or ""),
        keywords=list(data.get("keywords") or []),
        venues=list(data.get("venues") or []),
        seed_queries=list(data.get("seed_queries") or []),
        sections=list(data.get("sections") or []),
        seed_resources=dict(data.get("seed_resources") or {}),
        path=path,
        raw=data,
    )


def load_topics(home: Path) -> dict[str, Topic]:
    topics: dict[str, Topic] = {}
    root = home / "topics"
    if not root.is_dir():
        return topics
    for path in sorted(root.glob("*.yaml")):
        try:
            topic = load_topic_file(path)
        except Exception as exc:  # noqa: BLE001
            log.warning("cannot load topic %s: %s", path, exc)
            continue
        topics[topic.name] = topic
    return topics


def resolve_topics(all_topics: dict[str, Topic], names: list[str]) -> list[Topic]:
    if not names or names == ["all"]:
        return list(all_topics.values())
    out: list[Topic] = []
    for name in names:
        topic = all_topics.get(name)
        if topic is None:
            log.warning("unknown topic %r (available: %s)", name, ", ".join(sorted(all_topics)))
            continue
        out.append(topic)
    return out


# ---------------------------------------------------------------------------
# Building topics from a request (free text or a dict) — used by the HTTP
# service and `rb run --query`, so a new research request does not need a
# hand-written topics/<name>.yaml on disk.
# ---------------------------------------------------------------------------
# Words that cannot on their own prove topical relevance (mirrors the engine's
# generic-token gate); dropped from fallback keywords.
_GENERIC = frozenset(
    {
        "the", "and", "for", "with", "how", "what", "why", "core", "idea", "ideas",
        "concept", "concepts", "principle", "principles", "basic", "introduction",
        "overview", "guide", "survey", "tutorial", "研究", "核心", "思想", "原理",
        "概念", "介绍", "概述", "知识", "体系", "领域", "如何", "什么", "为什么",
    }
)

_SCHEMA_HINT = (
    '{"name":"短英文slug(小写连字符)","title":"标题","description":"一句话描述",'
    '"keywords":["用于相关性判定的关键词",...],"venues":["目标期刊/会议",...],'
    '"seed_queries":["具体的检索式",...],"sections":["报告章节标题",...]}'
)

_QUERY_SYSTEM = (
    "你是研究主题解析器。把用户的一段研究需求解析成结构化的 topic 配置，"
    "用于驱动多源检索与报告撰写。关键词要能区分同名歧义，检索式要具体可搜。"
)


def _fallback_keywords(text: str) -> list[str]:
    toks = [t for t in re.split(r"[^0-9a-z一-鿿]+", (text or "").lower()) if len(t) >= 2]
    out: list[str] = []
    for t in toks:
        if t in _GENERIC or t in out:
            continue
        # A long run of CJK is a phrase, not a discriminating term — drop it.
        if re.fullmatch(r"[一-鿿]+", t) and len(t) > 4:
            continue
        out.append(t)
    return out[:8]


def topic_from_dict(data: dict[str, Any]) -> Topic:
    """Build a ``Topic`` from a plain dict (e.g. a parsed request or LLM JSON)."""
    text = str(data.get("title") or data.get("query") or data.get("name") or "topic")
    name = str(data.get("name") or "").strip() or slugify(text) or "topic"
    return Topic(
        name=name,
        title=str(data.get("title") or name),
        description=str(data.get("description") or ""),
        keywords=[str(k).strip() for k in (data.get("keywords") or []) if str(k).strip()],
        venues=[str(v).strip() for v in (data.get("venues") or []) if str(v).strip()],
        seed_queries=[str(q).strip() for q in (data.get("seed_queries") or []) if str(q).strip()],
        sections=[str(s).strip() for s in (data.get("sections") or []) if str(s).strip()],
        seed_resources=dict(data.get("seed_resources") or {}),
        raw=dict(data),
    )


def topic_from_query(text: str, *, llm: Any = None, language: str = "bilingual") -> Topic:
    """Parse a free-text research request into a ``Topic``.

    Uses ``llm`` (any object exposing ``.json(messages, ...)``) to turn the text
    into structured fields; falls back to a deterministic derivation of
    name/title/keywords/seed_queries when no model is available or it fails, so
    a request always yields a runnable topic.
    """
    text = (text or "").strip()
    if llm is not None and text:
        try:
            data = llm.json(
                [
                    {"role": "system", "content": _QUERY_SYSTEM},
                    {
                        "role": "user",
                        "content": f"研究需求：{text}\n\n只输出严格 JSON：{_SCHEMA_HINT}\n输出语言：{language}",
                    },
                ],
                tier="fast",
                temperature=0.2,
            )
            if isinstance(data, dict) and (data.get("title") or data.get("seed_queries")):
                fb = topic_from_dict({"title": text, "seed_queries": [text]})
                data.setdefault("name", fb.name)
                data.setdefault("title", fb.title)
                if not data.get("keywords"):
                    data["keywords"] = fb.keywords
                if not data.get("seed_queries"):
                    data["seed_queries"] = fb.seed_queries
                return topic_from_dict(data)
        except Exception as exc:  # noqa: BLE001 - fall back rather than fail the request
            log.warning("topic_from_query LLM parse failed: %s", exc)

    name = slugify(text) if text else "topic"
    return Topic(
        name=name,
        title=text or name,
        description="",
        keywords=_fallback_keywords(text),
        seed_queries=[text] if text else [],
        raw={"query": text},
    )
