#!/usr/bin/env bash
# Import a SKILL.md into skills/<name>/ from a URL or a local path.
#
#   scripts/import_skill.sh https://github.com/OWNER/REPO/blob/main/skills/foo/SKILL.md
#   scripts/import_skill.sh --name my-skill https://raw.githubusercontent.com/OWNER/REPO/main/SKILL.md
#   scripts/import_skill.sh deer-flow/skills/public/deep-research/SKILL.md
#
# github.com blob URLs are rewritten to raw URLs; if direct raw.githubusercontent.com
# is blocked, it retries through the ghfast.top mirror.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME=""
SRC="${1:-}"

if [ "${1:-}" = "--name" ]; then
  NAME="${2:-}"
  SRC="${3:-}"
fi
if [ -z "$SRC" ]; then
  echo "usage: $0 [--name NAME] <url-or-path>" >&2
  exit 2
fi

TMP="$(mktemp)"
cleanup() { rm -f "$TMP"; }
trap cleanup EXIT

download() {
  local url="$1"
  if curl -fsSL --retry 2 -m 60 -A "Mozilla/5.0" "$url" -o "$TMP"; then
    return 0
  fi
  # mirror fallback for github-hosted content
  case "$url" in
    https://raw.githubusercontent.com/*)
      curl -fsSL --retry 2 -m 60 -A "Mozilla/5.0" "https://ghfast.top/$url" -o "$TMP" ;;
    https://github.com/*)
      curl -fsSL --retry 2 -m 60 -A "Mozilla/5.0" "https://ghfast.top/$url" -o "$TMP" ;;
    *)
      return 1 ;;
  esac
}

if [ -f "$SRC" ]; then
  cp "$SRC" "$TMP"
else
  url="$SRC"
  # github.com/OWNER/REPO/blob/BRANCH/path -> raw
  if [[ "$url" == https://github.com/*/blob/* ]]; then
    url="$(printf '%s' "$url" | sed -E 's#https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.*)#https://raw.githubusercontent.com/\1/\2/\3/\4#')"
  fi
  echo "==> downloading $url"
  download "$url" || { echo "!! download failed: $SRC" >&2; exit 1; }
fi

# Resolve the skill name: --name > frontmatter name > "imported".
if [ -z "$NAME" ]; then
  NAME="$(awk 'NR==1 && $0=="---"{f=1;next} f && /^name:/{sub(/^name:[[:space:]]*/,"");gsub(/["'"'"']/,"");print;exit}' "$TMP")"
fi
[ -z "$NAME" ] && NAME="imported"
NAME="$(printf '%s' "$NAME" | tr ' ' '-' | tr -cd '[:alnum:]_-')"

DEST="$REPO_ROOT/skills/$NAME"
mkdir -p "$DEST"
cp "$TMP" "$DEST/SKILL.md"
echo "==> installed skill '$NAME' -> $DEST/SKILL.md"
head -5 "$DEST/SKILL.md"
