# Deep-Research 技术核心与架构

> 本文记录 `research-bot` 的 **deep-research 技术核心**（算法与机制）与**技术架构**（模块、数据流、
> 并发、部署）。面向接手人：读完可据此定位任何一处行为背后的代码。术语、代码、命令保留英文。
>
> 相关文档：[`architecture.md`](architecture.md)（简明总览）、[`HANDOVER.md`](HANDOVER.md)（交接/运行）、
> [`skills-and-sources.md`](skills-and-sources.md)、[`github-actions.md`](github-actions.md)。

---

## 0. 一句话

`research-bot` 是一个 **headless deep-research agent**：把"深度调研"拆成
`规划 → 多源检索 → 排序 → 抓正文 → 抽取分级证据 → 评审补检 → 带引用综合` 的闭环，
**只用 `httpx` + `PyYAML`** 两个运行时依赖实现，因此能在 GitHub Actions / cron / 容器里无 Docker、无数据库地跑，
同时复用 [`bytedance/deer-flow`](../deer-flow) 的 skill 格式与 lead-agent/sub-agent 分工。

设计三条底线（贯穿全局）：
1. **引用可核查**——每个来源有稳定编号 `[n]`，正文引用必须命中该编号，禁止编造 URL/论文。
2. **拒绝编造证据**——证据不足写 `> 待核实`，不臆造数字/榜单。
3. **优雅降级**——LLM 挂了仍出"源码接地"报告；引擎被墙按熔断剔除；页面抓不到退化为仅用 snippet。

---

## 1. 技术核心（算法与机制）

### 1.1 多源检索：并行 fan-out + 加权 RRF 融合

`search/router.py`。9 个引擎注册在 `ENGINE_REGISTRY`，`SearchRouter.search()` 用
`ThreadPoolExecutor`（`max_workers=min(8, N_engines)`）对**一条查询**并行 fan-out，随后调用
`rrf_fuse()` 融合。

**RRF（Reciprocal Rank Fusion）**，`rrf_fuse(pairs, k=60, cap=80)`：每个引擎每个结果按排名贡献
`weight / (k + rank + 1)`，同 URL 累加；最终按总分排序取前 `cap` 条。

关键在 **引擎信任权重** `ENGINE_WEIGHTS`（`router.py:47`）：

| 引擎 | 权重 | 类型 | 理由 |
| --- | --- | --- | --- |
| `arxiv` | 1.5 | 学术 API | 服务端匹配 + 可引用元数据 |
| `openalex` | 1.4 | 学术 API | 摘要/引用/venue |
| `semantic_scholar` | 1.4 | 学术 API | 引用数 |
| `crossref` | 1.2 | 学术 API | DOI/日期 |
| `github` | 1.2 | API | 仓库/star |
| `searxng` | 0.9 | HTML | 自建元搜索 |
| `bing` / `sogou` | 0.6 | HTML | 广召回但同音噪声大 |
| `so360` | 0.5 | HTML | 同上 |
| 未知引擎 | 0.7 | — | `DEFAULT_ENGINE_WEIGHT` |

> 直观：同一排名下，arXiv 的一条要压过 Bing 的一条——因为结构化/学术引擎**服务端匹配**且返回可引用元数据，
> 而 HTML 引擎同名词冲突严重（ROS → *reactive oxygen species*）。

**去重键 `_dedup_key`**：优先 `norm_url(res.url)`（`util.norm_url` 去掉 `utm_*`/`ref`/`fbclid` 等参数、
小写 host、去 `www.`、去尾斜杠）；无 URL 时退化为标题前 120 字符。**字段合并**保留信息量最大的变体
（更长 snippet、非空 url/venue/published/citations/stars），并把重复来源记进 `extra["also_seen_on"]`。
融合后每条带 `extra["rrf_score"]`。

**熔断（circuit breaker）**：`failure_threshold=2`。某引擎在同一 run 内累计失败 2 次即加入 `_disabled`，
本 run 后续查询直接跳过——把被墙引擎的墙钟开销一次掐掉。单引擎异常被 `_run_one` 吞掉，绝不炸整个 run。
若没有任何引擎可用，回退到 `arxiv + openalex`。

