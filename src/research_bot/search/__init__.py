"""Search subsystem: engine registry + RRF fusion router."""

from __future__ import annotations

from .base import Engine, SearchResult
from .router import ENGINE_REGISTRY, SearchRouter, rrf_fuse

__all__ = ["Engine", "SearchResult", "SearchRouter", "ENGINE_REGISTRY", "rrf_fuse"]
