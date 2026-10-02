"""research_bot — headless deep-research agent for robotics frontier tracking.

The package is intentionally dependency-light (httpx + PyYAML) so that it can run
head-less in CI, cron and containers. It borrows the *skill* convention and the
lead-agent / sub-agent decomposition idea from bytedance/deer-flow, which is
vendored as a git submodule under ``deer-flow/``.
"""

from __future__ import annotations

__version__ = "0.1.0"

__all__ = ["__version__"]
