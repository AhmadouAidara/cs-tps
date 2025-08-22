from __future__ import annotations
from typing import Any, Optional, Iterable, List
from algo.tp1_hash_tables.implementations import Container  

class HashTableContainer(Container):
    """Separate-chaining hash table with a fixed number of buckets (lists)."""
    def __init__(self, m: int = 1024, data: Iterable[Any] = ()) -> None:
        self._m = max(1, int(m))
        self._buckets: List[list[Any]] = [[] for _ in range(self._m)]
        self._n = 0
        for x in data:
            self.add(x)

    def _idx(self, x: Any) -> int:
        return hash(x) % self._m

    def add(self, x: Any) -> None:
        b = self._buckets[self._idx(x)]
        if x not in b:
            b.append(x)
            self._n += 1

    def __contains__(self, x: Any) -> bool:
        return x in self._buckets[self._idx(x)]

    def __len__(self) -> int:
        return self._n

class ResizingHashTableContainer(HashTableContainer):
    """Separate-chaining hash table with automatic resizing by load factor."""
    def __init__(self, m: int = 16, max_load: float = 0.75, data: Iterable[Any] = ()) -> None:
        super().__init__(m=m)
        self._max_load = float(max_load)
        for x in data:
            self.add(x)

    def _load_factor(self) -> float:
        return self._n / self._m

    def _resize(self, new_m: int) -> None:
        old = self._buckets
        self._m = max(1, int(new_m))
        self._buckets = [[] for _ in range(self._m)]
        self._n = 0
        for bucket in old:
            for x in bucket:
                self.add(x)

    def add(self, x: Any) -> None:
        if self._load_factor() > self._max_load:
            self._resize(self._m * 2)
        super().add(x)

class LinkedListHashTableContainer(Container):
    """Separate-chaining hash table using singly linked lists per bucket."""
    class _Node:
        __slots__ = ("key", "next")
        def __init__(self, key: Any, nxt: Optional["LinkedListHashTableContainer._Node"] = None) -> None:
            self.key = key
            self.next = nxt

    def __init__(self, m: int = 1024, data: Iterable[Any] = ()) -> None:
        self._m = max(1, int(m))
        self._heads: list[Optional[LinkedListHashTableContainer._Node]] = [None] * self._m
        self._n = 0
        for x in data:
            self.add(x)

    def _idx(self, x: Any) -> int:
        return hash(x) % self._m

    def add(self, x: Any) -> None:
        i = self._idx(x)
        node = self._heads[i]
        while node:
            if node.key == x:
                return
            node = node.next
        self._heads[i] = LinkedListHashTableContainer._Node(x, self._heads[i])
        self._n += 1

    def __contains__(self, x: Any) -> bool:
        i = self._idx(x)
        node = self._heads[i]
        while node:
            if node.key == x:
                return True
            node = node.next
        return False

    def __len__(self) -> int:
        return self._n