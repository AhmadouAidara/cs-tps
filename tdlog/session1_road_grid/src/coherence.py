from tdlog.session1_road_grid.src.model import Cell, Grid
import random

# Opposites + deltas (utiles partout)
OPPOSITE = {"north": "south", "south": "north", "east": "west", "west": "east"}
DELTA = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}


def is_coherent(grid: Grid) -> bool:
    """True iff every declared connection has a reciprocal
    connection on the neighbor (borders ignored)."""
    h, w = grid.height, grid.width
    for i in range(h):
        for j in range(w):
            cell = grid.get_cell(i, j).connections
            for dir_ in ("north", "south", "west", "east"):
                if not getattr(cell, dir_):
                    continue
                di, dj = DELTA[dir_]
                ni, nj = i + di, j + dj
                if not grid.in_bounds(ni, nj):  # bords ignorés
                    continue
                if not getattr(grid.get_cell(ni, nj).connections, OPPOSITE[dir_]):
                    return False
    return True


def random_coherent_grid(width: int, height: int, prob: float = 0.5) -> Grid:
    """
    Generate a coherent grid: every connection between two adjacent
    cells is mutual (reciprocal). Border connections are allowed
    but ignored in coherence checks.
    """
    grid = Grid(width, height)

    for i in range(height):
        for j in range(width):
            # valeurs par défaut
            north = south = east = west = False

            # Contraintes depuis le voisin du haut
            if i > 0:
                if grid.get_cell(i - 1, j).connections.south:
                    north = True

            # Contraintes depuis le voisin de gauche
            if j > 0:
                if grid.get_cell(i, j - 1).connections.east:
                    west = True

            # Tirage aléatoire pour sud (si pas au bord)
            if i < height - 1:
                south = random.random() < prob

            # Tirage aléatoire pour est (si pas au bord)
            if j < width - 1:
                east = random.random() < prob

            # Créer et placer la cellule
            cell = Cell(north=north, south=south, east=east, west=west)
            grid.set_cell(i, j, cell)

            # Propager immédiatement la réciprocité si possible
            if east and j + 1 < width:
                neighbor = grid.get_cell(i, j + 1)
                grid.set_cell(
                    i,
                    j + 1,
                    Cell(
                        north=neighbor.connections.north,
                        south=neighbor.connections.south,
                        east=neighbor.connections.east,
                        west=True,  # réciprocité
                    ),
                )
            if south and i + 1 < height:
                neighbor = grid.get_cell(i + 1, j)
                grid.set_cell(
                    i + 1,
                    j,
                    Cell(
                        north=True,  # réciprocité
                        south=neighbor.connections.south,
                        east=neighbor.connections.east,
                        west=neighbor.connections.west,
                    ),
                )

    return grid