### 1.2 相关性门控：distinctive-token gate

`engine._filter_relevant` / `_is_offtopic`（`engine.py:55-67, 364`）。这是**本项目最重要的质量控制机制**，
用于压掉检索域漂移。

- `_content_tokens(text)`：按非字母数字/非汉字切分，取长度 ≥2 的词。
- `_GENERIC_TOKENS`：停用词表（`best/practices/project/survey/model/learning/…`），这类词**不能证明相关性**。
- `_distinctive_tokens(text)`：`_content_tokens − _GENERIC_TOKENS`。
- 判定 `_is_offtopic(res, distinct_query, keywords)`：命中主题关键词（`topic.keywords ∪ {topic.name}`）→ 保留；
  否则要求 `res` 与查询的**有区分度词**重叠 **≥2**，才保留。

```python
def _is_offtopic(res, distinct_query, keywords):
    text = f"{res.title} {res.snippet}".lower()
    if any(kw in text for kw in keywords):
        return False
    return len(_distinctive_tokens(text) & distinct_query) < 2
```

**设计取舍**：门控对**所有引擎**生效（不再只针对 HTML 引擎）——因为 Crossref/OpenAlex 这类
关键词匹配引擎同样会松散命中（`pi0` → π⁰ 介子）。若某子问题被全部滤掉，**故意留空**：把检索缺口暴露出来，
好过用垃圾凑数。

### 1.3 排序：RRF 分数 + 元数据加权的启发式打分

`engine._rank_results`（`engine.py:373`）。在门控后，对每条按下式打分（都基于已融合的 `rrf_score`）：

```
s = rrf_score
if res.engine in sub.prefer:                 s *= 1.6     # 子问题声明的优先源
if res.kind in (paper, project, dataset):    s *= 1.15    # 结构化类型加权
if res.citations:  s += min(citations,500)/500 * 0.2      # 引用
if res.stars:      s += min(stars,5000)/5000 * 0.15       # star
if res.published:  s += 0.1 if 近期 else -0.1              # 时效（recency_days）
```

降序后按标题规范化键去重，取前 `max_keep` 条。

### 1.4 引用注册表：全局稳定编号

`SourceRegistry`（`engine.py:139`）。键 = `norm_url(res.url) or title.lower()`；首次见到的来源分配全局自增
编号 `[n]`，之后同一来源返回同号。**抽取**与**综合**都引用同一编号，所以正文 `[n]` 与文末参考列表严格对齐。
`reference_list()` 输出 `{n,title,url,kind,venue,published,citations,stars}`。

### 1.5 抽取：候选证据块 → 结构化 findings（四轴证据）

`engine.extract`（`engine.py:465`）。先把子问题结果渲染成**候选证据块** `_candidate_block`：

```
[n] (kind; engine; published, venue, citations=…, stars=…) 标题
    URL: …
    Snippet: …（≤400 字）
    Content: …（抓取正文，≤1500 字）
```

再用 **fast tier** LLM（`temperature=0.2`，`json_mode`）抽取，要求输出 findings **3–8 条**、去重、按重要性排序，
每条字段固定：

- `point` 结论、`evidence` 细节、`sources`（引用编号 int 列表）、`type`、`confidence`、`year`；
- **四轴证据**：`heat`（热度：citations/stars/下载/讨论）、`authority`（权威：venue/同行评审/官方文档/标准）、
  `attention`（关注度：高/中/低 + 依据）、`recommendation`（推荐度：★1-5 + 理由）；
- 另出 `key_papers` / `key_projects` / `key_datasets` / `open_problems`。

**证据缺失必须留空/给中性值，禁止编造数字或榜单。** 提示词明确写了这条。

**降级抽取 `_fallback_extraction`**（LLM 不可用）：直接取前 6 条结果，`heat`/`authority` 由
`_heat_text`/`_authority_text` 填，`attention`/`recommendation` 由确定性规则推导：

- `_attention_text`：stars ≥1000 高 / ≥100 中 / 否则低；无 stars 看 citations ≥50 高 / ≥5 中 / 否则低；都没有返回空。
- `_recommendation_text`：基线 3 分（已过门控，值得看）→ 有 venue +1、高热度 +1；**完全无权威也无热度信号 −1**；
  截断到 1–5，渲染成 `★★★★☆（venue=RSS）` 形式。

