# Architecture

`research-bot` is the **headless lead agent** for a robotics research beat. It is deliberately small
(`httpx` + `PyYAML`) so it can run in GitHub Actions, cron or a container without Docker/DB/sandbox
dependencies, while reusing the conventions of [`bytedance/deer-flow`](../deer-flow) (vendored as a
submodule).

## Pipeline

```
topic.yaml ──► PLAN ──► ┌─ per sub-question: RETRIEVE ── RANK ── FETCH ── EXTRACT ─┐ ──► CRITIQUE ──┐
                         └──────────────── (parallel, round 1..N) ────────────────┘              │
                                                    ▲────────────────── gap-filling round ────────┘
                                                                                                 │
   references ◄── SourceRegistry (stable [n]) ◄── SYNTHESIZE ◄──────────────────────────────────┘
                                                    │
                                    report/*.md + *.json + index.json + push-log.jsonl
                                                    │
                                                 EMAIL (SMTP)
```

| Stage | Module | What it does |
| --- | --- | --- |
| Plan | `engine.DeepResearchEngine.plan` | topic + extra query → 3–8 sub-questions with search queries and preferred engines |
| Retrieve | `search.router.SearchRouter` | fan out every enabled engine in parallel, RRF-fuse, de-duplicate |
| Rank | `engine._rank_results` | source preference × kind × recency × citations/stars |
| Fetch | `fetch.fetch_many` | read the top-N pages, HTML→text |
| Extract | `engine.extract` | LLM turns candidates into graded, cited findings (JSON) |
| Critique | `engine.critique` | coverage gaps → extra queries/sub-questions (bounded by `max_rounds`) |
| Synthesize | `engine.synthesize` | cited Markdown report in the topic's required structure |
| Persist | `report.save_report` | `report/YYYY/MM/DD-<topic>.md` + `.json`, `index.json`, `push-log.jsonl` |
| Notify | `emailer.send_report` / `send_digest` | SMTP TLS/STARTTLS, HTML body + `.md` attachment |

## Key invariants

- **Citations are stable.** `SourceRegistry` assigns each unique normalised URL a global number once.
  Extraction and synthesis both reference those numbers, so `[n]` in the prose matches the reference list.
- **No fabricated evidence.** Prompts forbid inventing papers/URLs; synthesis may only cite numbers in the
  provided list. Insufficient evidence must be written as `> 待核实`.
- **Graceful degradation.** LLM down → deterministic source-grounded report; engine blocked → dropped;
  page fetch fails → snippet-only extraction; no network at all → topic seed catalogue only.
- **Bounded work.** `max_subquestions`, `max_rounds`, `results_per_subquestion`, `candidates`,
  `fetch_top_n` cap every fan-out.

## Modules

| Path | Responsibility |
| --- | --- |
| `src/research_bot/config.py` | defaults ← YAML ← env (`${VAR:-default}`, `MAIL_TO`) |
| `src/research_bot/llm.py` | OpenAI-compatible client, `tiers`, JSON coercion, retries, token stats |
| `src/research_bot/util.py` | HTTP, HTML→text, `extract_json`, URL normalisation, dates |
| `src/research_bot/search/` | engine registry + RRF router |
| `src/research_bot/fetch.py` | concurrent page reader |
| `src/research_bot/skills.py` | DeerFlow-compatible `SKILL.md` loader (local + submodule) |
| `src/research_bot/topics.py` | topic definitions with seed catalogues |
| `src/research_bot/engine.py` | the orchestrator |
| `src/research_bot/report.py` | artifacts + ledger |
| `src/research_bot/emailer.py` | SMTP delivery |
| `src/research_bot/cli.py` | `rb` management tool |

## Why not call DeerFlow's Python harness directly?

The upstream harness is a full LangGraph stack (gateway, sandbox, D1 DDS of middlewares, Kubernetes/E2B
sandboxes, ~80 dependencies). Requiring it would make the daily GitHub Action slow and fragile. Instead we
adopt its **interfaces** — skill packages and the lead-agent/sub-agent model — and keep the runner
dependency-light. The submodule keeps us aligned and lets us reuse every upstream public skill.
