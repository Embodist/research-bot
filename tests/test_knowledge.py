from __future__ import annotations

from research_bot.engine import ResearchResult
from research_bot.knowledge import (
    FACETS,
    build_knowledge_topic,
    evaluate_coverage,
    knowledge_sections,
)

_FULL_REPORT = """# Demo Domain

1. 定位与背景（Positioning）
- 它是什么，以及它不是什么 [1]
- 依赖的前置知识体系 [2]

2. 问题域（Problem Space）
- 核心问题与约束 [1]

3. 历史与演进（Evolution）
- 第一代解决了 X；代价是引入了 Y [2]

4. 核心机制（Mechanism）
- 核心原理 [1]
- 适用边界：仅当条件 Z 成立时有效，反例：……

5. 证据与评估（Evaluation）
- 基准指标 [2]

6. 实践与生态（Practice）
- 经典工具与学习路径 [1]

7. 关联与元层（Meta）
- 与相邻领域的边界与开放问题 [2]

## 参考来源
- [1] A — https://a
- [2] B — https://b
"""

_THIN_REPORT = """# Demo Domain

1. 定位与背景（Positioning）
- 一句没有引用的话

2. 问题域（Problem Space）
- 也是没有引用
"""


def _result(md: str) -> ResearchResult:
    return ResearchResult(
        topic="demo",
        title="Demo",
        query="demo",
        depth="quick",
        language="bilingual",
        started_at="2026-01-01T00:00:00Z",
        report_md=md,
    )


def test_knowledge_sections_has_seven_facets():
    sections = knowledge_sections()
    assert len(sections) == len(FACETS) == 7
    assert "定位与背景" in sections[0]
    assert "关联与元层" in sections[-1]


def test_build_knowledge_topic_uses_facets_and_probes():
    t = build_knowledge_topic("C++ RAII 的核心思想")
    assert t.sections == knowledge_sections()
    assert t.seed_queries[0] == "C++ RAII 的核心思想"
    # one probe per facet, in addition to the base query
    assert len(t.seed_queries) >= 1 + len(FACETS)
    assert t.raw.get("mode") == "knowledge"


def test_evaluate_coverage_full_report_scores_high():
    report = evaluate_coverage(_result(_FULL_REPORT))
    assert report.score >= 80
    assert all(fc.populated for fc in report.facets)
    assert report.sourced_ratio > 0
    assert not [g for g in report.gaps if "未覆盖" in g]


def test_evaluate_coverage_thin_report_flags_gaps():
    report = evaluate_coverage(_result(_THIN_REPORT))
    assert report.score < 80
    # empty facets (3..7) are reported as gaps, not silently dropped
    assert any("未覆盖" in g for g in report.gaps)
    # and the populated-but-unsourced facets are flagged
    assert any("引用" in g for g in report.gaps)
