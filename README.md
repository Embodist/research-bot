# research-bot

> A **headless deep-research agent** for frontier tracking in **Embodied AI · VLA · Kinematics · C++ · ROS 2**.
> Built around [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow) (vendored as a git submodule),
> with local skills, a dependency-light orchestrator, multi-source web search, daily email delivery and a
> committed report archive.

`research-bot` runs unattended (cron / GitHub Actions), plans a research question, fans out to academic and
web search backends, fetches and reads the primary sources, extracts graded evidence, critiques its own
coverage, then writes a cited Markdown report — and emails it to you. Every run is recorded under
[`report/`](report/) (`index.json` + `push-log.jsonl`).

> **Status (verified).** The daily GitHub Actions workflow runs green end-to-end **inside the prebuilt
> base image** (`ghcr.io/embodist/research-bot-base:py3.12`)
> ([→ run](https://github.com/Embodist/research-bot/actions)): install → `rb doctor` → research → commit
> reports → upload artifacts. Nine search engines (including your SearXNG) pass the connectivity check;
> 73 offline tests and lint pass. Email delivery (163 → outlook) is configured locally **and** in CI
> (7 Action secrets + 3 variables) and verified working. Every report now carries four evidence axes per
> item — **热度 heat · 权威 authority · 关注度 attention · 推荐度 recommendation** — and retrieval uses a
> distinctive-token relevance gate that drops homonym drift. Beyond batch runs, the pipeline can also be
> driven as an **HTTP service** (`rb serve`, async job API) and through two **cross-domain fixed-skeleton
> modes** — `knowledge` (rigorous 7-facet knowledge map) and `watch` (7-facet increment snapshot) — see below.

---

## Table of contents

- [Why / design](#why--design)
- [Architecture](#architecture)
- [Quick start](#quick-start)
- [Configuration](#configuration)
- [CLI reference](#cli-reference)
- [HTTP service (`rb serve`)](#http-service-rb-serve)
- [Cross-domain knowledge framework](#cross-domain-knowledge-framework)
- [Skills](#skills)
- [Topics](#topics)
- [Search layer](#search-layer)
- [Reports & push ledger](#reports--push-ledger)
- [Daily automation (GitHub Actions)](#daily-automation-github-actions)
- [Docker base image](#docker-base-image)
- [Email setup](#email-setup)
- [DeerFlow integration](#deerflow-integration)
- [Development](#development)
- [Troubleshooting](#troubleshooting)

---

## Why / design

Deep research is not "one search + one prompt". It is: **decompose → retrieve from many sources → read the
primary source → grade the evidence → critique coverage → synthesise with citations**. `research-bot`
implements exactly that loop, borrowing DeerFlow's conventions:

| DeerFlow idea | How research-bot uses it |
| --- | --- |
| Lead agent | `DeepResearchEngine` orchestrates the whole run |
| Sub-agents | one *researcher* per sub-question (search + fetch + extract) |
| Skills (`SKILL.md` + YAML front-matter) | `skills/` here **plus** `deer-flow/skills/public/*`, loaded uniformly |
| Pluggable tools | search engines and the reader are pluggable engines |
| Graceful degradation | every stage falls back (LLM down → source-only report; engine blocked → dropped) |

The runtime is intentionally **dependency-light** (`httpx` + `PyYAML`) so it is reliable in CI, cron and
containers. It does **not** require Docker, a sandbox, a database or the heavy DeerFlow stack — but it
happily lives next to the real DeerFlow submodule and reuses its skills.

## Architecture

```
                       ┌────────────────────────── rb CLI ──────────────────────────┐
                       │  rb run · doctor · skills · topics · report · engines      │
                       └───────────────────────────────┬────────────────────────────┘
                                                       │
                                          ┌────────────▼────────────┐
                                          │  DeepResearchEngine      │
                                          │  (DeerFlow lead-agent)   │
                                          └────────────┬────────────┘
   ┌───────────────┬───────────────────────┬────────────┼───────────────────────┬──────────────────┐
   ▼               ▼                       ▼            ▼                       ▼                  ▼
 planner      researcher ×N            critic       synthesizer            emailer            report store
 decompose    search → rank →          gap check    cited Markdown         SMTP               md + json +
 sub-Qs       fetch full text →        + extra      (skills injected)      digest             index.json +
              extract graded JSON      queries                                            push-log.jsonl
   │               │
   │               └── SearchRouter (parallel, RRF-fused) ──┬── arXiv / OpenAlex / Crossref
   │                                                        ├── Semantic Scholar / GitHub API
   │                                                        └── Bing / Sogou / 360 / SearXNG
   └── skills loader (local skills/ + deer-flow/skills/public/)
```

## Quick start

```bash
git clone --recurse-submodules https://github.com/Embodist/research-bot.git
cd research-bot

# 1) install (any of: uv / pip / venv)
#    On networks where PyPI is slow, use a domestic mirror (fastest here: Huawei):
#    uv:  uv venv .venv && uv pip install --python .venv/bin/python -e .
#    pip: pip install -e . -i https://repo.huaweicloud.com/repository/pypi/simple
uv venv .venv && uv pip install --python .venv/bin/python -e .
#   or: python -m pip install -e .

# 2) configure
cp config/config.example.yaml config/config.yaml
export LLM_API_KEY=...            # DeepSeek API key (or set it in config.yaml)

# 3) self-check (LLM + every search engine + email)
rb doctor

# 4) run one topic
rb run --topic vla --depth standard

# 5) run everything and email it
rb run --topic all --email
```

Outputs land in `report/YYYY/MM/DD-<topic>.md` and `.json`, with the ledger in `report/index.json`.

## Configuration

Config resolution: `--config` → `$RESEARCH_BOT_CONFIG` → `<repo>/config/config.yaml` → built-in defaults.
Strings support `${VAR}` and `${VAR:-default}` expansion from the environment. `rb` also auto-loads
`<repo>/.env` at startup (existing environment variables always win), so you can keep keys and
`LLM_BASE_URL` out of `config.yaml`.

Key knobs (`config/config.example.yaml` is fully commented):

```yaml
llm:
  base_url: ${LLM_BASE_URL:-https://api.deepseek.com/v1}   # DeepSeek official API
  api_key: ${LLM_API_KEY}
  model: deepseek-v4-flash      # DeepSeek's canonical id (alias: deepseek-flash)
  tiers: { fast: deepseek-v4-flash, strong: deepseek-v4-flash }

research:
  depth: standard               # quick | standard | deep
  max_subquestions: 6
  max_rounds: 2                 # 1 = single pass, 2 = one gap-filling round
  language: bilingual           # zh | en | bilingual
  skills: [deep-research, frontier-tracking, paper-survey, evidence-grading]

search:
  engines: [arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng]
  fetch_pages: true

email:
  enabled: false
  # smtp_* + to: [...]
```

> **Model note.** The LLM defaults to the **DeepSeek official API**
> (`https://api.deepseek.com/v1`). `deepseek-v4-flash` is DeepSeek's canonical model id (alias
> `deepseek-flash`), which is the default. Point `llm.base_url` at any OpenAI-compatible gateway and set
> `llm.model` to an id that gateway serves. If the primary model is missing, the client automatically
> retries the ids in `llm.fallback_models`.
>
> **Search note.** A local/remote **SearXNG is used when reachable** (JSON or HTML mode); the other eight
> engines need no keys. Blocked engines are dropped per-run by a circuit breaker, so a restricted network
> degrades instead of failing.

## CLI reference

> `rb` is **this project's own console script** (registered in `pyproject.toml` as
> `rb = "research_bot.cli:main"`), not a third-party dependency — the only runtime deps are `httpx` and
> `PyYAML`. It is exactly equivalent to `python -m research_bot`, so if you prefer, drop the alias and use
> `python -m research_bot <command>` everywhere. (`research-bot` is a longer alias for the same entry point.)

| Command | Purpose |
| --- | --- |
| `rb run [--topic X] [--query "..."] [--knowledge\|--watch] [--depth quick\|standard\|deep] [--rounds N] [--no-fetch] [--email] [--dry-run-email] [--json]` | run the deep-research pipeline (`--knowledge` = 7-facet knowledge map; `--watch` = 7-facet increment snapshot) |
| `rb serve [--host H] [--port P] [--workers N]` | run the HTTP research service (async job API) |
| `rb doctor` | check LLM, every search engine, skills/topics, email config |
| `rb skills [list\|show <name>]` | inspect skills (local + DeerFlow submodule) |
| `rb topics [list\|show <name>]` | inspect research topics and seed resources |
| `rb engines [list\|test] [--query ...]` | inspect / probe the search layer |
| `rb report [list\|show <id>]` | inspect the archive and push ledger |
| `rb config [show\|init\|path] [--force]` | inspect / bootstrap config |

## HTTP service (`rb serve`)

Expose the pipeline over HTTP for **即用即起**: `POST` a free-text `query` (or a `topic` name) plus optional
config overrides → parse it into a config/topic → run deep-research **asynchronously** → poll for the report.
Zero new dependencies (standard-library `http.server`).

```bash
rb serve --host 0.0.0.0 --port 8080 --workers 2     # or: make serve
# or containerised: cp .env.example .env && docker compose up --build

curl -s -XPOST localhost:8080/research -H 'content-type: application/json' \
  -d '{"query":"C++ RAII 的核心思想与边界","mode":"knowledge","depth":"quick"}'
# -> {"job_id":"...","status":"queued"}
curl -s localhost:8080/research/<job_id>/report
```

Endpoints: `GET /healthz`, `GET /topics`, `POST /research`, `GET /research/{id}`, `GET /research/{id}/report`,
`DELETE /research/{id}`. Optional bearer auth via `RESEARCH_BOT_API_TOKEN`. Full reference:
[`docs/service.md`](docs/service.md).

## Cross-domain knowledge framework

Two fixed **7-facet** skeletons turn any domain / concept / theorem / paradigm into a rigorous, closed-loop,
evaluable report, each enforced by its own skill and checked by a deterministic coverage evaluator
(`frame`, `score`, `gaps`, `elements_missing`):

- **`mode=knowledge`** (or `rb run --knowledge`) — *learn a domain*: 定位与背景 · 问题域 · 历史与演进 ·
  核心机制 · 证据与评估 · 实践与生态 · 关联与元层. Skill: `knowledge-framework`.
- **`mode=watch`** (or `rb run --watch`) — *track a domain's change*: 进展与热点 · 工业界与产品 · 蓝海与缺口 ·
  瓶颈与拐点 · 社会·政策·国际 · 资本与生态 · 信号与预测. Skill: `frontier-watch`.

Demonstrated across a C++ idiom (RAII), a math-analysis theorem (中值定理), and embodied-AI world models
(real2sim / sim2real). See [`docs/knowledge-framework.md`](docs/knowledge-framework.md) for the ontology,
the coverage formula, and worked examples.

## Skills

Skills follow DeerFlow's `SKILL.md` format (YAML front-matter `name`/`description` + Markdown body). The
loader merges **local** `skills/` with the submodule's `deer-flow/skills/public/*` (local wins on name
conflict).

| Skill | Role |
| --- | --- |
| `deep-research` | 4-phase methodology (broad → deep → validate → gap) |
| `frontier-tracking` | timeline building, "真前沿四问", watchlists |
| `frontier-watch` | increment-tracking discipline: dated deltas, [R]/[P] uncertainty tags, blue-ocean/inflection facets |
| `paper-survey` | paper graph, taxonomy, citation discipline |
| `evidence-grading` | A–E evidence levels and wording rules |
| `embodied-ai` | simulators, benchmarks, method lineage |
| `vla` | architecture paradigms, model/dataset catalogue |
| `kinematics` | DH vs screw, IK methods, control, libraries |
| `cpp-robotics` | numeric/optimisation libs, real-time C++, build systems |
| `ros2` | distributions, DDS/RMW, executors, ros2_control/Nav2/MoveIt2 |
| `dataset-hunting` | dataset/benchmark audit checklist |
| `report-writing` | report structure and citation format |
| `knowledge-framework` | cross-domain 7-facet knowledge map (learn a domain: background → evolution → mechanism → boundaries → learning path) |

Skills configured in `research.skills` are injected into every planner/researcher/critic/synthesiser prompt.

## Topics

A topic = a standing research beat. Each `topics/<name>.yaml` combines seed queries, target venues, and a
curated seed catalogue (classic papers / projects / datasets) so a useful report is possible even when the
network is restricted. Ships with: `vla`, `embodied-ai`, `kinematics`, `cpp-robotics`, `ros2`,
`cybersecurity`, `ai`, `music-audio`, and embodied sub-directions `embodied-humanoid`,
`embodied-manipulation`, `embodied-world-models`.

Add your own:

```bash
cp topics/vla.yaml topics/my-topic.yaml
# edit name/title/seed_queries/seed_resources
rb topics show my-topic
rb run --topic my-topic
```

## Search layer

All engines run in parallel per query and results are fused with **RRF** (Reciprocal Rank Fusion), then
re-ranked using source preference, recency, citation counts and GitHub stars.

| Engine | Type | Notes |
| --- | --- | --- |
| `arxiv` | API | Atom feed, newest first |
| `openalex` | API | abstracts, citations, venue |
| `crossref` | API | DOIs, published dates |
| `semantic_scholar` | API | citations (gracious on 429) |
| `github` | API | repos, stars, topics (uses `GITHUB_TOKEN` if set) |
| `bing` / `sogou` / `so360` | HTML | broad recall (network-dependent) |
| `searxng` | JSON + HTML | your instance at `http://43.155.145.78:58881`. Its JSON API is disabled, so the engine transparently parses the HTML result page |

Blocked or unavailable engines are skipped automatically (see `rb engines test`). The academic APIs are
preferred for evidence because they return citable metadata.

## Reports & push ledger

```
report/
  index.json          # every run (newest first): topic, title, sources, findings, email status, commit, run URL
  push-log.jsonl      # append-only email delivery audit
  latest/<topic>.md   # newest report per topic
  2026/10/02-vla.md   # dated, cited Markdown report
  2026/10/02-vla.json # full structured record incl. references + per-sub-question extraction
```

`rb report list` prints the ledger; `rb report show <id>` prints a report.

## Daily automation (GitHub Actions)

Workflows:

- **`.github/workflows/daily-research.yml`** — schedules the daily run, commits new reports back to the repo,
  emails the digest, uploads artifacts, and supports manual `workflow_dispatch`. It runs **inside the
  prebuilt base image** below, so no Python/dependency setup happens per run.
- **`.github/workflows/image.yml`** — builds and publishes the base image to GHCR (rebuilds only when
  `Dockerfile`/`pyproject.toml` change).
- **`.github/workflows/ci.yml`** — lint + tests on push/PR.

## Docker base image

`Dockerfile` bakes in **only the environment** (Python 3.12, `git`, `httpx`/`PyYAML`/`pytest`/`ruff`/
`hatchling`/`editables`) — **not the code**. Code is checked out and mounted at run time, so image rebuilds
are needed only when dependencies change.

```bash
# published by the `Base image` workflow
docker run --rm -v "$PWD":/app -w /app -e LLM_API_KEY=... \
  ghcr.io/embodist/research-bot-base:py3.12 \
  sh -c 'pip install -e . --no-deps --no-build-isolation && rb run --topic vla --depth quick'
```

See [docs/github-actions.md](docs/github-actions.md#docker-base-image).

Required repository secrets (**Settings → Secrets and variables → Actions**):

| Secret | Purpose |
| --- | --- |
| `LLM_API_KEY` | DeepSeek / OpenAI-compatible key |
| `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `SMTP_FROM`, `MAIL_TO` | email delivery |
| `GITHUB_TOKEN` | provided automatically; used for higher GitHub API rate limits |

The schedule is `cron: '0 22 * * *'` (22:00 UTC = 06:00 Asia/Shanghai). Edit the cron and the `MAIL_TO`
secret to taste. Trigger manually from the Actions tab with optional `topic` / `depth` inputs.

## Email setup

Set `email.enabled: true` and fill SMTP fields, or just provide the secrets in CI. Supported:

- **Implicit TLS (465)** — `smtp_ssl: true` (default, works with most providers)
- **STARTTLS (587)** — `smtp_ssl: false`

The HTML body is rendered from the Markdown report and the `.md` is attached. `digest: true` merges all
topics of a run into a single email ahead of the scheduled daily reports.

## DeerFlow integration

`deer-flow/` is a **git submodule** pinned to a specific upstream commit (see `git submodule status`).

```bash
git clone --recurse-submodules <this-repo>
# or, in an existing clone:
git submodule update --init --recursive
```

research-bot reuses DeerFlow's **skill format** and its public skills (`deer-flow/skills/public/*`), and
mirrors its lead-agent/sub-agent decomposition. To pull upstream updates:

```bash
git -C deer-flow fetch && git -C deer-flow checkout <commit>
git add deer-flow && git commit -m "chore: bump deer-flow submodule"
```

> If your network blocks `github.com` directly, clone through a mirror, e.g.
> `git -c url."https://ghfast.top/https://github.com/".insteadOf="https://github.com/" submodule update --init deer-flow`.

An optional adapter for driving the real DeerFlow harness programmatically is planned; the current
implementation runs standalone so it stays reliable in CI.

## Development

```bash
make help                 # list all management targets
make install              # uv venv + editable install
make test                 # pytest (offline)
make lint                 # ruff
make doctor               # live connectivity check
make run TOPIC=vla DEPTH=quick
make run-all              # every topic + email
make serve                # HTTP service (HOST=0.0.0.0 PORT=8080 WORKERS=2)
make report               # report/push ledger
make secrets REPO=Owner/repo   # push SMTP/LLM secrets to GitHub Actions
make schedule             # print a crontab line for a local daily run
```

Layout: `src/research_bot/` (package) · `skills/` · `topics/` · `config/` · `report/` · `scripts/` ·
`.github/workflows/`. See [`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md),
[`docs/HANDOVER.md`](docs/HANDOVER.md), [`docs/deep-research.md`](docs/deep-research.md) (tech core +
architecture), [`docs/service.md`](docs/service.md) (HTTP service), [`docs/knowledge-framework.md`](docs/knowledge-framework.md)
(cross-domain knowledge framework), [`docs/architecture.md`](docs/architecture.md),
[`docs/github-actions.md`](docs/github-actions.md), [`docs/email.md`](docs/email.md),
[`docs/scheduling.md`](docs/scheduling.md) and [`docs/skills-and-sources.md`](docs/skills-and-sources.md).

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `model_not_found` | set `llm.model` to an id your gateway serves (`deepseek-v4-flash` is the default) |
| Some engines show `FAIL` in `rb doctor` | expected on restricted networks; the remaining engines still run |
| `searxng not reachable` | start a local SearXNG on `SEARXNG_URL`, or ignore — it is optional |
| Empty report / few sources | widen `search.engines`, set `GITHUB_TOKEN`, or raise `research.max_subquestions` |
| Email not sent | check `rb doctor` → `email configured`, and the SMTP secrets |
| CI submodule checkout fails | the workflow uses `submodules: false`; the engine works without the submodule |

---

MIT licensed. DeerFlow is MIT licensed by its respective authors.
