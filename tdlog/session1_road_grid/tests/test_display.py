from tdlog.session1_road_grid.src.model import Cell, Grid
from tdlog.session1_road_grid.src.display import render_cell, render_grid


def test_render_cell_dimensions():
    # p, q contrôlent la largeur ; r, s contrôlent la hauteur
    p, q, r, s = 2, 1, 2, 1
    canvas = render_cell(Cell(), p, q, r, s)  # list[list[str]]
    rows = 2 * r + s
    cols = 2 * p + q

    assert isinstance(canvas, list)
    assert len(canvas) == rows
    assert all(isinstance(row, list) for row in canvas)
    assert all(len(row) == cols for row in canvas)


def test_render_cell_north_only_band_positions():
    p, q, r, s = 2, 1, 2, 1
    # north=True uniquement
    canvas = render_cell(Cell(north=True), p, q, r, s)
    rows = 2 * r + s
    mid_cols = range(p, p + q)
    for row in range(0, r + s):
        for col in mid_cols:
            assert canvas[row][col] == "#"

    for row in range(r + s, rows):
        for col in mid_cols:
            assert canvas[row][col] == " "


def test_render_grid_1x2_horizontal_continuity():
    # Deux cellules côte à côte : gauche->east, droite->west
    p, q, r, s = 2, 1, 2, 1
    g = Grid(width=2, height=1)
    g.set_cell(0, 0, Cell(east=True))
    g.set_cell(0, 1, Cell(west=True))

    big = render_grid(g, p, q, r, s)  # str
    lines = big.splitlines()

    cols = 2 * p + q
    row_idx = r
    line = lines[row_idx]
    assert line[cols - 1] == "#"
    assert line[cols] == "#"


def test_render_grid_2x1_vertical_continuity():
    # Deux cellules empilées : haut->south, bas->north
    p, q, r, s = 2, 1, 2, 1
    g = Grid(width=1, height=2)
    g.set_cell(0, 0, Cell(south=True))
    g.set_cell(1, 0, Cell(north=True))

    big = render_grid(g, p, q, r, s)
    lines = big.splitlines()

    rows = 2 * r + s
    col_idx = p

    assert lines[rows - 1][col_idx] == "#"
    assert lines[rows][col_idx] == "#"
