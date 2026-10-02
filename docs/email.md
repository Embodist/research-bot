# Email delivery

Reports are delivered over SMTP with **implicit TLS (465)** or **STARTTLS (587)**. The email contains the
full report rendered as HTML, plus the original Markdown as an attachment. Every attempt (success or
failure) is recorded in `report/index.json` and appended to `report/push-log.jsonl`.

## Configure

Either edit `config/config.yaml`:

```yaml
email:
  enabled: true
  smtp_host: smtp.qq.com
  smtp_port: 465
  smtp_ssl: true
  username: you@qq.com
  password: <smtp-auth-code>
  from: you@qq.com
  to: [you@qq.com, teammate@example.com]
  subject_prefix: "[Research Bot]"
  attach_report: true
  digest: false
```

or provide the environment variables (used automatically in CI):

```bash
export SMTP_HOST=smtp.qq.com SMTP_PORT=465 SMTP_USER=you@qq.com SMTP_PASS=***
export SMTP_FROM=you@qq.com MAIL_TO="you@qq.com,teammate@example.com"
export EMAIL_ENABLED=1
```

Then:

```bash
rb run --topic vla --email                 # send normally
rb run --topic vla --dry-run-email         # render + log, do not connect
rb run --topic all --no-email              # skip delivery
```

## Digest vs per-topic

- `email.digest: false` (default) → one email per topic.
- `email.digest: true` → a single merged email for all topics of the run (fewer messages).

## Provider cheat-sheet

| Provider | Host | Port | Mode |
| --- | --- | --- | --- |
| QQ Mail | `smtp.qq.com` | 465 | SSL (needs an auth code, not the login password) |
| 163 Mail | `smtp.163.com` | 465 | SSL (auth code) |
| Gmail | `smtp.gmail.com` | 587 | STARTTLS (app password) |
| Outlook | `smtp.office365.com` | 587 | STARTTLS |
| Aliyun DirectMail | `smtpdm.aliyun.com` | 465 | SSL |

Set `smtp_ssl: false` for 587/STARTTLS.

## Verifying

```bash
rb doctor          # prints: email enabled=<bool> configured=<bool> to=[...]
```

`configured=True` requires host + username + password + from + at least one recipient.

## Push ledger

```
report/push-log.jsonl
{"ts":"2026-10-02T22:03:11+00:00","id":"2026-10-02-vla","topic":"vla",
 "report_path":"report/2026/10/2026-10-02-vla.md",
 "email":{"sent":true,"to":["you@example.com"],"ts":"...","error":null,"dry_run":false}}
```

`report/index.json` mirrors the latest delivery state per report under its `email` key.
