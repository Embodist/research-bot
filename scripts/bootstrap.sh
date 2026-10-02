#!/usr/bin/env bash
# Bootstrap a fresh checkout: submodule (mirror-aware), venv, install, config.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "==> research-bot bootstrap in $REPO_ROOT"

# --- 1. deer-flow submodule (optional at runtime, but part of the product) ----
if [ ! -e deer-flow/AGENTS.md ]; then
  echo "==> fetching deer-flow submodule"
  if ! git submodule update --init --depth 1 deer-flow 2>/dev/null; then
    echo "!! direct github clone failed; retrying through ghfast.top mirror"
    git -c url."https://ghfast.top/https://github.com/".insteadOf="https://github.com/" \
      submodule update --init --depth 1 deer-flow
  fi
else
  echo "==> deer-flow submodule already present"
fi

# --- 2. Python environment ---------------------------------------------------
PYTHON_BIN="${PYTHON:-python3}"
if command -v uv >/dev/null 2>&1; then
  echo "==> creating venv with uv"
  uv venv .venv --python "$PYTHON_BIN"
  uv pip install --python .venv/bin/python -e ".[dev]"
  RB=".venv/bin/rb"
else
  echo "==> creating venv with python -m venv"
  "$PYTHON_BIN" -m venv .venv
  ./.venv/bin/python -m pip install --upgrade pip
  ./.venv/bin/python -m pip install -e ".[dev]"
  RB=".venv/bin/rb"
fi

# --- 3. Config ---------------------------------------------------------------
if [ ! -f config/config.yaml ]; then
  echo "==> creating config/config.yaml from example"
  cp config/config.example.yaml config/config.yaml
else
  echo "==> config/config.yaml already exists"
fi

echo
echo "==> done. Next steps:"
echo "    export LLM_API_KEY=...        # or edit config/config.yaml"
echo "    $RB doctor"
echo "    $RB run --topic vla"
