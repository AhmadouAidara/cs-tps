# tdlog/session2_carcassonne/src/display.py
from __future__ import annotations
from typing import List
from tile import Tile, Side
from player import COLOR_LETTER

TileCanvas = List[List[str]]  # 5 rows x 9 cols


def _blank_canvas() -> TileCanvas:
    rows, cols = 5, 9
    canvas = [[" " for _ in range(cols)] for _ in range(rows)]
    # cadre
    for c in range(cols):
        canvas[0][c] = "-" if 0 < c < cols - 1 else "+"
        canvas[rows - 1][c] = "-" if 0 < c < cols - 1 else "+"
    for r in range(rows):
        canvas[r][0] = "|" if 0 < r < rows - 1 else canvas[r][0]
        canvas[r][cols - 1] = "|" if 0 < r < rows - 1 else canvas[r][cols - 1]
    # “plots” de route sur les bords (comme l’énoncé)
    canvas[0][4] = "#"
    canvas[rows - 1][4] = "#"
    canvas[2][0] = "#"
    canvas[2][cols - 1] = "#"
    return canvas


def _midpoint(side: Side) -> tuple[int, int]:
    # (row, col) du milieu de chaque côté
    return {
        Side.NORTH: (0, 4),
        Side.SOUTH: (4, 4),
        Side.WEST: (2, 0),
        Side.EAST: (2, 8),
    }[side]


def _draw_path_to_center(canvas: TileCanvas, side: Side) -> None:
    """Trace des # depuis le milieu du côté jusqu'au centre (2,4)."""
    r, c = _midpoint(side)
    # centre
    cr, cc = 2, 4
    # avancer pas à pas vers le centre
    while r != cr:
        r += 1 if r < cr else -1
        canvas[r][c] = "#"
    while c != cc:
        c += 1 if c < cc else -1
        canvas[r][c] = "#"


def render_tile(tile: Tile) -> TileCanvas:
    """
    Retourne un canvas 5x9 (liste de listes de caractères) représentant la tuile.
    Règles :
    - cadre + plots '#'
    - pour chaque lien, on trace des '#' jusqu'au centre
    - 1 lien  -> lettre couleur au centre (2,4)
    - 2 liens -> lettres aux positions (2,3) et (2,5)
    """
    canvas = _blank_canvas()

    # tracer les routes
    for link in tile.links:
        a, b = link.sides
        _draw_path_to_center(canvas, a)
        _draw_path_to_center(canvas, b)

    # placer les lettres (si couleur présente)
    letters = []
    for link in tile.links:
        if link.color is not None:
            letters.append(COLOR_LETTER[link.color])

    if len(letters) == 1:
        canvas[2][4] = letters[0]
    elif len(letters) >= 2:
        # deux lettres de part et d’autre du centre (cohérent avec les exemples)
        canvas[2][3] = letters[0]
        canvas[2][5] = letters[1]

    return canvas


def render_tile_str(tile: Tile) -> str:
    """Version string (avec sauts de ligne) d'une tuile."""
    canvas = render_tile(tile)
    return "\n".join("".join(row) for row in canvas)


def render_board(board) -> str:
    """
    Assemble l’affichage 5x9 de chaque tuile du board.
    Les cases None sont affichées comme tuile vide (cadre + plots).
    """
    rows, cols = board.size()
    # rendre chaque case en canvas
    line_buffer: List[str] = []
    for i in range(rows):
        row_canvases: List[TileCanvas] = []
        for j in range(cols):
            t = board[i, j]
            if t is None:
                row_canvases.append(_blank_canvas())
            else:
                row_canvases.append(render_tile(t))
        # assembler verticalement (5 lignes)
        for r in range(5):
            line_buffer.append("".join("".join(canvas[r]) for canvas in row_canvases))
    return "\n".join(line_buffer)
