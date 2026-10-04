"""Cross-domain knowledge framework.

A fixed, universal set of *facets* + a deterministic coverage evaluator that
turns any domain/question into a rigorous, closed-loop, evaluable knowledge map.

The framework is deliberately domain-agnostic: the same seven facets apply to a
C++ idiom (RAII), a mathematics theorem (the mean value theorem) or an embodied
AI paradigm (real2sim/sim2real world models). Because the structure is fixed,
maps are comparable across domains and can evolve as the field does.

Rigor invariants (also encoded in ``skills/knowledge-framework/SKILL.md`` and
checked by :func:`evaluate_coverage`):

1. **Traceable** — every claim carries a citation ``[n]``; unknowns are written
   ``> 待核实`` rather than invented.
2. **Bounded** — every mechanism must state where it applies and where it does
   not (or give a counterexample).
3. **Closed-loop** — every "solved X" must be paired with the cost / new problem
   it introduced.
4. **Evaluable** — claims should attach to a metric, benchmark or proof standard
   wherever one exists.
5. **Explainable & learnable** — fixed facets + a prerequisite chain make the
   domain teachable.
6. **Evolvable** — a stable schema lets later knowledge slot in without rework.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from .topics import Topic, topic_from_query
from .util import slugify, truncate

KNOWLEDGE_SKILL = "knowledge-framework"


@dataclass(frozen=True)
class Facet:
    id: str
    zh: str
    en: str
    hint: str  # what the facet must contain
    probe: str  # a search probe appended to the domain query


FACETS: list[Facet] = [
    Facet("positioning", "定位与背景", "Positioning", "定义、边界（不是什么）、它为何存在、依赖的前置知识体系", "背景 定义 前置知识"),
    Facet("problem", "问题域", "Problem Space", "它要解决的核心问题、问题的形式化、约束与不变量", "要解决的问题 形式化 约束"),
    Facet("evolution", "历史与演进", "Evolution", "时间线/代际；每一代解决了什么、又新引入了什么", "历史 演进 各代方案 缺陷"),
    Facet("mechanism", "核心机制", "Mechanism", "概念/原理/定理/范式、关键权衡、作用域（何时适用/何时不适用）", "原理 机制 适用边界 反例"),
    Facet("evaluation", "证据与评估", "Evaluation", "指标/基准/可复现性、可解释性、反例与失败模式、争议", "评估指标 基准 失败模式 争议"),
    Facet("practice", "实践与生态", "Practice", "经典工作与人物、工具与库、落地案例、学习路径（前置顺序）", "经典工作 工具库 案例 学习路径"),
    Facet("meta", "关联与元层", "Meta", "相邻领域与边界、该领域知识如何被验证/推翻、开放问题与演进方向", "相关领域 开放问题 发展方向"),
]

FACET_IDS: list[str] = [f.id for f in FACETS]

# Keywords that signal a facet has stated its boundary / cost (rigor invariant 2 & 3).
_BOUNDARY_MARKERS = (
    "边界", "不适用", "反例", "局限", "代价", "权衡", "新问题", "何时不", "仅当",
    "counterexample", "limitation", "trade-off", "tradeoff", "does not apply", "caveat",
)

_CLAIM_RE = re.compile(r"^(\d+\.\s|[-*]\s)")
_CITE_RE = re.compile(r"\[\d+\]")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def knowledge_sections(language: str = "bilingual") -> list[str]:
    """The report structure for a knowledge map (the seven facets, numbered)."""
    return [f"{i}. {f.zh}（{f.en}）" for i, f in enumerate(FACETS, 1)]


def build_knowledge_topic(query: str, *, language: str = "bilingual") -> Topic:
    """Turn a free-text domain/question into a knowledge-map ``Topic``.

    Reuses the deterministic topic builder for name/keywords, then overrides the
    report structure with the seven facets and seeds one probe query per facet so
    the planner is steered to populate every facet.
    """
    base = topic_from_query(query, llm=None, language=language)
    topic = Topic(
        name=base.name or (slugify(query) or "topic"),
        title=base.title,
        description=f"{base.title} — 跨领域知识地图（7 facet）",
        keywords=base.keywords,
        venues=[],
        seed_queries=list(dict.fromkeys([query, *base.seed_queries] + [f"{query} {f.probe}" for f in FACETS])),
        sections=knowledge_sections(language),
        seed_resources={},
        raw={"query": query, "mode": "knowledge"},
    )
    return topic


# ---------------------------------------------------------------------------
# coverage evaluation (deterministic — no LLM)
# ---------------------------------------------------------------------------
@dataclass
class FacetCoverage:
    facet: str
    title: str
    populated: bool
    claim_count: int = 0
    sourced: int = 0
    has_boundary: bool = False
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "facet": self.facet,
            "title": self.title,
            "populated": self.populated,
            "claim_count": self.claim_count,
            "sourced": self.sourced,
            "has_boundary": self.has_boundary,
            "notes": self.notes,
        }


@dataclass
class CoverageReport:
    facets: list[FacetCoverage]
    sourced_ratio: float
    unsourced: list[str]
    gaps: list[str]
    score: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "score": self.score,
            "sourced_ratio": round(self.sourced_ratio, 3),
            "facets": [f.to_dict() for f in self.facets],
            "unsourced": self.unsourced[:20],
            "gaps": self.gaps,
        }


def _split_sections(md: str) -> dict[str, str]:
    """Map heading text -> body text for every heading in the report."""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in (md or "").splitlines():
        m = _HEADING_RE.match(line.strip())
        if m:
            current = m.group(2).strip()
            sections.setdefault(current, [])
        elif current is not None:
            sections[current].append(line)
    return {k: "\n".join(v) for k, v in sections.items()}


def _claim_stats(text: str) -> tuple[int, int, list[str]]:
    """Return (claim_lines, sourced_lines, unsourced_samples) for a block."""
    total = sourced = 0
    unsourced: list[str] = []
    for line in (text or "").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("> 待核实") or s.startswith("|--"):
            continue
        is_claim = bool(_CLAIM_RE.match(s)) or (s.startswith("|") and s.count("|") >= 3)
        if not is_claim:
            continue
        total += 1
        if _CITE_RE.search(s):
            sourced += 1
        else:
            unsourced.append(truncate(s, 100))
    return total, sourced, unsourced


def evaluate_coverage(result: Any) -> CoverageReport:
    """Deterministically score how well a knowledge report covers the facets.

    Works off ``result.report_md``: it locates each facet's section, counts
    sourced vs unsourced claim lines, checks for boundary/cost language, and
    emits the gaps. It *reports* gaps rather than failing, so a thin knowledge
    map is visible instead of silently accepted.
    """
    md = getattr(result, "report_md", "") or ""
    sections = _split_sections(md)

    facets: list[FacetCoverage] = []
    gaps: list[str] = []
    for f in FACETS:
        # section heading contains the zh facet title (see knowledge_sections)
        body = next((b for h, b in sections.items() if f.zh in h), "")
        total, sourced, _ = _claim_stats(body)
        populated = bool(body.strip()) and (total > 0 or len(body.strip()) >= 40)
        has_boundary = any(m in body for m in _BOUNDARY_MARKERS)
        notes: list[str] = []
        if not populated:
            notes.append("未覆盖或过薄")
            gaps.append(f"「{f.zh}」未覆盖")
        elif total and sourced == 0:
            notes.append("有内容但无引用")
            gaps.append(f"「{f.zh}」缺少 [n] 引用")
        if populated and not has_boundary:
            notes.append("未声明边界/代价")
        facets.append(
            FacetCoverage(f.id, f.zh, populated, claim_count=total, sourced=sourced, has_boundary=has_boundary, notes=notes)
        )

    total_claims, sourced_claims, unsourced = _claim_stats(md)
    sourced_ratio = (sourced_claims / total_claims) if total_claims else 0.0
    populated_frac = sum(1 for fc in facets if fc.populated) / len(FACETS)
    boundary_frac = sum(1 for fc in facets if fc.has_boundary) / len(FACETS)
    score = round(100 * (0.55 * populated_frac + 0.30 * sourced_ratio + 0.15 * boundary_frac), 1)
    if sourced_ratio < 0.5 and total_claims:
        gaps.append(f"整体引用率偏低（{sourced_ratio:.0%}）")
    return CoverageReport(facets=facets, sourced_ratio=sourced_ratio, unsourced=unsourced, gaps=gaps, score=score)
