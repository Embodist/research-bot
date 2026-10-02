"""Skill loader — DeerFlow-compatible ``SKILL.md`` packages.

DeerFlow stores agent skills as directories containing a ``SKILL.md`` with YAML
front-matter (``name``, ``description``) followed by methodology in Markdown.
We read the same format so that:

* our own ``skills/`` directory and
* the upstream submodule's ``deer-flow/skills/public/*``

can be loaded uniformly and injected into the lead prompt. See
``deer-flow/AGENTS.md`` and ``skills/public/deep-research/SKILL.md`` upstream.
"""

from __future__ import annotations

import logging
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

log = logging.getLogger(__name__)

_FRONTMATTER_RE = None


@dataclass
class Skill:
    name: str
    description: str
    body: str
    path: Path
    source: str = "local"  # local | deer-flow
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_prompt(self, max_chars: int = 8000) -> str:
        body = self.body.strip()
        if len(body) > max_chars:
            body = body[:max_chars] + "\n… (skill truncated)"
        return f"### Skill: {self.name}\n{self.description.strip()}\n\n{body}"


def _split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw_meta = text[3:end]
    body = text[end + 4 :]
    try:
        meta = yaml.safe_load(raw_meta) or {}
    except yaml.YAMLError as exc:  # noqa: BLE001
        log.warning("bad YAML front-matter: %s", exc)
        meta = {}
    if not isinstance(meta, dict):
        meta = {}
    return meta, body.lstrip("\n")


def parse_skill_file(path: Path, source: str = "local") -> Skill | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        log.warning("cannot read skill %s: %s", path, exc)
        return None
    meta, body = _split_frontmatter(text)
    name = str(meta.get("name") or path.parent.name)
    description = str(meta.get("description") or "")
    return Skill(name=name, description=description, body=body, path=path, source=source, metadata=meta)


def _scan_root(root: Path, source: str) -> list[Skill]:
    skills: list[Skill] = []
    if not root.is_dir():
        return skills
    for skill_md in sorted(root.glob("*/SKILL.md")):
        skill = parse_skill_file(skill_md, source=source)
        if skill:
            skills.append(skill)
    return skills


def load_skills(home: Path, *, include_deerflow: bool = True) -> dict[str, Skill]:
    """Load local skills, then fill gaps from the vendored deer-flow submodule."""
    found: dict[str, Skill] = {}
    for skill in _scan_root(home / "skills", "local"):
        found[skill.name] = skill
    if include_deerflow:
        upstream = home / "deer-flow" / "skills" / "public"
        for skill in _scan_root(upstream, "deer-flow"):
            found.setdefault(skill.name, skill)
    return found


def select_skills(skills: dict[str, Skill], names: Iterable[str]) -> list[Skill]:
    out: list[Skill] = []
    for name in names:
        skill = skills.get(name)
        if skill is None:
            log.warning("requested skill %r not found", name)
            continue
        out.append(skill)
    return out
