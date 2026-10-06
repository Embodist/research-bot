# 交接文档（HANDOVER）

> 面向**接手人**的运行与维护手册：怎么跑、怎么配、坑在哪、下一步做什么。
> 项目全貌见 [`README.md`](../README.md)，工程约定见 [`AGENTS.md`](../AGENTS.md)，AI 助手规则见
> [`CLAUDE.md`](../CLAUDE.md)，**deep-research 技术核心与架构**见 [`docs/deep-research.md`](deep-research.md)。
> **最后更新：2026-10-04。**

---

## 1. 项目是什么

`research-bot` 是一个**无头（headless）深度调研 Agent**，用于持续跟踪 **具身智能 / VLA / 运动学 / C++ /
ROS 2** 的前沿进展、经典论文、开源项目与数据集。它基于 [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow)
的约定（`SKILL.md` 技能包 + lead-agent/sub-agent 拆解），但运行时**刻意保持轻依赖**（仅 `httpx` + `PyYAML`），
因此既能在 GitHub Actions / cron 里**直接跑**（不需 Docker、不需数据库），也能收进容器（见 §2 的 base 镜像）。

一次运行的流程：`plan → retrieve（多引擎并行 + RRF 融合）→ extract（分级证据）→ critique（找缺口补检）
→ synthesize（带 `[n]` 引用的 Markdown 报告）`，产物落到 `report/` 并（可选）邮件推送。

## 2. 当前状态（截至 2026-10-04）

| 项 | 状态 |
| --- | --- |
| CLI / 引擎 / **11 个 topic** / 13 个 skill | ✅ 完成 |
| 离线测试 | ✅ 78 项通过（`pytest`） |
| lint（`src tests`） | ✅ 通过（`deer-flow/` 子模块不在范围内） |
| GitHub Actions 每日工作流 | ✅ 已配置（`0 22 * * *` UTC = 06:00 Asia/Shanghai）——**定时只跑增量 watch**；调研/初始改为按需手动 |
| 邮件（本地） | ✅ 已配置并**实测发送成功**（163 → outlook） |
| 邮件（CI） | ✅ 7 个 Secrets + 2 个 Variables 已写入仓库；`--email` 强制发信修复后实测 `sent=True`（见 §10.11） |
| 报告质量 | ✅ 检索域漂移已修复（统一相关性门控，见 §10） |
| 证据要求 | ✅ 每条结论四轴证据：热度 / 权威 / 关注度 / 推荐度（见 §10） |
| **HTTP 服务** | ✅ `rb serve`（stdlib `http.server`，异步任务 API）；离线测试覆盖，见 `docs/service.md` |
| **跨领域知识体系** | ✅ 两套固定骨架（`knowledge` 学习 / `watch` 增量）+ 确定性覆盖度评估（`mode=knowledge\|watch`、`rb run --knowledge\|--watch`），见 `docs/knowledge-framework.md` |
| **SQLite 知识库** | ✅ 多级 topic + 条目去重 + 增量 diff + 推送台账（不存地址）；`rb kb` / `rb run --kb`；CI 用 `actions/cache` 持久化，见 `docs/knowledge-base.md` |
| Docker base 镜像 | ✅ `Dockerfile` + `image.yml` 发布到 `ghcr.io/embodist/research-bot-base:py3.12`；daily 工作流在该容器内跑，**容器内全链路已实测转绿**（run `36999238952`，2026-10-02：install → doctor → research → 回提交 → artifact 全 success） |

> **Docker base 镜像**：只烤环境（Python 3.12 + `git` + `httpx/PyYAML/pytest/ruff/hatchling/editables`），
> **不烤代码**——代码由 `actions/checkout` 挂载，故改代码无需重建镜像，仅改 `Dockerfile`/`pyproject.toml` 才重建。
> daily 任务因此省去 `setup-python` 与依赖安装，只做一次离线可编辑安装
> `pip install -e . --no-deps --no-build-isolation`。**首次需先跑一次 `Base image` 工作流发布镜像**，
> daily 才能拉到。详见 `docs/github-actions.md`。

新增 topic：`cybersecurity`、`ai`、`music-audio`（MIR/CSI/音乐生成·理解/SVC/音频分离），以及具身细分方向
`embodied-humanoid`、`embodied-manipulation`、`embodied-world-models`。

## 3. 接手人 30 分钟跑起来

