from tdlog.session1_road_grid.src.model import Cell, Grid
import random


def random_cell(prob=0.5) -> Cell:
    """Return a Cell where each direction is True with probability `prob`
    (independently)."""
    return Cell(
        north=random.random() < prob,
        south=random.random() < prob,
        east=random.random() < prob,
        west=random.random() < prob,
    )


def random_grid(width, height, prob=0.5) -> Grid:
    """Return a Grid of given dimensions, filled with random cells."""
    grid = Grid(width, height)
    for i in range(height):
        for j in range(width):
            grid.set_cell(i, j, random_cell(prob))
    return grid


def seed_rng(seed: int):
    random.seed(seed)
