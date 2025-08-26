from tdlog.session1_road_grid.src.model import Cell, Grid


def render_cell(cell: Cell, p: int, q: int, r: int, s: int) -> list[list[str]]:
    # Dimensions du bloc cellule (cf. schéma)
    rows = 2 * r + s
    cols = 2 * p + q

    # Canvas rempli d'espaces
    canvas = [[" " for _ in range(cols)] for _ in range(rows)]

    # Bandes centrales (verticale et horizontale)
    mid_rows = range(r, r + s)  # bande horizontale (hauteur s)
    mid_cols = range(p, p + q)  # bande verticale (largeur q)

    conn = cell.connections

    # NORTH: bande verticale du haut jusqu'au centre (inclus)
    if conn.north:
        for row in range(0, r + s):
            for col in mid_cols:
                canvas[row][col] = "#"

    # SOUTH: bande verticale du centre jusqu'en bas (inclus)
    if conn.south:
        for row in range(r, rows):
            for col in mid_cols:
                canvas[row][col] = "#"

    # WEST: bande horizontale de la gauche jusqu'au centre (inclus)
    if conn.west:
        for col in range(0, p + q):
            for row in mid_rows:
                canvas[row][col] = "#"

    # EAST: bande horizontale du centre jusqu'à droite (inclus)
    if conn.east:
        for col in range(p, cols):
            for row in mid_rows:
                canvas[row][col] = "#"

    # Conversion en lignes de texte
    return canvas


def render_grid(grid: Grid, p: int, q: int, r: int, s: int):
    lines = []
    rows = 2 * r + s
    for i in range(grid.height):
        block_row = [
            render_cell(grid.get_cell(i, j), p, q, r, s) for j in range(grid.width)
        ]
        for k in range(rows):
            line_k = "".join("".join(bloc[k]) for bloc in block_row)
            lines.append(line_k)
    return "\n".join(lines)
