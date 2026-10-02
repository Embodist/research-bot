SHELL := bash
RB ?= .venv/bin/rb
PY ?= .venv/bin/python
TOPIC ?= vla
DEPTH ?= standard
REPO ?= $(shell git config --get remote.origin.url 2>/dev/null | sed -E 's#(git@|https://)github.com[:/]##; s#\.git$$##')

.PHONY: help install test lint fmt doctor run run-all topics skills report clean secrets schedule ci

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Create .venv and install research-bot (editable, with dev tools)
	uv venv .venv --python python3
	uv pip install --python $(PY) -e ".[dev]"

test: ## Run the offline test suite
	$(PY) -m pytest -q

lint: ## Lint the package and tests
	$(PY) -m ruff check src tests

fmt: ## Auto-fix lint issues
	$(PY) -m ruff check src tests --fix

doctor: ## Self-check LLM, search engines, skills, topics, email config
	$(RB) doctor

run: ## Run one topic: make run TOPIC=vla DEPTH=quick
	$(RB) run --topic $(TOPIC) --depth $(DEPTH)

run-all: ## Run every topic and email if configured
	$(RB) run --topic all --depth $(DEPTH) --email

topics: ## List topics
	$(RB) topics list

skills: ## List skills (local + deer-flow)
	$(RB) skills list

report: ## List the report/push ledger
	$(RB) report list

secrets: ## Push SMTP/LLM secrets to GitHub Actions (needs GITHUB_TOKEN + pynacl)
	$(PY) scripts/set_github_secrets.py "$(REPO)"

schedule: ## Print a crontab line for a local daily run
	@echo "0 6 * * * cd $(CURDIR) && ./scripts/run_daily.sh >> report/cron.log 2>&1"

clean: ## Remove caches and build artifacts
	rm -rf .pytest_cache .ruff_cache build dist *.egg-info
	find src tests -name __pycache__ -type d -prune -exec rm -rf {} +
