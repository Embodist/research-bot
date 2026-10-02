# Base image for research-bot.
#
# Only Python + the (tiny) runtime/dev dependencies are baked in. The application
# code is NOT copied in — it is checked out and mounted at run time. So this image
# only needs rebuilding when dependencies change, not on every code edit.
#
#   python:3.12-slim matches the version the daily workflow runs.
#   Runtime deps: httpx + PyYAML (see pyproject.toml); dev tools: pytest + ruff.
#   hatchling is preinstalled so the editable install at run time is fully offline.
FROM python:3.12-slim

# git: the engine commits reports back to the repo; ca-certificates for HTTPS.
RUN apt-get update \
 && apt-get install -y --no-install-recommends git ca-certificates \
 && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir --upgrade pip \
 && python -m pip install --no-cache-dir \
      "httpx>=0.27" "PyYAML>=6.0" \
      "pytest>=8.0" "ruff>=0.6" \
      hatchling editables

# Required by GHCR to associate the published package with this repository.
LABEL org.opencontainers.image.source="https://github.com/Embodist/research-bot" \
      org.opencontainers.image.title="research-bot-base" \
      org.opencontainers.image.description="Base image for research-bot: Python 3.12 + httpx/PyYAML/pytest/ruff/hatchling. App code is mounted at run time."

# Default cwd for local `docker run -v "$PWD":/app`. CI overrides it with the
# checkout workspace, so nothing here depends on the code being present.
WORKDIR /app

# No ENTRYPOINT/CMD: this is a base image, consumers run `rb ...` explicitly.
