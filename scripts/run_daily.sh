#!/usr/bin/env bash
# Daily driver for cron / systemd timers / manual runs.
#
#   ./scripts/run_daily.sh                 # all topics, standard depth, email if configured
#   TOPICS="vla ros2" DEPTH=deep ./scripts/run_daily.sh
#   ./scripts/run_daily.sh --no-email
#
# Environment:
#   TOPICS (default: all)   DEPTH (quick|standard|deep, default: standard)
#   RB (default: .venv/bin/rb, falls back to rb on PATH)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

RB="${RB:-.venv/bin/rb}"
command -v "$RB" >/dev/null 2>&1 || RB="rb"

TOPICS="${TOPICS:-all}"
DEPTH="${DEPTH:-standard}"
mkdir -p report

LOG="report/run-$(date -u +%Y%m%dT%H%M%SZ).log"
echo "==> $(date -u +%FT%TZ) starting: topics=$TOPICS depth=$DEPTH" | tee -a "$LOG"

ARGS=(--topic "$TOPICS" --depth "$DEPTH")
if [ "${1:-}" != "--no-email" ] && [ "${EMAIL_ENABLED:-1}" = "1" ]; then
  ARGS+=(--email)
fi

set +e
"$RB" run "${ARGS[@]}" 2>&1 | tee -a "$LOG"
STATUS=${PIPESTATUS[0]}
set -e
echo "==> finished with status $STATUS; log: $LOG"
exit "$STATUS"
