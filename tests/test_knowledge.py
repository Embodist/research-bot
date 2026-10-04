from __future__ import annotations

import pytest

from research_bot.engine import ResearchResult
from research_bot.knowledge import (
    FACETS,
    FRAMES,
    WATCH_FRAME,
    build_knowledge_topic,
    evaluate_coverage,
    get_frame,
    knowledge_sections,
)

_FULL_REPORT = """# Demo Domain

## 摘要
- 一句话压缩：……

1. 定位与背景（Positioning）
- 它是什么，以及它不是什么 [1]
- 依赖的前置知识体系 [2]

2. 问题域（Problem Space）
- 核心问题与约束 [1]

3. 历史与演进（Evolution）
- 第一代解决了 X；代价是引入了 Y [2]

4. 核心机制（Mechanism）
- 核心原理 [1]
- 适用边界：仅当条件 Z 成立时有效，反例：……；常见失败案例见下 [2]

5. 证据与评估（Evaluation）
- 基准指标与失败模式 [2]

6. 实践与生态（Practice）
- 学习路径：先学前置知识，再掌握核心能力地图 [1]

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

_WATCH_REPORT = """# Demo (2026-10)

1. 进展与热点（Progress & Hotspots）
- 2026-09 发布 X，相对上次的增量：…… [1]

2. 工业界与产品（Industry & Product）
- 厂商 Y 开源权重并真机部署 [2]

3. 蓝海与缺口（Blue Ocean & Gaps）
- 尚无工作的空白方向 Z [1]

4. 瓶颈与拐点（Bottleneck & Inflection）
- 数据瓶颈尚未突破，拐点存在不确定性 [2]

5. 社会·政策·国际（Society, Policy & Geopolitics）
- 监管草案带来的风险 [1]

6. 资本与生态（Capital & Ecosystem）
- 融资与并购、人才流动 [2]

7. 信号与预测（Signals & Forecast）
- 预测未来 12 个月方向；不确定性高 [1]

## 参考来源
- [1] A — https://a
- [2] B — https://b
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


def test_frames_registry_and_defaults():
    assert set(FRAMES) == {"knowledge", "watch"}
    assert get_frame(None).id == "knowledge"
    assert get_frame("watch") is WATCH_FRAME
    assert [f.id for f in FACETS] == get_frame("knowledge").facet_ids
    with pytest.raises(KeyError):
        get_frame("nope")


def test_knowledge_sections_per_frame():
    assert len(knowledge_sections()) == len(FACETS) == 7
    assert "定位与背景" in knowledge_sections()[0]
    watch = knowledge_sections(frame="watch")
    assert len(watch) == 7
    assert "进展与热点" in watch[0]
    assert "信号与预测" in watch[-1]


def test_build_knowledge_topic_knowledge_frame():
    t = build_knowledge_topic("C++ RAII 的核心思想")
    assert t.sections == knowledge_sections()
    assert t.seed_queries[0] == "C++ RAII 的核心思想"
    assert len(t.seed_queries) >= 1 + len(FACETS)
    assert t.raw["mode"] == "knowledge"


def test_build_knowledge_topic_watch_frame():
    t = build_knowledge_topic("具身智能世界模型", frame="watch")
    assert t.sections == knowledge_sections(frame="watch")
    assert t.raw["mode"] == "watch"
    assert any("最新进展" in q for q in t.seed_queries)
    assert any("监管" in q or "政策" in q for q in t.seed_queries)


def test_evaluate_coverage_full_report_scores_high():
    report = evaluate_coverage(_result(_FULL_REPORT))
    assert report.frame == "knowledge"
    assert report.score >= 80
    assert all(fc.populated for fc in report.facets)
    assert report.sourced_ratio > 0
    assert not report.elements_missing
    assert not [g for g in report.gaps if "未覆盖" in g]


def test_evaluate_coverage_thin_report_flags_gaps():
    report = evaluate_coverage(_result(_THIN_REPORT))
    assert report.score < 80
    assert any("未覆盖" in g for g in report.gaps)
    assert any("引用" in g for g in report.gaps)
    assert report.elements_missing  # missing learning-path elements


def test_evaluate_coverage_watch_frame():
    report = evaluate_coverage(_result(_WATCH_REPORT), frame="watch")
    assert report.frame == "watch"
    assert report.score >= 80
    assert not report.elements_missing
    assert all(fc.populated for fc in report.facets)
    # a knowledge report scored against the watch frame will not match its facets
    mismatched = evaluate_coverage(_result(_FULL_REPORT), frame="watch")
    assert any("未覆盖" in g for g in mismatched.gaps)
