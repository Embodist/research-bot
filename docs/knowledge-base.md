# 知识库（SQLite topic knowledge base）

> 面向"持续演进"的知识管理：把每次 run 的**报告、条目、推送**落进一个 SQLite 库，
> 支撑 **增量追踪**（watch 只报"新/变"）与 **推送去重**（同一知识不重复触达），
> 并允许用**多级 topic** 组织领域。
>
> 实现见 [`src/research_bot/store.py`](../src/research_bot/store.py)；相关：
> [`docs/knowledge-framework.md`](knowledge-framework.md)（七维骨架）、[`docs/github-actions.md`](github-actions.md)（CI）。

---

## 0. 为什么

没有知识库时：

- `watch` 是**无记忆**的——每次都是全新快照，没有"上次基线"，谈不上真正的**增量**
  （现每日工作流已调度 `watch`，见 [`docs/github-actions.md`](github-actions.md)）；
- 高质量来源会在多天/多次推送里**重复触达**；
- 知识没有**多级结构**，无法"AI 音乐 ⊂ 音乐产业"这样归类。

知识库解决这三点。

## 1. 数据模型

| 表 | 作用 |
| --- | --- |
| `topics` | 多级领域树：`parent_id` 自引用；`name` 唯一；记 `title` / `mode` |
| `reports` | 每次 run 的报告：`report_key`（如 `2026-10-04-ai-music`）、mode/depth、路径、coverage、来源数 |
| `items` | 去重后的知识条目：`norm_key`（标题/URL 归一）为主键；`payload_hash` 判"是否变"；`seen_count` / `first_seen_report` / `last_seen_report` |
| `pushes` | 推送台账：`dedup_key`、channel、**收件人数（不存地址）**、subject、时间 |

条目来自 run 的抽取结果：`findings`、`key_papers` / `key_projects` / `key_datasets`、`open_problems`
（见 `store.items_from_result`）。

## 2. 去重键与增量算法

- `norm_key(title, url)`：对标题（或退化到 URL）做 slug 归一，得到稳定键。
- `payload_hash(payload)`：对条目载荷做**规范化 JSON** 的 sha1 → 判"内容是否变"。
- `record_items(topic_id, report_id, items)` 逐个判定：
  - 库里没有该 `norm_key` → **new**（新增，`seen_count=1`）；
  - 有但 `payload_hash` 不同 → **updated**（内容变化，计数 +1）；
  - 有且哈希相同 → **known**（重复，计数 +1）。
- 返回 `Increment(new, updated, known)`；`Increment.dedup_key()` 由本次 new 的键集合派生，
  用于 `should_push` / `record_push` 判断"这批新知识是否已推送过"。

> 注意：`findings` 是 LLM 生成的自由文本，跨天措辞会漂移，去重效果有限；
> **稳定去重主要落在带 URL/标题的 `key_*` 条目**上。

## 3. 命令行

```bash
.venv/bin/rb kb init                 # 建库并打印统计
.venv/bin/rb kb stats                # 统计（topics/reports/items/pushes）
.venv/bin/rb kb topics               # 多级 topic 树
.venv/bin/rb kb recent --limit 20    # 最近报告（含 coverage）
.venv/bin/rb kb new --topic ai-music # 只出现过一次、可能值得推送的条目
```

## 4. 与 run 集成

- `rb run --kb ...`：run 结束后写入库，并在 stderr 打印增量
  `kb[<topic>]: +N new, ~M updated, K known`。
- 也可在 `config.yaml` 里置 `kb.enabled: true` 让所有 run 默认入库。
- **watch 邮件门控**：当 `mode=watch` 且本次 `changed==0`（既无 new 也无 updated）时，
  默认**跳过邮件**（`kb.skip_email_when_unchanged: true`），避免同一知识重复触达；
  需要"心跳邮件"可把它设为 `false`。

## 5. CI 持久化（不提交二进制）

库是二进制、且 `pushes` 含**收件人数**，故 **`.gitignore` 排除 `report/knowledge.db`**
（`*.db` / `-wal` / `-shm`）。每日工作流用 `actions/cache` 跨天持久化：restore 最新的 `kb-` 前缀缓存，
每次 run 存一份新的；daily 的 `git add report/` 因 gitignore 不会误带 DB。

## 6. 隐私

`pushes` **只记收件人数量，不记地址**——因此即便库被误传，也不泄露 PII。
投递明细（含地址）仍在 `report/push-log.jsonl`，且该文件不入库、仅作 CI artifact。
