"""Configuration loading: defaults <- config file <- environment overrides."""

from __future__ import annotations

import copy
import os
import re
from pathlib import Path
from typing import Any

import yaml

# Allow ${VAR} and ${VAR:-default} inside string values.
_ENV_RE = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(?::-([^}]*))?\}")

_HOME_MARKERS = ("topics", "skills")


class DotDict(dict):
    """A dict whose keys are also reachable as attributes (recursively)."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__()
        self.update(*args, **kwargs)

    def update(self, *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        for key, value in dict(*args, **kwargs).items():
            dict.__setitem__(self, key, _wrap(value))

    def __getattr__(self, item: str) -> Any:  # pragma: no cover - trivial
        try:
            return self[item]
        except KeyError as exc:  # pragma: no cover
            raise AttributeError(item) from exc

    def __setattr__(self, key: str, value: Any) -> None:  # pragma: no cover
        self[key] = _wrap(value)

    def get_path(self, dotted: str, default: Any = None) -> Any:
        node: Any = self
        for part in dotted.split("."):
            if isinstance(node, dict) and part in node:
                node = node[part]
            else:
                return default
        return node


def _wrap(value: Any) -> Any:
    if isinstance(value, dict) and not isinstance(value, DotDict):
        return DotDict({k: _wrap(v) for k, v in value.items()})
    if isinstance(value, list):
        return [_wrap(v) for v in value]
    return value


DEFAULTS: dict[str, Any] = {
    "llm": {
        "base_url": "${LLM_BASE_URL:-https://api.deepseek.com/v1}",
        "api_key": "${LLM_API_KEY:-}",
        "model": "${LLM_MODEL:-deepseek-v4-flash}",
        "fallback_models": ["${LLM_MODEL_FALLBACK:-deepseek-flash}"],
        "temperature": 0.3,
        "max_tokens": 8192,
        "max_tokens_report": "${LLM_MAX_TOKENS_REPORT:-16384}",
        "timeout": 240,
        "max_retries": 3,
        "tiers": {"fast": "${LLM_MODEL_FAST:-deepseek-v4-flash}", "strong": "${LLM_MODEL_STRONG:-deepseek-v4-flash}"},
    },
    "search": {
        "engines": [
            "arxiv",
            "openalex",
            "crossref",
            "semantic_scholar",
            "github",
            "bing",
            "sogou",
            "so360",
            "searxng",
        ],
        "searxng_url": "${SEARXNG_URL:-http://43.155.145.78:58881}",
        "github_token": "${GITHUB_TOKEN:-}",
        "max_results_per_engine": 8,
        "timeout": 20,
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
        ),
        "fetch_pages": True,
        "fetch_top_n": 4,
        "fetch_timeout": 20,
        "max_page_chars": 6000,
    },
    "research": {
        "depth": "standard",
        "max_subquestions": 6,
        "max_rounds": 2,
        "results_per_subquestion": 6,
        "candidates_for_ranking": 24,
        "language": "bilingual",
        "recency_days": 540,
        "skills": ["deep-research", "frontier-tracking", "paper-survey", "evidence-grading"],
    },
    "report": {
        "dir": "report",
        "formats": ["md", "json"],
        "keep_latest": True,
        "include_raw_sources": True,
    },
    "email": {
        "enabled": False,
        "smtp_host": "${SMTP_HOST:-}",
        "smtp_port": "${SMTP_PORT:-465}",
        "smtp_ssl": True,
        "username": "${SMTP_USER:-}",
        "password": "${SMTP_PASS:-}",
        "from": "${SMTP_FROM:-}",
        "to": [],
        "subject_prefix": "[Research Bot]",
        "attach_report": True,
        "digest": False,
    },
}


def find_home(start: Path | None = None) -> Path:
    """Locate the repository root (the dir containing ``topics/`` and ``skills/``)."""
    env = os.environ.get("RESEARCH_BOT_HOME")
    if env and Path(env).is_dir():
        return Path(env).resolve()
    here = (start or Path.cwd()).resolve()
    for base in [here, *here.parents]:
        if all((base / m).exists() for m in _HOME_MARKERS):
            return base
    # Fall back to the checkout that contains this package (editable installs).
    pkg_root = Path(__file__).resolve().parents[2]
    if all((pkg_root / m).exists() for m in _HOME_MARKERS):
        return pkg_root
    return here


def expand_env(value: Any) -> Any:
    if isinstance(value, str):

        def repl(match: re.Match[str]) -> str:
            name, default = match.group(1), match.group(2)
            got = os.environ.get(name)
            # POSIX `:-` semantics: empty counts as missing.
            if got is None or got == "":
                return default if default is not None else ""
            return got

        return _ENV_RE.sub(repl, value)
    if isinstance(value, dict):
        return {k: expand_env(v) for k, v in value.items()}
    if isinstance(value, list):
        return [expand_env(v) for v in value]
    return value


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(base)
    for key, value in (override or {}).items():
        if key in out and isinstance(out[key], dict) and isinstance(value, dict):
            out[key] = deep_merge(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


def load_config(path: str | os.PathLike[str] | None = None, home: Path | None = None) -> tuple[DotDict, Path]:
    """Load config, returning ``(config, home)``.

    Resolution order: explicit ``path`` or ``$RESEARCH_BOT_CONFIG``, then
    ``<home>/config/config.yaml``. Missing file is fine — defaults are used.
    """
    home = home or find_home()
    candidate: Path | None = None
    if path:
        candidate = Path(path)
    elif os.environ.get("RESEARCH_BOT_CONFIG"):
        candidate = Path(os.environ["RESEARCH_BOT_CONFIG"])
    else:
        candidate = home / "config" / "config.yaml"

    data: dict[str, Any] = {}
    if candidate and candidate.is_file():
        with candidate.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
    merged = deep_merge(DEFAULTS, data)

    # CI convenience: MAIL_TO="a@x.com,b@y.com" seeds the recipient list so a
    # workflow only needs to provide secrets, not a config file.
    mail_to = os.environ.get("MAIL_TO", "")
    if mail_to and not merged.get("email", {}).get("to"):
        merged.setdefault("email", {})["to"] = [x.strip() for x in mail_to.split(",") if x.strip()]
    if os.environ.get("EMAIL_ENABLED", "").lower() in ("1", "true", "yes"):
        merged.setdefault("email", {})["enabled"] = True
    if os.environ.get("EMAIL_DIGEST", "").lower() in ("1", "true", "yes"):
        merged.setdefault("email", {})["digest"] = True

    return _wrap(expand_env(merged)), home
