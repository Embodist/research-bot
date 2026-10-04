"""Cross-domain knowledge framework — two fixed-skeleton frames.

A *frame* is a fixed, numbered set of **facets** plus the rigour discipline the
report must satisfy. Because the structure is fixed, maps from different domains
(and different frames) are comparable and can evolve as the field does.

Two frames ship today, matching the two ways a domain is attacked:

* ``knowledge`` — *learn a domain from scratch* (方向1: 初学者快速积累). Background,
  problem domain, evolution, mechanism, evidence, practice (learning path,
  capability map), meta (question tree, frontier).
* ``watch`` — *track a domain's change* (方向2: 增量/蓝海/产业/社会). Progress &
  hotspots, industry & product, blue-ocean gaps, bottlenecks & inflections,
  society/policy/geopolitics, capital & ecosystem, signals & forecast.

Rigor invariants (encoded in each frame's skill and checked by
:func:`evaluate_coverage`):

1. **Traceable** — every claim carries a citation ``[n]``; unknowns are written
   ``> 待核实`` rather than invented.
2. **Bounded** — every mechanism must state where it applies and where it does
   not (or give a counterexample); for ``watch``, uncertainty must be marked.
3. **Closed-loop** — every "solved X" is paired with the cost / new problem it
   introduced.
4. **Evaluable** — claims attach to a metric, benchmark or proof standard.
5. **Explainable & learnable** — fixed facets + a prerequisite chain.
6. **Evolvable** — a stable schema lets later knowledge slot in without rework.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from .topics import Topic, topic_from_query
from .util import slugify, truncate

KNOWLEDGE_SKILL = "knowledge-framework"
WATCH_SKILL = "frontier-watch"


@dataclass(frozen=True)
class Facet:
    id: str
    zh: str
    en: str
    hint: str  # what the facet must contain
    probe: str  # a search probe appended to the domain query


@dataclass(frozen=True)
class Frame:
    id: str
    title: str
    facets: tuple[Facet, ...]
    skill: str  # skill name injected for this frame
    markers: tuple[str, ...]  # discipline markers (boundary / cost / uncertainty)
    elements: tuple[str, ...]  # per-frame "must appear" tokens (evaluable)

    @property
    def facet_ids(self) -> list[str]:
        return [f.id for f in self.facets]

    @property
    def facet_titles(self) -> tuple[str, ...]:
        return tuple(f.zh for f in self.facets)


# ---------------------------------------------------------------------------
# Frame 1 — knowledge map (方向1: learn / master a domain)
# ---------------------------------------------------------------------------
_KNOWLEDGE_FACETS: tuple[Facet, ...] = (
    Facet("positioning", "定位与背景", "Positioning", "定义、边界（不是什么）、它为何存在、依赖的前置知识体系", "背景 定义 前置知识"),
    Facet("problem", "问题域", "Problem Space", "它要解决的核心问题、问题的形式化、约束与不变量", "要解决的问题 形式化 约束"),
    Facet("evolution", "历史与演进", "Evolution", "时间线/代际；每一代解决了什么、又新引入了什么", "历史 演进 各代方案 缺陷"),
    Facet("mechanism", "核心机制", "Mechanism", "概念/原理/定理/范式、关键权衡、作用域（何时适用/何时不适用）、失败案例", "原理 机制 适用边界 反例 失败"),
    Facet("evaluation", "证据与评估", "Evaluation", "指标/基准/可复现性、可解释性、反例与失败模式、争议", "评估指标 基准 失败模式 争议"),
    Facet("practice", "实践与生态", "Practice", "经典工作与人物、工具与库、落地案例、学习路径与能力地图（前置顺序）", "经典工作 工具库 学习路径 能力"),
    Facet("meta", "关联与元层", "Meta", "相邻领域与边界、如何被验证/推翻、开放问题、问题树与高杠杆压缩", "相关领域 开放问题 发展方向"),
)

_KNOWLEDGE_MARKERS = (
    "边界", "不适用", "反例", "局限", "代价", "权衡", "新问题", "何时不", "仅当", "失败",
    "counterexample", "limitation", "trade-off", "tradeoff", "does not apply", "caveat",
)

# Elements a good learning map should surface (方向1): a learning path, its
# prerequisites, a capability map, and the failure cases experts remember.
_KNOWLEDGE_ELEMENTS = ("学习路径", "前置", "能力", "失败")

# ---------------------------------------------------------------------------
# Frame 2 — increment watch (方向2: a domain's change / blue ocean / society)
# ---------------------------------------------------------------------------
_WATCH_FACETS: tuple[Facet, ...] = (
    Facet("progress", "进展与热点", "Progress & Hotspots", "论文/课题最新进展、SOTA、被独立验证 vs 仅有演示", "最新进展 论文 SOTA 榜单 突破"),
    Facet("industry", "工业界与产品", "Industry & Product", "厂商产品、开源与权重、真机部署、商业化与量产", "工业界 产品 发布 部署 商业化"),
    Facet("blueocean", "蓝海与缺口", "Blue Ocean & Gaps", "未解问题、无人区、竞争空白、高杠杆机会", "未解问题 空白 机会 蓝海"),
    Facet("bottleneck", "瓶颈与拐点", "Bottleneck & Inflection", "知识/数据/算力/算法/评测/成本/人力 瓶颈；是否临近拐点", "瓶颈 拐点 限制 突破"),
    Facet("society", "社会·政策·国际", "Society, Policy & Geopolitics", "监管、标准、地缘政治、供应链、伦理与劳动影响", "政策 监管 标准 地缘 供应链 伦理"),
    Facet("capital", "资本与生态", "Capital & Ecosystem", "投资、并购、人才流动、社区、公司格局", "融资 投资 并购 人才 生态"),
    Facet("forecast", "信号与预测", "Signals & Forecast", "早期信号、不确定性、未来 6–18 月预判、可验证假设", "趋势 预测 信号 未来 判断"),
)

# For watch the discipline is *recency + honest uncertainty*, not proof boundaries.
_WATCH_MARKERS = (
    "增量", "较上", "上次", "新进展", "首次", "最新", "时间线", "不确定性", "风险",
    "传闻", "未证实", "待证实", "预测", "预判", "拐点", "尚不明确", "存在争议", "假设", "代价",
)

# Elements a good increment report should surface (方向2): that it is *dated*,
# *incremental* vs last snapshot, and honest about uncertainty / risk.
_WATCH_ELEMENTS = ("增量", "不确定", "风险", "预测")


KNOWLEDGE_FRAME = Frame(
    "knowledge", "跨领域知识地图（学习/掌握）", _KNOWLEDGE_FACETS, KNOWLEDGE_SKILL, _KNOWLEDGE_MARKERS, _KNOWLEDGE_ELEMENTS
)
WATCH_FRAME = Frame(
    "watch", "领域增量追踪（变化/蓝海/产业/社会）", _WATCH_FACETS, WATCH_SKILL, _WATCH_MARKERS, _WATCH_ELEMENTS
)

FRAMES: dict[str, Frame] = {"knowledge": KNOWLEDGE_FRAME, "watch": WATCH_FRAME}
DEFAULT_FRAME = "knowledge"

# Back-compat: the default (knowledge) frame's facets, exposed as before.
FACETS: list[Facet] = list(KNOWLEDGE_FRAME.facets)
FACET_IDS: list[str] = KNOWLEDGE_FRAME.facet_ids

_CLAIM_RE = re.compile(r"^(\d+\.\s|[-*]\s)")
_CITE_RE = re.compile(r"\[\d+\]")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_SECTION_TITLE_RE = re.compile(r"^\d+\.\s+\S")


def get_frame(frame: str | Frame | None = None) -> Frame:
    """Normalise a frame id (or a Frame) to a Frame; default = knowledge."""
    if isinstance(frame, Frame):
        return frame
    if not frame:
        return KNOWLEDGE_FRAME
    key = str(frame).lower()
    if key not in FRAMES:
        raise KeyError(f"unknown frame {frame!r} (known: {', '.join(sorted(FRAMES))})")
    return FRAMES[key]


def knowledge_sections(language: str = "bilingual", *, frame: str | Frame | None = None) -> list[str]:
    """The report structure for a frame (its facets, numbered)."""
    return [f"{i}. {f.zh}（{f.en}）" for i, f in enumerate(get_frame(frame).facets, 1)]


def build_knowledge_topic(query: str, *, frame: str | Frame | None = None, language: str = "bilingual") -> Topic:
    """Turn a free-text domain/question into a frame-driven ``Topic``.

    Reuses the deterministic topic builder for name/keywords, then overrides the
    report structure with the frame's facets and seeds one probe query per facet
    so the planner is steered to populate every facet.
    """
    fr = get_frame(frame)
    base = topic_from_query(query, llm=None, language=language)
    topic = Topic(
        name=base.name or (slugify(query) or "topic"),
        title=base.title,
        description=f"{base.title} — {fr.title}（{len(fr.facets)} facet）",
        keywords=base.keywords,
        venues=[],
        seed_queries=list(dict.fromkeys([query, *base.seed_queries] + [f"{query} {f.probe}" for f in fr.facets])),
        sections=knowledge_sections(language, frame=fr),
        seed_resources={},
        raw={"query": query, "mode": fr.id, "frame": fr.id},
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
    frame: str = DEFAULT_FRAME
    elements_hit: list[str] = field(default_factory=list)
    elements_missing: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "frame": self.frame,
            "score": self.score,
            "sourced_ratio": round(self.sourced_ratio, 3),
            "facets": [f.to_dict() for f in self.facets],
            "unsourced": self.unsourced[:20],
            "gaps": self.gaps,
            "elements_hit": self.elements_hit,
            "elements_missing": self.elements_missing,
        }


def _split_sections(md: str, facet_titles: tuple[str, ...]) -> dict[str, str]:
    """Map heading text -> body text, recognising Markdown headings and our
    bare numbered section titles (``1. 定位与背景（Positioning）``)."""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in (md or "").splitlines():
        stripped = line.strip()
        m = _HEADING_RE.match(stripped)
        if m:
            current = m.group(2).strip()
            sections.setdefault(current, [])
            continue
        if _SECTION_TITLE_RE.match(stripped) and any(t in stripped for t in facet_titles):
            current = stripped
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
    return {k: "\n".join(v) for k, v in sections.items()}


def _claim_stats(text: str, facet_titles: tuple[str, ...]) -> tuple[int, int, list[str]]:
    """Return (claim_lines, sourced_lines, unsourced_samples) for a block."""
    total = sourced = 0
    unsourced: list[str] = []
    for line in (text or "").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("> 待核实") or s.startswith("|--"):
            continue
        if _SECTION_TITLE_RE.match(s) and any(t in s for t in facet_titles):
            continue  # a section title, not a claim
        is_claim = bool(_CLAIM_RE.match(s)) or (s.startswith("|") and s.count("|") >= 3)
        if not is_claim:
            continue
        total += 1
        if _CITE_RE.search(s):
            sourced += 1
        else:
            unsourced.append(truncate(s, 100))
    return total, sourced, unsourced


def evaluate_coverage(result: Any, *, frame: str | Frame | None = None) -> CoverageReport:
    """Deterministically score how well a report covers a frame's facets.

    Works off ``result.report_md``: it locates each facet's section, counts
    sourced vs unsourced claim lines, checks for discipline markers, and emits
    the gaps. It *reports* gaps rather than failing, so a thin map is visible
    instead of silently accepted.
    """
    fr = get_frame(frame)
    titles = fr.facet_titles
    md = getattr(result, "report_md", "") or ""
    sections = _split_sections(md, titles)

    facets: list[FacetCoverage] = []
    gaps: list[str] = []
    for f in fr.facets:
        body = next((b for h, b in sections.items() if f.zh in h), "")
        total, sourced, _ = _claim_stats(body, titles)
        populated = bool(body.strip()) and (total > 0 or len(body.strip()) >= 40)
        has_boundary = any(m in body for m in fr.markers)
        notes: list[str] = []
        if not populated:
            notes.append("未覆盖或过薄")
            gaps.append(f"「{f.zh}」未覆盖")
        elif total and sourced == 0:
            notes.append("有内容但无引用")
            gaps.append(f"「{f.zh}」缺少 [n] 引用")
        if populated and not has_boundary:
            notes.append("未声明边界/代价" if fr.id == "knowledge" else "未标注不确定性/风险")
        facets.append(
            FacetCoverage(f.id, f.zh, populated, claim_count=total, sourced=sourced, has_boundary=has_boundary, notes=notes)
        )

    total_claims, sourced_claims, unsourced = _claim_stats(md, titles)
    sourced_ratio = (sourced_claims / total_claims) if total_claims else 0.0
    populated_frac = sum(1 for fc in facets if fc.populated) / len(fr.facets)
    boundary_frac = sum(1 for fc in facets if fc.has_boundary) / len(fr.facets)

    elements_hit = [e for e in fr.elements if e in md]
    elements_missing = [e for e in fr.elements if e not in md]
    elements_frac = len(elements_hit) / len(fr.elements) if fr.elements else 1.0

    score = round(100 * (0.45 * populated_frac + 0.25 * sourced_ratio + 0.15 * boundary_frac + 0.15 * elements_frac), 1)
    if sourced_ratio < 0.5 and total_claims:
        gaps.append(f"整体引用率偏低（{sourced_ratio:.0%}）")
    for e in elements_missing:
        gaps.append(f"缺少关键要素「{e}」")
    return CoverageReport(
        facets=facets,
        sourced_ratio=sourced_ratio,
        unsourced=unsourced,
        gaps=gaps,
        score=score,
        frame=fr.id,
        elements_hit=elements_hit,
        elements_missing=elements_missing,
    )