### 1.6 评审与补检回路（bounded）

`engine.critique` + `run()` 的轮次循环（`engine.py:690-732`）。每轮：并行检索所有子问题 → 逐条抽取 →
若未达 `max_rounds` 则让 **strong tier** critic 评估覆盖度、给缺口 `gaps`、补充查询 `additional_queries`、
补充子问题 `additional_subquestions`。

- 补充查询接到 `subquestions[0].queries`（去重，最多 2 条）；
- 补充子问题经 `_subquestions_from_critique` 过滤（去重、**最多 3 个**，id 形如 `r2q1`）；
- 若 critic 认为覆盖充分（无新子问题）→ **提前停止**。

轮数与扇出全部有界：`max_subquestions`、`max_rounds`、`results_per_subquestion`、`candidates`、`fetch_top_n`。

### 1.7 综合：带引用的 Markdown 报告

`engine.synthesize`（`engine.py:562`）。输入：各子问题的 findings 摘要（findings ≤8、key_* ≤6、open_problems ≤5）、
topic 的**种子资源**、**可引用来源列表**（`[n] 标题 — URL`）、以及 topic 规定的**章节结构**
（`topic.sections`，缺省用内置八段式）。

硬性写作要求：以 `# 标题` 开头 + 元信息行；每个论断带 `[n]` 且**只能引用给定编号**；经典/项目/数据集用表格
（列：`名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明`）；区分"近1-2年最新进展"与"经典工作"；
证据不足写 `> 待核实`；结尾附参考来源。语言由 `research.language`（`zh|en|bilingual`）经 `LANG_INSTRUCTIONS` 控制。

**降级报告 `_fallback_report`**：LLM 不可用时产出确定性 Markdown（findings 逐条列出 + 参考来源），
文件顶部标注"降级模式，需人工复核"。

### 1.8 LLM 客户端

`llm.py`。极简 OpenAI 兼容客户端，针对本网关（`whnetsea`）做了加固：

- **tiers**：`fast`（抽取）与 `strong`（规划/评审/综合）两档映射到具体 model id；默认都是 `deepseek-v4-flash`。
- **模型兜底**：主模型报 `model_not_found` / `no available channel` / `does not exist` / `unknown model` 时，
  自动尝试 `fallback_models`（默认 `deepseek-flash`）。
- **JSON 强制**：`json()` 用 `response_format={"type":"json_object"}`；解析失败时把上次回复回灌并要求"只输出合法 JSON"，
  最多重试 `retries` 次。`util.extract_json` 容忍 code fence、前后散文、尾逗号。
- **重试**：429/5xx 指数退避（`min(2**attempt,8)`）重试 `max_retries`；鉴权/校验错误快速失败。
- **健壮性**：`reasoning_content` 兜底；命中 `finish_reason=length` 且无正文时抛错提示调大 `max_tokens`。
- **统计**：累计 calls / prompt_tokens / completion_tokens，写入运行记录。

### 1.9 配置解析

`config.py`。解析链：**内置 `DEFAULTS` ← YAML 文件 ← 环境变量**。

- 文件位置：`--config` → `$RESEARCH_BOT_CONFIG` → `<home>/config/config.yaml`（缺失则纯默认）。
- 字符串支持 `${VAR}` / `${VAR:-default}`（POSIX 语义：空值算缺失）。
- CI 便利：`MAIL_TO`（逗号分隔）填充收件人，`EMAIL_ENABLED` / `EMAIL_DIGEST` 置位开关。
- 结果包成 `DotDict`（键可属性访问，递归）。
- `home` 通过 `find_home()` 定位（含 `topics/` 与 `skills/` 的目录；支持 `$RESEARCH_BOT_HOME`）。

---

## 2. 技术架构

### 2.1 流水线与数据流

