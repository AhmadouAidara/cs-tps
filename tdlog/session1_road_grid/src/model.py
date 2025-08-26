import collections

Connections = collections.namedtuple("Connections", ["north", "south", "east", "west"])


class Cell:
    def __init__(
        self,
        north: bool = False,
        south: bool = False,
        east: bool = False,
        west: bool = False,
    ):
        self.connections = Connections(north, south, east, west)


class Grid:
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self.grid: list[list[Cell]] = self.empty_grid(self.width, self.height)

    def empty_grid(self, width: int, height: int) -> list[list[Cell]]:
        return [[Cell() for _ in range(width)] for _ in range(height)]

    def in_bounds(self, i: int, j: int) -> bool:
        return 0 <= i < self.height and 0 <= j < self.width

    def neighbors(self, i: int, j: int) -> list[tuple[int, int]]:
        assert self.in_bounds(i, j), "Cell indices out of bounds"
        neighbors = []
        if self.grid[i][j].connections.south:
            if self.in_bounds(i + 1, j):
                neighbors.append((i + 1, j))
        if self.grid[i][j].connections.north:
            if self.in_bounds(i - 1, j):
                neighbors.append((i - 1, j))
        if self.grid[i][j].connections.east:
            if self.in_bounds(i, j + 1):
                neighbors.append((i, j + 1))
        if self.grid[i][j].connections.west:
            if self.in_bounds(i, j - 1):
                neighbors.append((i, j - 1))
        return neighbors

    def get_cell(self, i: int, j: int) -> Cell:
        return self.grid[i][j]

    def set_cell(self, i: int, j: int, cell: Cell) -> None:
        if 0 <= i < self.height and 0 <= j < self.width:
            self.grid[i][j] = cell
        else:
            raise IndexError("Index out of the grid")

    def set_connection(self, i: int, j: int, direction: str, value: bool) -> None:
        if not self.in_bounds(i, j):
            raise IndexError("Index out of the grid")
        if direction not in {"north", "south", "east", "west"}:
            raise ValueError("Direction must be in: north,south,east,west")
        cell = self.grid[i][j]
        conn = cell.connections._replace(**{direction: value})
        self.grid[i][j] = Cell(conn.north, conn.south, conn.east, conn.west)


__all__ = ["Cell", "Grid", "Connections"]
