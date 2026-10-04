# CLAUDE.md

本文件是 Claude Code 在本仓库工作时的**操作要点**。工程约定（依赖、目录、测试、子模块）见
[`AGENTS.md`](AGENTS.md)，项目全貌见 [`README.md`](README.md)，交接信息见
[`docs/HANDOVER.md`](docs/HANDOVER.md)。

## 硬性规则（必须遵守）

1. **每一次变更都要提交 commit。** 完成一个最小可独立说明的改动就立即 commit，不要积攒。提交信息用
   Conventional Commits 前缀（`feat:` / `fix:` / `chore:` / `docs:` / `harden:` / `refactor:` / `test:`），
   与现有历史风格一致。
2. **提交后自动 push 到 `origin/main`。** 本仓库的交付物就是远端仓库，保持本地与远端同步，不要留下
   未推送的 commit。（历史上曾因会话中断导致 2 个 commit 卡在本地未推送。）
3. **维护交接文档。** 凡是影响"接手人能否独立运行/维护"的改动（架构、配置项、运行方式、已知问题、
   待办），同步更新 [`docs/HANDOVER.md`](docs/HANDOVER.md)。新增的坑与未决事项要写进其中的
   "已知问题 / 待办"。
4. **绝不提交密钥。** `config/config.yaml`、`.env*`、`.claude/` 含明文凭据，均已或被要求 gitignore。
   提交前用 `git status` 确认，不要 `git add -A` 误带。密钥只走环境变量 / GitHub Secrets。
5. **报告质量优先于"跑通"。** 检索域漂移（同名词，如 ROS→reactive oxygen species）是本项目已知的主要
   质量问题；不要用"CI 绿了"掩盖低质量报告。

## 协作偏好

- 与用户用**中文**沟通；代码、命令、术语保留英文。
- 用户会时不时问"进度怎么样了"——回答时先读 memory 与 `git log`，以**最高价值的未决问题**开头，而不是
  罗列已完成的绿色项。
- 需要用户提供凭据（如 SMTP）时，明确列出需要的字段，不要臆造。

## 常用命令

```bash
.venv/bin/pytest                      # 离线测试（不联网）
.venv/bin/ruff check src tests        # lint（只查 src/tests；deer-flow/ 子模块不在范围内）
.venv/bin/rb doctor                   # 联网自检：LLM + 各搜索引擎 + 邮件配置
.venv/bin/rb run --topic vla --depth quick
make help                             # 全部管理目标
```

## 环境

- Python ≥ 3.10；运行时依赖仅 `httpx` + `PyYAML`（不要引入重依赖，见 AGENTS.md）。
- LLM 网关默认 `https://api.deepseek.com/v1`（DeepSeek 官网）；**可用模型 id 是 `deepseek-v4-flash`**
  （官网 canonical id，别名 `deepseek-flash`）；可用 `${LLM_BASE_URL}` / `${LLM_MODEL}` 覆盖。
- `deer-flow/` 是 pinned git submodule，**不要在其中编辑**；引擎在子模块缺失时也必须能跑。