```bash
git clone --recurse-submodules https://github.com/Embodist/research-bot.git
cd research-bot
uv venv .venv && uv pip install --python .venv/bin/python -e ".[dev]"
cp config/config.example.yaml config/config.yaml     # 然后填 LLM/SMTP（见 §6）
.venv/bin/rb doctor                                  # 自检：LLM + 各搜索引擎 + 邮件配置
.venv/bin/rb run --topic vla --depth quick           # 跑一个 topic
.venv/bin/python -m pytest                            # 离线测试
```

> 国内网络装依赖慢时用镜像：`pip install -e . -i https://repo.huaweicloud.com/repository/pypi/simple`。

## 4. 架构与数据流

```
rb CLI → DeepResearchEngine（lead agent）
  planner  → 拆子问题 + 生成查询词
  researcher ×N → SearchRouter（arxiv/openalex/crossref/semantic_scholar/github/bing/sogou/so360/searxng
                  并行 → RRF 融合加权 → 相关性门控 → rank → fetch 正文 → LLM 抽取分级证据）
  critic   → 覆盖度评估 + 补检索
  synthesizer → 注入 skills 生成带引用 Markdown
  emailer / report store → SMTP + report/*.md/.json + index.json + push-log.jsonl
```

细节见 [`docs/architecture.md`](architecture.md)。

## 5. 仓库结构

```
src/research_bot/     Python 包（产品本体）
  engine.py           编排器（plan/retrieve/extract/critique/synthesize）
  serve.py            HTTP 服务（stdlib：异步任务 API + 可选 bearer token）
  knowledge.py        跨领域固定骨架（knowledge 学习 / watch 增量）+ 覆盖率评估
  store.py            SQLite 知识库（多级 topic / 报告历史 / 条目去重 / 推送台账）
  search/             engines.py（各引擎）+ router.py（RRF 融合 + 引擎权重）+ base.py
  config.py llm.py fetch.py skills.py topics.py report.py emailer.py cli.py util.py
skills/               本地技能（SKILL.md，含 knowledge-framework、frontier-watch）
topics/               研究主题（seed 查询 + 种子资源目录）
config/               config.example.yaml（入库）；config.yaml（gitignore，含密钥）
report/               生成的报告 + 推送台账
deer-flow/            upstream 子模块（**不要在其中编辑**）
tests/                pytest（离线、确定性）
Dockerfile            base 镜像定义（`python:3.12-slim`，只烤环境不烤代码）；配合 `.dockerignore`
docker-compose.yml    即用即起地跑 HTTP 服务（挂载仓库 + 装 editable + 起 `rb serve`）
.github/workflows/    daily-research.yml（每日，容器内跑）、image.yml（发布 base 镜像）、ci.yml（lint+test）
scripts/              bootstrap.sh、run_daily.sh、import_skill.sh、set_github_secrets.py
docs/                 architecture / deep-research / service / knowledge-framework / knowledge-base / email / github-actions / scheduling / skills-and-sources / intelligence_governance_final_report（长期研究蓝图：World→Value→Decision→Governance 闭环，指导 watch 领域收敛）/ HANDOVER
```

## 6. 配置与密钥（**不要提交任何密钥**）

**本地**（`config/config.yaml`，已 gitignore）：LLM、search、research、email 四段。
可覆盖的环境变量见 [`.env.example`](../.env.example)。`rb` 启动时会自动加载 `<repo>/.env`（已存在的
环境变量优先、不覆盖），因此密钥与 `LLM_BASE_URL` 可只放 `.env`，不必写进 `config.yaml`；
`config.yaml` 里对应值写成 `${LLM_BASE_URL:-...}` 占位即可被 env 注入。

**GitHub Actions**（Settings → Secrets and variables → Actions）——注意 **Secrets 与 Variables 是两处**：

| 类型 | 名称 | 用途 |
| --- | --- | --- |
| Secret | `LLM_API_KEY` | LLM 网关密钥 |
| Secret | `SMTP_HOST` / `SMTP_PORT` / `SMTP_USER` / `SMTP_PASS` / `SMTP_FROM` / `MAIL_TO` | 邮件 |
| Variable | `LLM_MODEL` / `LLM_BASE_URL` / `SEARXNG_URL` | 非敏感配置 |

