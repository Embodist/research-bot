# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Cursor, pi) working in this repository.

## What this repo is

`research-bot` is a **headless deep-research agent** for frontier tracking in **Embodied AI · VLA ·
Kinematics · C++ · ROS 2**. It adopts the conventions of [`bytedance/deer-flow`](deer-flow/) (a pinned git
submodule): `SKILL.md` skill packages and a lead-agent/sub-agent decomposition. Unlike upstream, the
runtime is intentionally dependency-light (only `httpx` + `PyYAML`) so it runs in GitHub Actions / cron /
containers without Docker, a database or a sandbox.

## Layout

```
src/research_bot/        Python package (the product)
  config.py  llm.py  util.py
  search/    engines.py, router.py, base.py   # multi-source search + RRF
  fetch.py   skills.py  topics.py
  engine.py    # the orchestrator (plan → retrieve → extract → critique → synthesize)
  report.py    # report/*.md + *.json + index.json + push-log.jsonl
  emailer.py   # SMTP delivery
  cli.py       # `rb` management CLI
skills/                  local skills (DeerFlow SKILL.md format)
topics/                  research beats (seed queries + curated catalogues)
config/                  config.example.yaml (tracked), config.yaml (gitignored, secrets)
report/                  generated reports + the push ledger
deer-flow/               upstream submodule (do not edit inside)
tests/                   pytest suite (no network)
.github/workflows/       daily-research.yml, ci.yml
scripts/                 bootstrap.sh, run_daily.sh, import_skill.sh
docs/                    architecture, github-actions, email, skills-and-sources
```

## Commands

```bash
uv venv .venv && uv pip install --python .venv/bin/python -e ".[dev]"
.venv/bin/pytest                       # tests (offline)
.venv/bin/ruff check src tests         # lint
.venv/bin/rb doctor                    # live connectivity + config check
.venv/bin/rb run --topic vla --depth quick
```

## Conventions

- **Python ≥ 3.10**, `from __future__ import annotations`, type hints on public functions.
- Keep runtime dependencies to `httpx` + `PyYAML`. Do not add heavy deps; if unavoidable, put them in an
  optional extra and guard the import.
- **Never raise out of a search engine or the emailer** — degrade and log. `rb doctor` must always print a
  useful report even with no network.
- Add new search engines by subclassing `search.base.Engine` and registering in
  `search.router.ENGINE_REGISTRY`.
- Prompts live inline in `engine.py`; keep the "no fabricated evidence, cite `[n]`, mark `> 待核实`" rules.
- New skills go in `skills/<name>/SKILL.md` with `name` + `description` front-matter.
- New topics go in `topics/<name>.yaml` and must include `seed_queries` + a `seed_resources` catalogue.
- Do not commit secrets. `config/config.yaml`, `.env` and `.venv/` are gitignored.

## Tests

`tests/` must stay offline and deterministic. Network code is exercised only through `rb doctor` / manual
runs. When adding a feature, add a test to the matching module (`test_search.py`, `test_engine.py`, …).

## Updating the submodule

```bash
git -C deer-flow fetch && git -C deer-flow checkout <commit>
git add deer-flow && git commit -m "chore: bump deer-flow submodule"
```

The engine must keep working when the submodule is absent (CI checks out with `submodules: false`).
