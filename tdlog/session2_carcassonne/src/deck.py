# tdlog/session2_carcassonne/src/deck.py
from itertools import combinations
from typing import List

from .tile import Tile, Link, Side
from .player import Color


# Paires utilitaires
CONSECUTIVE = (
    (Side.NORTH, Side.EAST),
    (Side.EAST, Side.SOUTH),
    (Side.SOUTH, Side.WEST),
    (Side.WEST, Side.NORTH),
)
OPPOSITE = (
    (Side.NORTH, Side.SOUTH),
    (Side.EAST, Side.WEST),
)


def make_tiles() -> List[Tile]:
    """
    Construit le paquet de tuiles conformément à l’énoncé :
      - 4 tuiles sans lien
      - 8 tuiles (2 par couleur) avec un lien entre côtés consécutifs
      - 12 tuiles (3 par couleur) avec un lien entre côtés opposés
      - 12 tuiles (2 par combinaison de 2 couleurs) avec deux liens entre côtés consécutifs
    Total attendu : 36 tuiles.
    """
    tiles: List[Tile] = []

    # 1) 4 tuiles vides
    tiles += [Tile([]) for _ in range(4)]

    # 2) 8 tuiles : 2 par couleur, lien consécutif (on fixe N-E pour rester simple)
    for color in (Color.BLUE, Color.PURPLE, Color.RED, Color.YELLOW):
        tiles.append(Tile([Link(Side.NORTH, Side.EAST, color)]))
        tiles.append(Tile([Link(Side.NORTH, Side.EAST, color)]))

    # 3) 12 tuiles : 3 par couleur, lien opposé (on fixe N-S pour rester simple)
    for color in (Color.BLUE, Color.PURPLE, Color.RED, Color.YELLOW):
        tiles.append(Tile([Link(Side.NORTH, Side.SOUTH, color)]))
        tiles.append(Tile([Link(Side.NORTH, Side.SOUTH, color)]))
        tiles.append(Tile([Link(Side.NORTH, Side.SOUTH, color)]))

    # 4) 12 tuiles : 2 par combinaison de 2 couleurs, deux liens consécutifs
    # Combinaisons de 2 couleurs parmi 4 => C(4,2) = 6; 6 * 2 = 12
    # On utilise deux paires consécutives disjointes : (N-E) et (S-W)
    for c1, c2 in combinations((Color.BLUE, Color.PURPLE, Color.RED, Color.YELLOW), 2):
        tiles.append(
            Tile(
                [
                    Link(Side.NORTH, Side.EAST, c1),
                    Link(Side.SOUTH, Side.WEST, c2),
                ]
            )
        )
        tiles.append(
            Tile(
                [
                    Link(Side.NORTH, Side.EAST, c1),
                    Link(Side.SOUTH, Side.WEST, c2),
                ]
            )
        )

    # Sanity check
    assert len(tiles) == 36, f"Expected 36 tiles, got {len(tiles)}"
    return tiles