写入 Secrets：`python scripts/set_github_secrets.py Embodist/research-bot`（需 `pip install pynacl` 与
一个有 repo+workflow 权限的 token）。**注意：该脚本只写 Secrets，不写 Variables**——`vars.LLM_MODEL` 等
需在网页或另用 API 设置。

> 含明文凭据的 `config/config.yaml`、`.env*`、`.claude/` 均不得入库。提交前务必 `git status` 核对，
> 不要 `git add -A`。

## 7. 运行方式

- **单次**：`.venv/bin/rb run --topic vla --depth standard [--email]`
- **全部 + 邮件**：`.venv/bin/rb run --topic all --email`
- **知识地图（方向1：学习）**：`.venv/bin/rb run --knowledge --query "C++ RAII 的核心思想" --depth quick`（打印 coverage + gaps）
- **增量追踪（方向2：变化/蓝海/产业/社会）**：`.venv/bin/rb run --watch --query "具身智能世界模型" --depth quick`
- **知识库**：`.venv/bin/rb kb init|stats|topics|recent|new`；`rb run ... --kb` 会把本次 run 入库并打印增量
  `+N new, ~M updated, K known`。watch 且无新增/变化时默认**跳过邮件**（`kb.skip_email_when_unchanged`）。
- **HTTP 服务**：`.venv/bin/rb serve --host 0.0.0.0 --port 8080 --workers 2`（`make serve` / `docker compose up`）；
  `POST /research` 传 `query`/`topic`（+ `mode=knowledge|watch`），轮询 `GET /research/{id}`；可选 `RESEARCH_BOT_API_TOKEN` 鉴权。
  详见 [`docs/service.md`](service.md)。
- **Makefile**：`make run TOPIC=vla DEPTH=quick` / `make run-all` / `make serve` / `make doctor` / `make test` / `make lint`
- **GitHub Actions（`Daily Watch`）**：**定时 `0 22 * * *` UTC 只跑增量 watch**——对收敛后的快变前沿
  （默认 6 条：具身智能/VLA/机器人 + 价值对齐 / Agent 评测与安全 / AI 治理；作为工作流默认值提交在 git，
  可用仓库 Variable `WATCH_QUERIES` 覆盖）逐条
  `rb run --watch --query ... --kb --email`，回提交报告。**调研（research/topic）与初始（knowledge 建知识地图）
  不进流水线**，改为按需手动：Actions → Daily Watch → Run workflow（`mode=research|knowledge|watch` 配
  `topic` / `query`，加 `depth` / `send_email`）。手动触发只跑所请求的 mode；`Run watch increments`
  **只在 schedule 事件**执行，避免重复。**首个领域的首次 watch 即基线**，之后靠 KB 去重只报增量。
- **容器（可复现，无需本地装 Python）**：
  `docker run --rm -v "$PWD":/app -w /app -e LLM_API_KEY=... ghcr.io/embodist/research-bot-base:py3.12 sh -c 'pip install -e . --no-deps --no-build-isolation && rb run --topic vla --depth quick'`
- **本地 cron/systemd**：见 [`docs/scheduling.md`](scheduling.md)

## 8. 输出产物

```
report/
  index.json          每次运行的台账（最新在前）：topic/标题/来源数/邮件状态/commit/run URL
  push-log.jsonl      邮件投递追加审计（**gitignore，不入库**；仅作为 CI artifact 上传）
  latest/<topic>.md   每个 topic 的最新报告
  2026/10/2026-10-02-<topic>.md / .json   带引用报告 + 完整结构化记录
```

## 9. 网络与推送（**重要，容易卡住**）

本机（WSL2）**直连 `github.com:443` 会被阻断**（DNS 能解析 20.205.243.166，但 TCP 超时）。pi 会话当初就是
卡在 push 上。可用路径：**Windows 主机上的代理**，在 WSL2 NAT 模式下地址是 `/etc/resolv.conf` 里的
nameserver（当前为 `172.24.16.1`，端口 `54321`；`localhost` 在 WSL 内到不了它）。

```bash
HOST=$(grep -i nameserver /etc/resolv.conf | awk '{print $2}')   # 例如 172.24.16.1
export https_proxy=http://$HOST:54321 http_proxy=http://$HOST:54321
git push origin main
```

