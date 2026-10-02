"""Search result model and engine base class."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str = ""
    engine: str = ""
    kind: str = "web"  # web | paper | project | dataset | news
    published: str | None = None
    authors: list[str] = field(default_factory=list)
    venue: str | None = None
    citations: int | None = None
    stars: int | None = None
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class Engine:
    """Base class for a search backend."""

    name: str = "engine"
    kind: str = "web"

    def __init__(self, cfg: Any) -> None:
        self.cfg = cfg

    def available(self) -> bool:
        return True

    def search(self, query: str, limit: int) -> list[SearchResult]:  # pragma: no cover - interface
        raise NotImplementedError
