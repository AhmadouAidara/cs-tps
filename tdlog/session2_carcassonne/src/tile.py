import enum
from .player import Color
from typing import Optional, Tuple


class Side(enum.Enum):
    """
    The four possible sides of a tile.
    """

    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


class Link:
    """
    A link connects two sides and may carry a color (meeple).
    """

    def __init__(self, side1: Side, side2: Side, color: Optional[Color] = None):
        # ordre stable (N < E < S < W) pour éviter que (N,E) et (E,N) soient différents
        order = {Side.NORTH: 0, Side.EAST: 1, Side.SOUTH: 2, Side.WEST: 3}
        if order[side1] <= order[side2]:
            self.sides: Tuple[Side, Side] = (side1, side2)
        else:
            self.sides: Tuple[Side, Side] = (side2, side1)
        self.color: Optional[Color] = color

    def __str__(self):
        c = self.color.name[0] if self.color else "-"
        return f"{self.sides[0].name}-{self.sides[1].name}:{c}"


class Tile:
    """
    A tile can have 0, 1, or 2 links.
    """

    def __init__(self, links: Optional[list[Link]] = None):
        self.links: list[Link] = links or []

    def is_empty(self) -> bool:
        return len(self.links) == 0

    def rotate_clockwise(self) -> "Tile":
        """
        Return a new tile rotated 90° clockwise.
        """
        mapping = {
            Side.NORTH: Side.EAST,
            Side.EAST: Side.SOUTH,
            Side.SOUTH: Side.WEST,
            Side.WEST: Side.NORTH,
        }
        new_links = [
            Link(mapping[l.sides[0]], mapping[l.sides[1]], l.color) for l in self.links
        ]
        return Tile(new_links)

    def rotate_counterclockwise(self) -> "Tile":
        """
        Return a new tile rotated 90° counterclockwise.
        """
        mapping = {
            Side.NORTH: Side.WEST,
            Side.WEST: Side.SOUTH,
            Side.SOUTH: Side.EAST,
            Side.EAST: Side.NORTH,
        }
        new_links = [
            Link(mapping[l.sides[0]], mapping[l.sides[1]], l.color) for l in self.links
        ]
        return Tile(new_links)

    def __str__(self) -> str:
        if self.is_empty():
            return "Tile(empty)"
        return "Tile(" + ", ".join(str(l) for l in self.links) + ")"
