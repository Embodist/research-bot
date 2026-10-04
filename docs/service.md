# HTTP service (`rb serve`)

> 把 `research-bot` 变成**即用即起**的 HTTP 服务：外部调用方通过 HTTP 传一个 `topic` 或一段自由文本
> `query`（可带 config 覆盖），服务把它解析成 research config、在后台异步跑 deep-research，并轮询取回报告。
> **零新增依赖**——服务基于 Python 标准库 `http.server` 实现，与项目"只有 `httpx` + `PyYAML`"的取向一致。

相关文档：[`deep-research.md`](deep-research.md)（引擎内部）、[`knowledge-framework.md`](knowledge-framework.md)
（跨领域知识体系）、[`HANDOVER.md`](HANDOVER.md)（运行/交接）。

---

## 1. 启动

```bash
# 本地
rb serve --host 127.0.0.1 --port 8080 --workers 2
make serve HOST=0.0.0.0 PORT=8080 WORKERS=2          # 等价

# 容器（即用即起；见 docker-compose.yml）
cp .env.example .env                                 # 填 LLM_API_KEY、可选 token
docker compose up --build                            # curl localhost:8080/healthz
```

| flag | 默认 | 说明 |
| --- | --- | --- |
| `--host` | `127.0.0.1` | 绑定地址。对外暴露用 `0.0.0.0`（务必配 token 或反代）。 |
| `--port` | `8080` | 绑定端口。 |
| `--workers` | `2` | 并发 worker 数。**同时最多 `workers` 个研究任务在跑**，其余排队——这是 LLM 花费的上界。 |

服务只监听、不自动重载；`SIGINT`/`SIGTERM` 触发**优雅关闭**（停止接受新请求，等在跑的任务收尾）。

## 2. 鉴权（可选）

| 环境变量 | 行为 |
| --- | --- |
| `RESEARCH_BOT_API_TOKEN` 已设置 | 除 `GET /healthz` 外，所有端点都要求 `Authorization: Bearer <token>`（常量时间比较）。 |
| 未设置 | 服务**开放**（无鉴权），启动时打印警告。仅限可信网络/反代之后。 |

```bash
curl -s localhost:8080/topics -H "Authorization: Bearer $RESEARCH_BOT_API_TOKEN"
```

> 这是**开发级**服务（标准库 server，非公网硬化）。生产请在反向代理（TLS、限流）之后运行，并设置 token。

## 3. API

### `GET /healthz` — 存活 + 队列深度（始终开放）

```json
{"ok": true, "version": "0.1.0", "total": 3, "queued": 1, "running": 1, "done": 1, "failed": 0}
```

### `GET /topics` — 内置 topic 列表

返回 `[{name, title, description, keywords, seed_queries, sections, ...}]`。

### `POST /research` — 提交任务（异步）

请求体（JSON 对象）：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `query` | string | **自由文本**研究需求。与 `topic` 至少给一个。 |
| `topic` | string | 已有 topic 名（`GET /topics` 里的 `name`）。命中则直接用；否则当作自由文本解析。 |
| `mode` | `"research"` \| `"knowledge"` \| `"watch"` | 默认 `research`。`knowledge` = 七维知识地图（学习一个领域）；`watch` = 七维增量快照（追踪一个领域的变化）。二者都返回 `coverage` 评估。 |
| `depth` | `quick` \| `standard` \| `deep` | 覆盖 `research.depth`。 |
| `rounds` | int | 覆盖最大补检轮数。 |
| `language` | `zh` \| `en` \| `bilingual` | 覆盖 `research.language`。 |
| `fetch` | bool | `false` 时跳过抓正文（只用语料 snippet）。 |
| `email` | bool | 默认 `false`。`true` 且邮件已配置则任务完成后发信。 |
| `config` | object | **config 覆盖**，支持嵌套或点号键（见下）。 |

响应 `202`：

```json
{"job_id": "8f...e1", "status": "queued"}
```

错误：`400`（body 非法 / `config` 含未知顶层段）、`413`（body > 256 KB）、`422`（既无 `query` 也无 `topic`，
或 `mode` 非法）。

**`config` 覆盖**只接受内置 `DEFAULTS` 的顶层段（`llm` / `search` / `research` / `report` / `email`），
嵌套或点号写法等价，随后 `deep_merge ← expand_env`，绝不 eval：

```json
{"query": "C++ RAII", "config": {"llm.model": "deepseek-v4-flash", "research": {"depth": "deep"}}}
```

### `GET /research/{id}` — 轮询状态

```json
{
  "job_id": "8f...e1", "status": "done", "topic": "c-raii-的核心思想",
  "progress": ["plan ok", "retrieve ok", "..."],
  "result": { "report_md": "# ...", "references": [...], "depth": "quick", ... },
  "report_url": "/research/8f...e1/report",
  "coverage": { "frame": "knowledge", "score": 88.7, "sourced_ratio": 0.909, "facets": [...], "gaps": [] }
}
```

