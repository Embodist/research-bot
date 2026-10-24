# 研究体系的维护与跟进

> 面向"长期跑、别跑偏"的操作手册：把 `research-bot` 的三层模式（调研 / 初始 / 增量）与
> [`intelligence_governance_final_report.md`](intelligence_governance_final_report.md) 的蓝图对应起来，
> 给出**日 / 周 / 季**节奏、知识库卫生、质量监控与扩展流程。
>
> 相关：[`knowledge-base.md`](knowledge-base.md)（KB + 增量摘要 + feed）、
> [`knowledge-framework.md`](knowledge-framework.md)（两种骨架）、[`github-actions.md`](github-actions.md)（CI）。

---

## 0. 一句话职责划分

| 层 | 模式 | 频率 | 谁触发 | 产出 |
| --- | --- | --- | --- | --- |
| **调研** | `research --topic` | 按需（周/月） | 手动 | 某 topic 的深调研报告 |
| **初始** | `knowledge --query` | 每个新领域一次 | 手动 | 七维知识地图（可推敲、可评估） |
| **增量** | `watch --query` | 每日（CI 自动） | cron | 增量摘要（新作 + 趋势）+ Atom feed |

> 原则：**蓝图与框架属于"初始"，只建一次；每日流水线只做"增量"。**
> 不要让每日 pipeline 去重做调研或初始——那是花钱重复劳动。

## 1. 日：只看增量（自动）

- CI `Daily Watch` 每天 22:00 UTC 对收敛后的前沿逐条 `watch`，只发 **🆕新作 + 📈Trending**。
- 订阅：`report/feed/<topic>.xml` 是标准 Atom，可加进任意阅读器；
  `report/feed/<topic>.jsonl` 是机器可读历史。
- **无新增且无趋势的当天不发邮件、不写 feed**——这是特性，不是故障。

**每天 2 分钟复核**（收到邮件时）：
1. 新作里有没有"仅演示、未复现"却高热度的？（关注 `关注度/推荐度` 两列）
2. Trending 里连续多期出现的条目，是否该升级为"必读/跟进对象"？
3. 是否有明显域漂移（标题与主题无关）→ 收紧该领域的 `WATCH_QUERIES` 词。

## 2. 周：趋势复盘与 KB 卫生（10–15 分钟）

```bash
.venv/bin/rb kb stats            # topics / reports / items / pushes 规模
.venv/bin/rb kb topics           # 领域树，找空转/重复的 topic
.venv/bin/rb kb recent --limit 20
.venv/bin/rb kb new --topic <slug>   # 只出现过一次、可能值得推送的条目
```

- **看趋势**：连续多期重复出现的条目 = 该领域真正的热点；把它们记入你的"跟进清单"。
- **剪枝**：长期零新增、且不属于核心的领域，从 `WATCH_QUERIES` 移除（每天少一条就少一次 LLM 花销）。
- **去重体检**：若某领域每期 `known` 比例长期 > 90%，说明该领域变化慢 → 降频或移出每日 watch。
- **升级**：把稳定高热条目沉淀进话题清单/种子资源（`topics/*.yaml`），让后续 `research/knowledge` 直接覆盖。

## 3. 季：深度调研与初始刷新（半天）

- 对"周复盘里反复出现"的领域，手动跑一次 `research --topic` 或 `knowledge --query`，形成阶段性强报告；
- 对领域结构发生变化的，重跑 `knowledge`（初始）更新地图；
- 复核蓝图的**研究方向 A–J** 与 **H1–H9 假设**：哪些有了新证据、哪些被推翻（见蓝图 §32–33）。

```bash
# 手动（远程，CLAUDE.md 要求不要本地跑）
gh workflow run daily-research.yml -R Embodist/research-bot \
  -f mode=knowledge -f query="<领域>" -f depth=standard -f send_email=true
gh workflow run daily-research.yml -R Embodist/research-bot \
  -f mode=research  -f topic=<topic> -f depth=deep -f send_email=true
```

## 4. 与情报治理蓝图的对应

| 蓝图部分 | 处理方式 |
| --- | --- |
| World / Value / Decision / Calibration / Evaluation / Governance 框架 | **一次 `knowledge`** 建图（初始），不每日跟踪 |
| 各层的前沿（世界模型、价值对齐、Agent 评测、AI 治理…） | **每日 `watch`**（已在 `WATCH_QUERIES`） |
| 研究方向 A–J | 季度 `research` / `knowledge` 深挖 |
| H1–H9 假设、Golden Cases、四大数据库 | **自建实验/数据**，不进 bot；用 feed 的文献增量驱动假设验证 |

> 蓝图的"数据资产"（Golden Cases、失败库、专家轨迹）是你真正的护城河，bot 只负责**供给文献与趋势增量**，
> 不替代实验。

## 5. 质量监控（每周扫一眼 CI）

- **CI 绿不绿**：`gh run list --workflow daily-research.yml --limit 7`
- **邮件是否真发出**：日志应有 `email[...] (增量): sent=True`；`sent=False error=...` 要查 SMTP/`--email`。
- **覆盖度**：知识/增量报告会打印 `coverage score` 与 `gaps`；长期低分的领域要补检索或换词。
- **引擎健康**：`rb doctor` 里被墙引擎属预期；若学术引擎大面积 FAIL，报告的权威性会下降。
- **域漂移**：见 HANDOVER §10.1 的统一相关性门控；仍漂移多为查询词过泛。

## 6. 扩展 / 退役一个领域

1. 在 workflow 的 `WATCH_QUERIES` 默认值里增删一条（逗号分隔，**条目内不要用 ASCII 逗号**，用 `、`）；
2. 或用同名仓库 Variable 覆盖（临时试验用）；
3. 新增领域**首次 watch = 基线**（全 "new"），之后才是增量；
4. 退役时直接从清单删除即可，KB 里历史保留、不影响其他领域。

## 7. 数据与隐私

- KB 只存**收件人数**，不存地址；`report/push-log.jsonl` 含地址但 gitignore、仅作 artifact。
- feed 文件随报告入库，**不含任何收件人信息**。
- `.env*` / `config.yaml` / `.claude/` 永不入库。
