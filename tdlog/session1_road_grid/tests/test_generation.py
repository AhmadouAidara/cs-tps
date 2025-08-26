from tdlog.session1_road_grid.src.gen_random import random_cell, random_grid, seed_rng


def test_random_cell_all_true():
    seed_rng(42)
    c = random_cell(1.0)
    assert (
        c.connections.north
        and c.connections.south
        and c.connections.east
        and c.connections.west
    )


def test_random_cell_all_false():
    seed_rng(42)
    c = random_cell(0.0)
    assert not (
        c.connections.north
        or c.connections.south
        or c.connections.east
        or c.connections.west
    )


def test_random_grid_shape():
    g = random_grid(4, 3)
    assert len(g.grid) == 3
    assert len(g.grid[0]) == 4
