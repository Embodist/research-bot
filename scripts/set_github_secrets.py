#!/usr/bin/env python3
"""Push repository secrets to GitHub Actions from environment variables.

Usage:
    export GITHUB_TOKEN=ghp_xxx
    export LLM_API_KEY=sk-xxx
    export SMTP_HOST=smtp.qq.com SMTP_PORT=465 SMTP_USER=you@qq.com
    export SMTP_PASS=... SMTP_FROM=you@qq.com MAIL_TO=you@qq.com
    python scripts/set_github_secrets.py Owner/repo

Only variables that are present and non-empty are written. Requires `pynacl`
(`pip install pynacl`). Nothing is written to disk.
"""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.request

SECRET_KEYS = [
    "LLM_API_KEY",
    "SMTP_HOST",
    "SMTP_PORT",
    "SMTP_USER",
    "SMTP_PASS",
    "SMTP_FROM",
    "MAIL_TO",
]


def api(method: str, url: str, token: str, data: dict | None = None) -> tuple[int, str]:
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode()


def main() -> int:
    repo = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_REPOSITORY", "")
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not repo or not token:
        print("usage: GITHUB_TOKEN=... python scripts/set_github_secrets.py Owner/repo", file=sys.stderr)
        return 2
    try:
        from nacl import encoding, public  # type: ignore
    except ImportError:
        print("pynacl is required: pip install pynacl", file=sys.stderr)
        return 2

    base = f"https://api.github.com/repos/{repo}"
    status, body = api("GET", f"{base}/actions/secrets/public-key", token)
    if status != 200:
        print(f"cannot read public key ({status}): {body[:200]}", file=sys.stderr)
        return 1
    key = json.loads(body)
    box = public.SealedBox(public.PublicKey(key["key"].encode(), encoding.Base64Encoder()))

    written = 0
    for name in SECRET_KEYS:
        value = os.environ.get(name, "")
        if not value:
            continue
        encrypted = base64.b64encode(box.encrypt(value.encode())).decode()
        status, body = api(
            "PUT", f"{base}/actions/secrets/{name}", token, {"encrypted_value": encrypted, "key_id": key["key_id"]}
        )
        print(f"  {name:12s} -> {status}")
        written += status in (201, 204)
    print(f"done: {written} secret(s) set on {repo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