```
topic.yaml
   │
   ▼
 PLAN ──(strong LLM / seed fallback)→ 3–8 子问题（queries + prefer）
   │
   ▼  每个子问题并行（round = 1..max_rounds）
 ┌───────────────────────────────────────────────────────────┐
 │ retrieve : router.search(每条 query) → 加权 RRF 融合        │
 │ rank     : 相关性门控 → 启发式打分 → 去重 → topN             │
 │ fetch    : 并发抓 topN 正文 → html_to_text                  │
 │ extract  : fast LLM → findings（四轴证据）+ key_* / gaps    │
 └───────────────────────────────────────────────────────────┘
   │  (round < max_rounds)
   ├──► CRITIQUE (strong LLM) ── 缺口/补检子问题 ──► 回到 retrieve
   │
   ▼
 SYNTHESIZE (strong LLM) → 带 [n] 引用的 Markdown
   │
   ▼
 SourceRegistry.reference_list() ──► 文末参考列表
   │
   ▼
 report/YYYY/MM/DD-<topic>.md + .json · latest/<topic>.md · index.json · push-log.jsonl
   │
   ▼
 EMAIL (SMTP, stdlib)
```

### 2.2 模块职责

| 路径 | 职责 |
| --- | --- |
| `engine.py` | **编排器**（DeerFlow lead-agent 等价物）：plan / retrieve / rank / extract / critique / synthesize；相关性门控与四轴证据 helper |
| `search/router.py` | 引擎注册、并行 fan-out、加权 RRF 融合、熔断、去重 |
| `search/engines.py` | 9 个引擎实现（arxiv/openalex/crossref/semantic_scholar/github/bing/sogou/so360/searxng） |
| `search/base.py` | `SearchResult` 数据模型 + `Engine` 基类 |
| `fetch.py` | 并发页面抓取 + HTML→文本 |
| `llm.py` | OpenAI 兼容客户端（tiers/兜底/JSON 强制/重试/统计） |
| `config.py` | `DEFAULTS ← YAML ← env` 合并、`${VAR}` 展开、`DotDict`、`find_home` |
| `util.py` | HTTP 重试、HTML→文本、`extract_json`、`norm_url`、日期/截断/slug |
| `skills.py` | DeerFlow 兼容 `SKILL.md` 加载（本地 + 子模块，本地优先） |
| `topics.py` | topic 定义（种子查询/资源/章节），`Topic` 数据类 |
| `report.py` | 落盘 md/json、`index.json` 台账、`push-log.jsonl` 审计、git/run 元数据 |
| `emailer.py` | 纯 stdlib SMTP：隐式 TLS(465)/STARTTLS(587)、Markdown→HTML 正文、附件 |
| `cli.py` | `rb` 管理工具：`run/doctor/skills/topics/engines/report/config` |

### 2.3 核心数据模型

- **`SearchResult`**：`title,url,snippet,engine,kind,published,authors,venue,citations,stars,extra{}`
  （`kind ∈ web|paper|project|dataset|news`；`extra` 存 `rrf_score`、`also_seen_on` 等）。
- **`SubQuestion`**：`id,question,queries,rationale,prefer,results,pages,extraction,round`。
- **`ResearchResult`**：整个 run 的完整记录（plan、subquestions、critiques、report_md、references、
  engines、skills、llm_stats、models、耗时/轮次），即 `.json` 报告的主体。

### 2.4 并发模型

| 层级 | 线程池 | 上限 |
| --- | --- | --- |
| 子问题之间 | `run()` | `max_workers=6` |
| 同一子问题的多条 query | `_retrieve_subquestion` | `min(4, len(queries))` |
| 单条 query 的多引擎 fan-out | `SearchRouter.search` | `min(8, N_engines)` |
| 页面抓取 | `fetch.fetch_many` | `workers=4` |

`arxiv` 单独用**进程级锁**自限速（`_min_interval=3.5s`），因为 router 是并发的而 arXiv 要求 ~1 req/3s。

### 2.5 深度档位（`DEPTH_PRESETS`）

| depth | max_subquestions | max_rounds | results_per_subquestion | fetch_top_n | candidates |
| --- | --- | --- | --- | --- | --- |
| `quick` | 3 | 1 | 4 | 2 | 12 |
| `standard` | 5 | 2 | 6 | 4 | 24 |
| `deep` | 8 | 3 | 8 | 6 | 32 |

（`standard` 时 `max_subquestions`/`max_rounds` 走配置默认，其余档位由 preset 收紧。）

