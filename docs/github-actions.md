# Daily automation with GitHub Actions

The workflow is [`.github/workflows/daily-research.yml`](../.github/workflows/daily-research.yml). It:

1. checks out the repo (**without** the submodule — the engine works without it),
2. installs `research-bot` on Python 3.12,
3. runs `rb doctor` (non-fatal preflight, logged),
4. runs `rb run --topic <topic> --depth <depth> [--email]`,
5. commits `report/` back to the repo,
6. uploads the Markdown/JSON reports + `push-log.jsonl` as a build artifact.

## Configure secrets

**Settings → Secrets and variables → Actions**.

### Secrets

| Secret | Required | Notes |
| --- | --- | --- |
| `LLM_API_KEY` | yes | whnetsea / OpenAI-compatible key |
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
| `LLM_BASE_URL` | `https://api.whnetsea.com/v1` | OpenAI-compatible base URL |
| `SEARXNG_URL` | `http://43.155.145.78:58881` | your SearXNG (JSON or HTML) |

## Schedule

```yaml
on:
  schedule:
    - cron: "0 22 * * *"   # 22:00 UTC = 06:00 Asia/Shanghai
```

GitHub cron is always UTC. Also runnable on demand from the **Actions → Daily Research → Run workflow**
button, with inputs `topic`, `depth` and `send_email`.

## Commit-back permissions

The workflow requests `permissions: contents: write` and pushes as
`github-actions[bot]`. If your default branch is protected, allow GitHub Actions to bypass the branch
protection rule or push to a dedicated reports branch.

## Manual run

```bash
gh workflow run daily-research.yml -f topic=vla -f depth=deep -f send_email=true
```

## Rate limits & cost notes

- `rb run --topic all` performs ~5 topics × 3–8 sub-questions × (search + fetch + 2–4 LLM calls). On the
  default `standard` depth this is roughly 30–60 LLM calls per topic; use `--depth quick` for cheap runs.
- The arXiv engine self-throttles to 1 request / 3 s. Semantic Scholar may return 429; it is skipped
  gracefully.
- Set the `GITHUB_TOKEN` env (already wired) so GitHub search uses 30 req/min instead of 10.
