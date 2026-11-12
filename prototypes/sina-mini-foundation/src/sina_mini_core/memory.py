"""Memory contracts and a volatile adapter for local tests only."""
from __future__ import annotations

from typing import Any


class InMemoryMemoryStore:
    """Non-persistent test adapter. Data is lost when the process exits."""

    def __init__(self) -> None:
        self._items: dict[tuple[str, str], Any] = {}

    async def get(self, namespace: str, key: str) -> Any | None:
        return self._items.get((namespace, key))

    async def put(self, namespace: str, key: str, value: Any) -> None:
        if not namespace or not key:
            raise ValueError("namespace and key must be non-empty")
        self._items[(namespace, key)] = value