### 2.6 产物与台账

```
report/
  index.json            每次运行台账（最新在前）；含 topic/来源数/findings/email/git/run_url
  push-log.jsonl        只追加的邮件投递审计
  latest/<topic>.md      每个 topic 最新报告
  YYYY/MM/DD-<topic>.md  带引用 Markdown
  YYYY/MM/DD-<topic>.json 完整结构化记录（含 references + 逐子问题抽取）
```

`report.ensure_footer` 保证文末有参考列表并追加一行元信息（topic/depth/rounds/engines/skills/model/sources/耗时）。

### 2.7 部署形态

- **本地 / cron**：`.venv/bin/rb run --topic vla --depth standard [--email]`；`make schedule` 打印 crontab 行。
- **GitHub Actions（推荐）**：`.github/workflows/daily-research.yml`，cron `0 22 * * *`（UTC，= 06:00 Asia/Shanghai），
  提交报告回仓库、发邮件、上传 artifact；支持手动 `workflow_dispatch`。
- **容器**：`Dockerfile` 造 base 镜像（只烤环境：Python 3.12 + `git` + `httpx/PyYAML/pytest/ruff/hatchling/editables`，
  **不烤代码**），由 `.github/workflows/image.yml` 发布到 `ghcr.io/embodist/research-bot-base:py3.12`；
  daily 任务在该镜像内跑，只需离线可编辑安装 `pip install -e . --no-deps --no-build-isolation`。

### 2.8 CLI（`rb`）

| 命令 | 用途 |
| --- | --- |
| `rb run` | 跑流水线（`--topic/--query/--depth/--rounds/--no-fetch/--email/--dry-run-email/--json`） |
| `rb doctor` | 自检：LLM + 各搜索引擎 + skills/topics + 邮件配置 |
| `rb skills` | 查看 skill（本地 + 子模块） |
| `rb topics` | 查看 topic 与种子资源 |
| `rb engines` | 查看/探测搜索引擎 |
| `rb report` | 查看报告归档与推送台账 |
| `rb config` | 查看/初始化配置 |

---

## 3. 关键不变量（改动时必须守住）

1. **引用稳定**：`SourceRegistry` 一旦分配 `[n]` 不再变；抽取/综合/文末列表共用同一编号空间。
2. **拒绝编造**：prompt 禁止臆造论文/URL/数字/榜单；综合只能引用给定编号；不足写 `> 待核实`。
3. **有界工作**：所有 fan-out 与轮次受 preset/配置约束，避免无界放大。
4. **单点失败不致命**：任一引擎、任一次抓取、任一次 LLM 调用失败都可降级，run 仍产出报告。
5. **相关性门控优先于召回**：宁可留空暴露缺口，不用噪声充数。

---

## 4. 为什么直接调用 DeerFlow 的 Python harness？

上游 harness 是完整 LangGraph 栈（gateway、sandbox、middleware、Kubernetes/E2B 沙箱、~80 依赖），
每日 Action 用它又慢又脆。本项目**只借用它的接口约定**——`SKILL.md` skill 包与 lead-agent/sub-agent 分工——
而 runner 保持依赖极轻。`deer-flow/` 子模块的保留让我们与上游对齐、并复用其全部 public skill，
但引擎在**子模块缺失时也能跑**（skills 回退到本地集合）。

---

## 5. 扩展点

- **加搜索引擎**：在 `search/engines.py` 写一个 `Engine` 子类（`name`/`kind`/`search()`），在
  `router.ENGINE_REGISTRY` 注册，并按信任度给 `ENGINE_WEIGHTS` 一个权重。
- **加 topic**：`cp topics/vla.yaml topics/my-topic.yaml`，改 `name/title/keywords/seed_queries/seed_resources/sections`；
  `keywords` 会喂给相关性门控。
- **加 skill**：在 `skills/<name>/SKILL.md` 写 YAML front-matter（`name`/`description`）+ Markdown 方法论；
  在 `config.research.skills` 里列名即注入所有 LLM system prompt。
- **换模型/网关**：改 `llm.base_url` / `llm.model` / `llm.tiers` / `llm.fallback_models`（走 `${VAR}` 环境变量）。