`status ∈ queued | running | done | failed | cancelled`；失败时带 `error`；未完成时无 `result`。
`coverage` 仅 `knowledge` / `watch` 模式出现，其 `frame` 字段标明实际使用的骨架。

### `GET /research/{id}/report` — Markdown 正文

`200 text/markdown`（即 `result.report_md`）；未完成返回 `409`。

### `DELETE /research/{id}` — 取消

仅能取消 `queued` 的作业（`202`）；已在跑返回 `409`（尽力而为，不中断执行中的任务）。

## 4. 解析：请求 → config / topic

`serve.py` 的 `_prepare()` 把一次请求变成 `(cfg, topic, rounds, email)`：

1. **config**：`overrides`（嵌套或点号键）→ 校验顶层段 → `deep_merge(base_cfg, …)` → `expand_env` → `DotDict`。
   逐请求开关 `depth` / `language` / `fetch` 再覆盖。
2. **topic**：
   - `mode=knowledge|watch` → `build_knowledge_topic(query|topic, frame=mode)`（七维 facet 结构，见下）。
   - 否则若 `topic` 命中 `topics/*.yaml` → 直接用。
   - 否则 `topic_from_query(seed)`：有 LLM 时用 LLM 解析成结构化 topic；无 LLM / 失败则确定性兜底
     （`name=slug`、`keywords=有区分度的词`、`seed_queries=[原文]`）——**请求永远能得到可跑的 topic**。
3. `knowledge` / `watch` 模式自动把对应 skill（`knowledge-framework` / `frontier-watch`）注入 `research.skills`。

## 5. `knowledge` / `watch` 模式：两种固定骨架

两个模式共用**同一套固定骨架机制**，区别在骨架本身与注入的 skill：

- **`mode=knowledge`（方向1：学习）**——从零理解一个领域/概念/定理/范式，七维：
  `定位与背景 · 问题域 · 历史与演进 · 核心机制 · 证据与评估 · 实践与生态 · 关联与元层`。
- **`mode=watch`（方向2：增量）**——追踪一个领域的**变化**，七维：
  `进展与热点 · 工业界与产品 · 蓝海与缺口 · 瓶颈与拐点 · 社会·政策·国际 · 资本与生态 · 信号与预测`。

两者任务完成后都附带**确定性覆盖度评估** `coverage`（不需要 LLM）：

```json
{"frame": "watch", "score": 88.7, "sourced_ratio": 0.909,
 "facets": [{"facet": "progress", "title": "进展与热点", "populated": true,
             "claim_count": 2, "sourced": 2, "has_boundary": true, "notes": []}, ...],
 "gaps": [], "elements_hit": ["增量", "风险"], "elements_missing": ["不确定", "预测"]}
```

`score = 100·(0.45·已覆盖facet比例 + 0.25·引用率 + 0.15·声明边界/代价的比例 + 0.15·elements命中率)`。
`gaps` 列出未覆盖 / 无引用的 facet 与缺失 elements——**暴露缺口而非静默接受**。详见
[`knowledge-framework.md`](knowledge-framework.md)。

## 6. 端到端示例

```bash
# 1) 知识地图（异步）
curl -s -XPOST localhost:8080/research -H 'content-type: application/json' \
  -d '{"query":"C++ RAII 的核心思想与边界","mode":"knowledge","depth":"quick"}'
# -> {"job_id":"...","status":"queued"}

# 2) 轮询
curl -s localhost:8080/research/<job_id> | jq '{status, topic, coverage: .coverage.score}'

# 3) 取报告
curl -s localhost:8080/research/<job_id>/report

# 4) 增量快照（追踪某领域的变化）
curl -s -XPOST localhost:8080/research -H 'content-type: application/json' \
  -d '{"query":"具身智能世界模型","mode":"watch","depth":"quick"}'

# 5) 追踪型研究 + config 覆盖
curl -s -XPOST localhost:8080/research -H 'content-type: application/json' \
  -d '{"topic":"vla","config":{"research":{"depth":"deep"}},"email":true}'
```

CLI 的等价单次调用：`rb run --knowledge --query "中值定理" --depth quick`（打印 coverage 与 gaps），
或 `rb run --watch --query "具身智能世界模型" --depth quick`。

## 7. 边界与已知取舍

- **内存态、非持久**：job 历史在进程内（默认保留最近 200 个已结束作业，超出裁剪）。重启即丢失任务。
  报告本身仍会落盘到 `report/`（与批处理共用归档 + 台账）。
- **有界并发**：`--workers` 是 LLM 花费的硬上界；超出排队。默认 `depth` 建议用 `quick`。
- **取消是尽力而为**：只能取消尚未开始的任务。
- **开发级 server**：标准库 `http.server` 未做公网硬化；请置于反代/可信网络之后。
- **密钥**：token 只走环境变量，不写入日志；`config.yaml` / `.env` / `.claude/` 保持 gitignore。
