# tdlog/session2_carcassonne/src/board.py
from __future__ import annotations
from typing import Optional, List, Tuple
from .tile import Tile


class Board:
    def __init__(self, rows: int = 1, cols: int = 1) -> None:
        assert rows >= 1 and cols >= 1
        self.rows = rows
        self.cols = cols
        self.grid: List[List[Optional[Tile]]] = [
            [None for _ in range(cols)] for _ in range(rows)
        ]

    def size(self) -> Tuple[int, int]:
        return self.rows, self.cols

    def in_bounds(self, i: int, j: int) -> bool:
        return 0 <= i < self.rows and 0 <= j < self.cols

    def __getitem__(self, key: tuple[int, int]) -> Optional[Tile]:
        i, j = key
        if not self.in_bounds(i, j):
            raise IndexError(f"indices hors limites: ({i}, {j})")
        return self.grid[i][j]

    def _add_row_before(self) -> None:
        self.grid.insert(0, [None] * self.cols)
        self.rows += 1

    def _add_row_after(self) -> None:
        self.grid.append([None] * self.cols)
        self.rows += 1

    def _add_col_before(self) -> None:
        for r in self.grid:
            r.insert(0, None)
        self.cols += 1

    def _add_col_after(self) -> None:
        for r in self.grid:
            r.append(None)
        self.cols += 1

    def __setitem__(self, key: tuple[int, int], value: Tile) -> None:
        i, j = key
        if value is None:
            raise ValueError("tile cannot be None")

        # ---------- BEFORE expansions ----------
        # Ligne : on ajoute AVANT si i == 0
        if i == 0:
            self._add_row_before()
            # i reste 0

        # Colonne : on ajoute AVANT uniquement au tout premier coin (0,0)
        if i == 0 and j == 0:
            self._add_col_before()
            # j reste 0

        # ---------- AFTER expansions (recalculés après les BEFORE) ----------
        add_row_after = i == self.rows - 1
        add_col_after = j == self.cols - 1

        # Coin bas-droit : si on est aussi en dernière colonne, on ne rajoute pas de ligne après
        if add_col_after:
            add_row_after = False

        if add_row_after:
            self._add_row_after()
        if add_col_after:
            self._add_col_after()

        # ---------- Pose avec contrôles ----------
        if not self.in_bounds(i, j):
            raise IndexError(f"target index out of bounds after expand: ({i}, {j})")

        if self.grid[i][j] is not None:
            raise ValueError(f"cell ({i},{j}) already occupied")

        self.grid[i][j] = value

    def display(self) -> str:
        # vue debug simple
        lines = []
        for i in range(self.rows):
            row = "".join(
                "T" if self.grid[i][j] is not None else "·" for j in range(self.cols)
            )
            lines.append(row)
        return "\n".join(lines)
