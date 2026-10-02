"""Topic definitions — the standing research beats this bot tracks daily.

Each topic lives in ``topics/<name>.yaml`` and combines: seed queries, target
venues, recurring keywords and a curated seed catalogue (classic papers,
projects, datasets). The planner uses it to bias decomposition; the synthesiser
uses it as the required report structure; the seed catalogue guarantees a useful
report even if every network source is unavailable.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

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
