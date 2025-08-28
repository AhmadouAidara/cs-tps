# tdlog/session2_carcassonne/src/game.py
from __future__ import annotations
from typing import List, Optional
import random

from .board import Board
from .player import Player
from .deck import make_tiles
from .tile import Tile


class Game:
    """
    Minimal game state:
      - players: ordered list of Player
      - board: growing Board
      - draw_pile: list[Tile] (shuffled)
      - turn_index: int
      - current_tile: Optional[Tile]
    """

    def __init__(self, players: List[Player], board: Optional[Board] = None) -> None:
        if not players:
            raise ValueError("Game needs at least one player.")
        colors = [p.color for p in players]
        if len(set(colors)) != len(colors):
            raise ValueError("Each player must have a unique color.")

        self.players = players
        self.board = board or Board()

        self.draw_pile: List[Tile] = make_tiles()
        random.shuffle(self.draw_pile)

        self.turn_index: int = 0
        self.current_tile: Optional[Tile] = None

    # --- turn helpers ---
    def current_player(self) -> Player:
        return self.players[self.turn_index]

    def next_player(self) -> Player:
        self.turn_index = (self.turn_index + 1) % len(self.players)
        return self.current_player()

    # --- deck / tiles ---
    def draw_tile(self) -> Optional[Tile]:
        self.current_tile = self.draw_pile.pop() if self.draw_pile else None
        return self.current_tile

    def place_current_tile(self, i: int, j: int) -> None:
        if self.current_tile is None:
            raise ValueError("No tile to place. Call draw_tile() first.")
        self.board[i, j] = self.current_tile
        self.current_tile = None

    # --- queries ---
    def remaining_tiles(self) -> int:
        return len(self.draw_pile)

    def is_over(self) -> bool:
        return self.current_tile is None and not self.draw_pile
