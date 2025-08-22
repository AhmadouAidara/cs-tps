from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Any

class Container(ABC):
    """Contract: set-like container supporting add, membership and length."""

    @abstractmethod
    def add(self, x: Any) -> None: ...

    @abstractmethod
    def __contains__(self, x: Any) -> bool: ...

    @abstractmethod
    def __len__(self) -> int: ...

class ListContainer(Container):
    """Baseline container backed by a Python list (O(n) membership)."""
    def __init__(self, data: Iterable[Any] = ()) -> None:
        self._lst: list[Any] = []
        for x in data:
            if x not in self._lst:
                self._lst.append(x)

    def add(self, x: Any) -> None:
        if x not in self._lst:
            self._lst.append(x)

    def __contains__(self, x: Any) -> bool:
        return x in self._lst

    def __len__(self) -> int:
        return len(self._lst)

class SetContainer(Container):
    """Baseline container backed by a Python set (avg O(1) membership)."""
    def __init__(self, data: Iterable[Any] = ()) -> None:
        self._s: set[Any] = set(data)

    def add(self, x: Any) -> None:
        self._s.add(x)

    def __contains__(self, x: Any) -> bool:
        return x in self._s

    def __len__(self) -> int:
        return len(self._s)