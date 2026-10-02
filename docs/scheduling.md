# Scheduling the daily research

## GitHub Actions (recommended)

The default: [`.github/workflows/daily-research.yml`](../.github/workflows/daily-research.yml) runs daily at
`22:00 UTC` (06:00 Asia/Shanghai), commits the reports back and emails the digest.

```
Actions → Daily Research → Run workflow   # manual, optional topic/depth/send_email
```

Required setup (once):

```bash
export GITHUB_TOKEN=ghp_...            # repo + workflow scope
export LLM_API_KEY=sk-...              # already set for this repo
export SMTP_HOST=smtp.qq.com SMTP_PORT=465 SMTP_USER=you@qq.com
export SMTP_PASS=... SMTP_FROM=you@qq.com MAIL_TO="you@qq.com"
python scripts/set_github_secrets.py Embodist/research-bot
#   or:  make secrets
```

Change the cron in the workflow to move the run. GitHub cron is **always UTC**:

| Desired local time (Asia/Shanghai) | cron |
| --- | --- |
| 06:00 | `0 22 * * *` |
| 08:00 | `0 0 * * *` |
| 09:30 | `30 1 * * *` |

## Local cron / systemd timer

```bash
# install once
./scripts/bootstrap.sh
export LLM_API_KEY=...
export SMTP_HOST=... SMTP_USER=... SMTP_PASS=... SMTP_FROM=... MAIL_TO=...

# test
./scripts/run_daily.sh

# crontab entry (06:00 daily), logs under report/
make schedule
# 0 6 * * * cd /path/to/research-bot && ./scripts/run_daily.sh >> report/cron.log 2>&1
```

Put the environment variables in `config/config.yaml` (gitignored) so cron does not need a shell profile.

### systemd timer alternative

`/etc/systemd/system/research-bot.service`

```ini
[Unit]
Description=research-bot daily deep research
After=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/path/to/research-bot
EnvironmentFile=/path/to/research-bot/.env
ExecStart=/path/to/research-bot/scripts/run_daily.sh
```

`/etc/systemd/system/research-bot.timer`

```ini
[Unit]
Description=Run research-bot daily at 06:00

[Timer]
OnCalendar=*-*-* 06:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl enable --now research-bot.timer
```

## Cost / runtime budget

- `quick` ≈ 3–5 sub-questions, 1 round → ~5–10 min/topic.
- `standard` ≈ 5–6 sub-questions, 2 rounds → ~10–20 min/topic.
- `deep` ≈ 8 sub-questions, 3 rounds → ~25–40 min/topic.

For a daily run across all 5 topics, `standard` is a good default; use `--depth quick` for a low-cost
watchlist and reserve `deep` for manual runs.
