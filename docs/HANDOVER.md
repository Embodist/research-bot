# 交接文档（HANDOVER）

> 面向**接手人**的运行与维护手册：怎么跑、怎么配、坑在哪、下一步做什么。
> 项目全貌见 [`README.md`](../README.md)，工程约定见 [`AGENTS.md`](../AGENTS.md)，AI 助手规则见
> [`CLAUDE.md`](../CLAUDE.md)。**最后更新：2026-10-02。**

---

## 1. 项目是什么

`research-bot` 是一个**无头（headless）深度调研 Agent**，用于持续跟踪 **具身智能 / VLA / 运动学 / C++ /
ROS 2** 的前沿进展、经典论文、开源项目与数据集。它基于 [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow)
的约定（`SKILL.md` 技能包 + lead-agent/sub-agent 拆解），但运行时**刻意保持轻依赖**（仅 `httpx` + `PyYAML`），
因此能在 GitHub Actions / cron / 容器里无 Docker、无数据库地跑。

一次运行的流程：`plan → retrieve（多引擎并行 + RRF 融合）→ extract（分级证据）→ critique（找缺口补检）
→ synthesize（带 `[n]` 引用的 Markdown 报告）`，产物落到 `report/` 并（可选）邮件推送。

## 2. 当前状态（截至 2026-10-02）

| 项 | 状态 |
| --- | --- |
| CLI / 引擎 / 5 个 topic / 10 个 skill | ✅ 完成 |
| 离线测试 | ✅ 48 项通过（`pytest`） |
| lint（`src tests`） | ✅ 通过（`deer-flow/` 子模块不在范围内） |
| GitHub Actions 每日工作流 | ✅ 已配置（`0 22 * * *` UTC = 06:00 Asia/Shanghai） |
| 邮件（本地） | ✅ 已配置并**实测发送成功**（163 → outlook） |
| 邮件（CI） | ⏳ 待把 Secrets/Variables 写入仓库（见 §6、§11） |
| 报告质量 | ⚠️ 检索域漂移问题，已缓解未根治（见 §10） |
| `embodied-ai` / `cpp-robotics` 报告 | ⏳ 尚未生成（见 §11） |

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
  search/             engines.py（各引擎）+ router.py（RRF 融合 + 引擎权重）+ base.py
  config.py llm.py fetch.py skills.py topics.py report.py emailer.py cli.py util.py
skills/               本地技能（SKILL.md）
topics/               研究主题（seed 查询 + 种子资源目录）
config/               config.example.yaml（入库）；config.yaml（gitignore，含密钥）
report/               生成的报告 + 推送台账
deer-flow/            upstream 子模块（**不要在其中编辑**）
tests/                pytest（离线、确定性）
.github/workflows/    daily-research.yml、ci.yml
scripts/              bootstrap.sh、run_daily.sh、import_skill.sh、set_github_secrets.py
docs/                 architecture / email / github-actions / scheduling / skills-and-sources / HANDOVER
```

## 6. 配置与密钥（**不要提交任何密钥**）

**本地**（`config/config.yaml`，已 gitignore）：LLM、search、research、email 四段。
可覆盖的环境变量见 [`.env.example`](../.env.example)。

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
- **Makefile**：`make run TOPIC=vla DEPTH=quick` / `make run-all` / `make doctor` / `make test` / `make lint`
- **GitHub Actions**：每日 `0 22 * * *` UTC 自动跑并回提交 + 发摘要邮件；也可 Actions → Daily Research →
  Run workflow 手动触发（可选 topic/depth/send_email）
- **本地 cron/systemd**：见 [`docs/scheduling.md`](scheduling.md)

## 8. 输出产物

```
report/
  index.json          每次运行的台账（最新在前）：topic/标题/来源数/邮件状态/commit/run URL
  push-log.jsonl      邮件投递追加审计
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

第三方镜像（ghfast.top / ghproxy.net）虽可达，但会把 GitHub 凭据经手第三方，**不建议**用于推送。

## 10. 已知问题与限制

1. **检索域漂移（主要质量问题）**：HTML 引擎对同名词会召回严重离题结果（ROS → *reactive oxygen species*、
   *Pinocchio* → 童话、*Drake* → Drake 方程）。**已缓解**：`router.rrf_fuse` 给结构化/学术引擎更高权重；
   `engine._filter_relevant` 用 topic 关键词 + 查询词对 HTML 结果做相关性门控（学术结果信任、且不会清空
   子问题）。**未根治**：仍可能漏网，彻底的方案是 LLM rerank 或限定符检索。
2. **模型 id**：网关只服务 `deepseek-v4-flash`；请求 `deepseek-v1-flash` 会 `model_not_found`。
3. **`deer-flow/` 子模块**：直接 `ruff check .` 会报 100+ 错，**全在子模块内**，不在 `src tests` 范围内，忽略即可。
4. **`set_github_secrets.py` 只写 Secrets**，不写 Variables（见 §6）。
5. **降级行为**：LLM 不可用时仍会产出「源码接地」的降级报告；搜索引擎被墙则按熔断逐个剔除——CI 不会因网络
   受限而失败，但报告可能因此变薄。

## 11. 待办 / 下一步

- [ ] 把 LLM/SMTP 写入 GitHub **Secrets**，并把 `LLM_MODEL`/`LLM_BASE_URL`/`SEARXNG_URL` 写入 **Variables**，
      然后手动触发一次 Daily Research 验证 CI 邮件链路。
- [ ] 生成尚缺的 `embodied-ai`、`cpp-robotics` 两份报告。
- [ ] （可选）用 LLM 对候选结果做一次 rerank / 相关性打分，进一步压掉域漂移。
- [ ] （可选）验证 WSL 代理主机 IP 变化时的推送脚本化（当前需手动取 nameserver）。

## 12. 故障排查

| 症状 | 处理 |
| --- | --- |
| `git push` 超时 | github 直连被墙，走 §9 的代理 |
| `model_not_found: deepseek-v1-flash` | 改用 `deepseek-v4-flash` |
| `rb doctor` 里部分引擎 FAIL | 受限网络下的预期行为，其余引擎仍会跑 |
| 新报告来源很少 / 空 | 扩大 `search.engines`、设 `GITHUB_TOKEN`、或提高 `research.max_subquestions` |
| 邮件未发送 | `rb doctor` 看 `configured=True`，核对 SMTP Secrets / `config.yaml` |
| CI 检出子模块失败 | 工作流用 `submodules: false`，引擎无需子模块即可运行 |

---
MIT licensed. DeerFlow 归其各自作者所有（MIT）。
