# Daily automation with GitHub Actions

The workflow is [`.github/workflows/daily-research.yml`](../.github/workflows/daily-research.yml) (`Daily
Watch`). It:

1. runs **inside the prebuilt base image** `ghcr.io/embodist/research-bot-base:py3.12`
   (see [Docker base image](#docker-base-image)) — Python and every dependency are already present,
2. checks out the repo (**without** the submodule — the engine works without it),
3. does an offline editable install of the checked-out code (`pip install -e . --no-deps --no-build-isolation`),
4. runs `rb doctor` (non-fatal preflight, logged),
5. on the **daily schedule** runs **only the incremental watch** — one `rb run --watch --query <domain>
   --kb --email` per converged domain in `WATCH_QUERIES`; on a **manual dispatch** runs the requested mode
   (`research` / `knowledge` / `watch`),
6. commits `report/` back to the repo,
7. uploads the Markdown/JSON reports + `push-log.jsonl` as a build artifact.

> **What runs when — 调研 / 初始 / 增量.** The daily cron is reserved for **increments** (`watch`: track how
> a domain changed). One-off **research** (`research`: survey a topic) and **knowledge** (`knowledge`: build
> a domain's knowledge map — the "initial") are **not scheduled**; trigger them on demand with
> `workflow_dispatch`. The first watch run for a domain establishes its baseline (everything reads as
> "new"); later runs email only the delta, so an "initial" snapshot never needs to live in the pipeline.

## Docker base image

The image is built by [`.github/workflows/image.yml`](../.github/workflows/image.yml) and published to
GitHub Container Registry. It bakes in **only the environment** — Python 3.12, `git`, and the
`httpx`/`PyYAML`/`pytest`/`ruff`/`hatchling`/`editables` packages — **not the application code**. The code
is checked out and mounted at run time, so editing code never requires rebuilding the image; only changing
`Dockerfile` or `pyproject.toml` does.

| Item | Value |
| --- | --- |
| Image | `ghcr.io/embodist/research-bot-base:py3.12` (also `:latest`) |
| Rebuild triggers | push to `main` touching `Dockerfile`, `.dockerignore`, `pyproject.toml`, or `image.yml`; or manual `workflow_dispatch` |
| Permissions | `packages: write` to publish; the daily job uses `packages: read` + `GITHUB_TOKEN` to pull |

> **First-run ordering.** Publish the image once (the `Base image` workflow runs automatically on the
> push that adds the Dockerfile, or trigger it manually) **before** the daily workflow can pull it.

> **Container-mode gotchas.** A job with `container:` runs its `run:` steps with the image's **default
> shell `sh -e {0}`**, not bash — so bash-only syntax (arrays such as `ARGS=(...)`, `set -o pipefail`)
> fails with `Syntax error: "(" unexpected`. Keep job scripts POSIX-only. Also, the checkout inside the
> container is owned by the runner uid, so the first git command fails with `fatal: not in a git
> directory` until the workspace is trusted: `git config --global --add safe.directory "$GITHUB_WORKSPACE"`.
> The daily workflow pins `defaults.run.working-directory` to the workspace and does both. Because the job
> runs for minutes and `main` can move underneath it, the commit-back step rebases
> (`git pull --rebase origin main`) before pushing, so a concurrent/manual push does not reject it with
> `fetch first`.

Run the same image locally without installing Python:

```bash
docker run --rm -v "$PWD":/app -w /app \
  -e LLM_API_KEY=... \
  ghcr.io/embodist/research-bot-base:py3.12 \
  sh -c 'pip install -e . --no-deps --no-build-isolation && rb run --topic vla --depth quick'
```

## Configure secrets

**Settings → Secrets and variables → Actions**.

### Secrets

| Secret | Required | Notes |
| --- | --- | --- |
| `LLM_API_KEY` | yes | DeepSeek / OpenAI-compatible key |
| `SMTP_HOST` | for email | e.g. `smtp.qq.com`, `smtp.gmail.com` |
| `SMTP_PORT` | for email | `465` (SSL) or `587` (STARTTLS) |
| `SMTP_USER` | for email | login user |
| `SMTP_PASS` | for email | SMTP auth code / password |
| `SMTP_FROM` | for email | sender address (must match the provider's rules) |
| `MAIL_TO` | for email | comma-separated recipients, e.g. `a@x.com,b@y.com` |

`GITHUB_TOKEN` is provided automatically and is passed through for GitHub API search rate limits.

### Variables (optional)

| Variable | Default | Notes |
| --- | --- | --- |
| `LLM_MODEL` | `deepseek-v4-flash` | override the model id |
| `LLM_BASE_URL` | `https://api.deepseek.com/v1` | OpenAI-compatible base URL (this repo is set to the whnetsea gateway) |
| `SEARXNG_URL` | `http://43.155.145.78:58881` | your SearXNG (JSON or HTML) |
| `WATCH_QUERIES` | *(workflow default — the converged core domains)* | 增量追踪的领域：逗号/换行分隔。**不设**则用工作流里已提交的默认清单（具身智能/VLA/机器人）；条目不要含 ASCII 逗号（查询里的顿号 `、` 安全） |
| `WATCH_DEPTH` | `quick` | watch 步骤的深度 |

> **每日增量（watch）**：`Run watch increments` 步骤**只在 schedule 事件**运行，对 `WATCH_QUERIES` 的每条查询跑
> `rb run --watch --query ... --kb --email`。领域清单**收敛到项目核心**并作为工作流默认值提交在 git 里
> （可用同名仓库 Variable 覆盖）。`--kb` 让每次增量入库；若本次既无新增也无变化，邮件被**去重跳过**
> （见 [`docs/knowledge-base.md`](knowledge-base.md)）。知识库 `report/knowledge.db` 由 `actions/cache`
> 跨天持久化（不提交进 git）。**首个领域的首次 watch** 即建立基线（都是 "new"），之后才是真增量——
> 所以"初始"不必进流水线，按需手动触发即可。

## Schedule

```yaml
on:
  schedule:
    - cron: "0 22 * * *"   # 22:00 UTC = 06:00 Asia/Shanghai
```

GitHub cron is always UTC. The schedule runs **only the incremental watch**. One-off research / knowledge
runs are triggered on demand from the **Actions → Daily Watch → Run workflow** button (or `gh`), with
inputs `mode` (`research` | `knowledge` | `watch`), `topic` (mode=research), `query` (mode=knowledge|watch),
`depth` and `send_email`.

## Commit-back permissions

The workflow requests `permissions: contents: write` and pushes as
`github-actions[bot]`. If your default branch is protected, allow GitHub Actions to bypass the branch
protection rule or push to a dedicated reports branch.

## Manual run

```bash
# research mode (default): one topic or 'all'
gh workflow run daily-research.yml -f mode=research -f topic=vla -f depth=deep -f send_email=true

# knowledge / watch mode: a free-text query
gh workflow run daily-research.yml -f mode=knowledge -f query="C++ RAII 的核心思想与边界" -f depth=quick
gh workflow run daily-research.yml -f mode=watch -f query="具身智能世界模型" -f depth=quick
```

> A manual dispatch runs **exactly** the requested mode; the `Run watch increments` step (which walks
> `WATCH_QUERIES`) is gated to the **schedule** event, so it does not double-run on a manual trigger.

## Rate limits & cost notes

- `rb run --topic all` performs ~5 topics × 3–8 sub-questions × (search + fetch + 2–4 LLM calls). On the
  default `standard` depth this is roughly 30–60 LLM calls per topic; use `--depth quick` for cheap runs.
- The arXiv engine self-throttles to 1 request / 3 s. Semantic Scholar may return 429; it is skipped
  gracefully.
- Set the `GITHUB_TOKEN` env (already wired) so GitHub search uses 30 req/min instead of 10.