> **已配置仓库级自动推送**（2026-10-02）：`.git/config` 里设了 `credential.helper = store --file=.git/.credentials`
> （token 存于 `.git/.credentials`，权限 600，已写入 `.git/info/exclude`）以及 `http(s).proxy`。因此在本仓库内
> 直接 `git push origin main` 即可，无需再手动设 token；仅当代理主机 IP 变化时才需改 `http.proxy`。

第三方镜像（ghfast.top / ghproxy.net）虽可达，但会把 GitHub 凭据经手第三方，**不建议**用于推送。

## 10. 已知问题与限制

1. **检索域漂移（已修复，2026-10-02）**：同名词会让检索离题——不只是 HTML 引擎，**关键词匹配的学术引擎
   （Crossref/OpenAlex）同样会召回**（ROS → *reactive oxygen species*、`pi0` → π⁰ 介子、`project` → 游戏工作室）。
   修复分两层：
   - `router.rrf_fuse` 给结构化/学术引擎更高权重（`ENGINE_WEIGHTS`）；
   - `engine._filter_relevant` 用**统一门控**：候选必须含 topic 关键词，或与查询重叠 **≥2 个有区分度词**
     （`_GENERIC_TOKENS` 停用词表剔除 best/practices/project/survey 等泛词）。门控对**所有引擎**生效；
     若子问题被全部滤掉，**故意留空**以暴露检索缺口，而不是用垃圾凑数。
2. **证据四轴（2026-10-02）**：每条关键结论/条目必须给出**热度**（引用/star/下载）、**权威**（venue/同行评审/
   官方文档）、**关注度**（高/中/低 + 依据）、**推荐度**（★1-5 + 理由）。抽取与综合 prompt 强制要求，报告证据表
   列为 `名称|年份|机构/作者|热度|权威|关注度|推荐度|链接|说明`；取不到的写 `> 待核实`，**不得编造数字**。
   降级抽取（LLM 不可用）用 `_attention_text` / `_recommendation_text` 从 citations/stars/venue 确定性推导。
3. **模型 id**：默认网关是 DeepSeek 官网（`https://api.deepseek.com/v1`），canonical id 为
   `deepseek-v4-flash`（别名 `deepseek-flash`）；换网关时改 `llm.base_url` / `llm.model`（走 `${LLM_BASE_URL}` /
   `${LLM_MODEL}`）。
4. **`deer-flow/` 子模块**：直接 `ruff check .` 会报 100+ 错，**全在子模块内**，不在 `src tests` 范围内，忽略即可。
5. **`set_github_secrets.py` 只写 Secrets**，不写 Variables（见 §6）。
6. **降级行为**：LLM 不可用时仍会产出「源码接地」的降级报告；搜索引擎被墙则按熔断逐个剔除——CI 不会因网络
   受限而失败，但报告可能因此变薄。
7. **`.claude/` 曾含明文 `ANTHROPIC_AUTH_TOKEN`**，已加入 `.gitignore`（不提交）。`report/push-log.jsonl`
   含收件邮箱，也已加入 `.gitignore`（此前会被 CI 的 `git add report/` 误提交，2026-10-02 修复）；它仍作为
   CI artifact 上传以便审计，只是不入 git 历史。
8. **GitHub Actions 容器任务的 `sh` 陷阱（2026-10-02）**：`container:` 任务的所有 `run:` 步骤默认用镜像里的
   `sh -e {0}` 执行（**不是 bash**），因此 bash 专有语法（`ARGS=(...)` 数组、`set -o pipefail`）会报
   `Syntax error: "(" unexpected`；且容器内 checkout 属主是 runner uid，第一条 git 命令会报
   `fatal: not in a git directory`。修复：脚本保持 POSIX 兼容（用位置参数 `set --` 代替数组），并在 commit
   前 `git config --global --add safe.directory "$GITHUB_WORKSPACE"`；工作流另把 `defaults.run.working-directory`
   钉到 workspace。详见 `docs/github-actions.md`。
9. **CI 提交回写的竞态（2026-10-02）**：daily 任务运行数分钟，期间 `main` 可能已被手动推送推进，
   `git push` 会因 non-fast-forward 被拒（`fetch first`）。修复：commit 后先 `git pull --rebase origin main`
   再 push。若同一天同一 topic 已有报告，rebase 可能冲突并失败——属可接受的显式失败。
10. **HTTP 服务是开发级、内存态（2026-10-04）**：`rb serve` 基于标准库 `http.server`，未做公网硬化；
   作业历史仅存内存（默认保留最近 200 个已结束作业，重启即丢，报告本身仍落盘 `report/`）。生产应在反向代理
   （TLS/限流）之后运行，并设 `RESEARCH_BOT_API_TOKEN`；否则服务**开放无鉴权**（启动日志会警告）。并发受
   `--workers` 限（LLM 花费上界），`config` 覆盖只接受 `DEFAULTS` 顶层段（`llm/search/research/report/email`），
   经 `deep_merge`+`expand_env`，**绝不 eval**。
11. **CI 邮件此前一直未发（已修复，2026-10-04）**：`--email` 的语义是"即使 config 里 disabled 也强制发信"，
   但 `cmd_run` 只把它算进 `push_requested`，从未把 `cfg.email.enabled` 置真——emailer 里
   `if not cfg.enabled: "email disabled"` 会直接拦下。CI 无 `config.yaml`（默认 `enabled:false`），故线上
   即使传了 `--email` 也**只回提交报告、不发邮件**（日志里 `sent=False error=email disabled`）。修复：
   `args.email` 为真时强制 `cfg.email.enabled=True`（回归测试 `tests/test_cli.py`）；本地/CI 均恢复正常发信。

## 11. 待办 / 下一步

**已闭环（决策记录）**
- 旧归档报告（`vla`/`ros2`/`kinematics`/`embodied-ai`/`cpp-robotics`）**保留原样**：用户 2026-10-02 明确
  「已归档的不管」——改代码后新跑的报告一律带四轴，旧归档作为历史快照不动。日后如要统一，逐 topic 重跑即可。

**待办**
- [ ] （可选）用 LLM 对候选结果做一次 rerank / 相关性打分，进一步压掉域漂移。
- [ ] （可选）验证 WSL 代理主机 IP 变化时的推送脚本化（当前需手动取 nameserver）。

## 12. 故障排查

| 症状 | 处理 |
| --- | --- |
| `git push` 超时 | github 直连被墙，走 §9 的代理 |
| `model_not_found` | 把 `llm.model` 改成你的网关所服务的 id（默认 `deepseek-v4-flash`） |
| `rb doctor` 里部分引擎 FAIL | 受限网络下的预期行为，其余引擎仍会跑 |
| 新报告来源很少 / 空 | 扩大 `search.engines`、设 `GITHUB_TOKEN`、或提高 `research.max_subquestions` |
| 邮件未发送 | `rb doctor` 看 `configured=True`，核对 SMTP Secrets / `config.yaml` |
| CI 日志 `sent=False error=email disabled` | `--email` 现已强制置 `enabled=True`（见 §10.11）；若仍失败，核对 6 个 SMTP Secrets |
| CI 检出子模块失败 | 工作流用 `submodules: false`，引擎无需子模块即可运行 |
| CI 回提交被拒（`fetch first`） | 工作流已内置 `git pull --rebase origin main` 后再 push（见 §10.9）；手动 / 并发推送时就会遇到 |
| CI 容器内 `Syntax error: "("` / `not in a git directory` | 容器任务默认 `sh` 且 workspace 未受信任（见 §10.8）；脚本须 POSIX、并设 `safe.directory` |
| `rb serve` 返回 401 | 已设 `RESEARCH_BOT_API_TOKEN`；请求需带 `Authorization: Bearer <token>`（`/healthz` 除外） |
| `rb serve` 返回 400 `unknown config section` | `config` 覆盖只能是 `DEFAULTS` 顶层段（`llm/search/research/report/email`） |
| `rb serve` 返回 422 `mode must be one of` | `mode` 只能是 `research` / `knowledge` / `watch` |
| 知识/增量模式 `coverage` 有 gap | 属预期——报告确实缺该维/缺引用/缺 elements（见 `docs/knowledge-framework.md`） |
| 报告只写到前几维 / 后半截断 | 综合输出被截断时**会自动补写**缺失章节（`engine._complete_sections`，插到参考列表前）；仍不够就调大 `llm.max_tokens_report`（默认 16384，env `LLM_MAX_TOKENS_REPORT`）。日志会记 "synthesis truncated" |
| 报告混入与本领域无关的论文 | 相关性门控已改为**关键词整词匹配**（`_keyword_hit`）；若仍漂移，多为 planner 生成了过泛查询，收紧种子查询 |

---
MIT licensed. DeerFlow 归其各自作者所有（MIT）。
