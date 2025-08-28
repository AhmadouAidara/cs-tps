import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from tdlog.session2_carcassonne.src.board import Board
from tdlog.session2_carcassonne.src.tile import Tile


def test_board_init_and_getset():
    b = Board(2, 3)
    assert b.size() == (2, 3)
    assert b[0, 0] is None
    b[1, 2] = Tile([])
    assert b[1, 2] is not None


def test_board_auto_expand_on_borders():
    b = Board(1, 1)
    # poser sur (0,0) agrandit avant (ligne) et avant (colonne)
    b[0, 0] = Tile([])
    rows, cols = b.size()
    assert rows == 2 and cols == 2

    # poser sur dernière colonne agrandit après (colonne)
    b[1, cols - 1] = Tile([])
    rows2, cols2 = b.size()
    assert rows2 == rows and cols2 == cols + 1

    # poser sur dernière ligne agrandit après (ligne)
    b[rows2 - 1, 0] = Tile([])
    rows3, cols3 = b.size()
    assert rows3 == rows2 + 1 and cols3 == cols2


def test_board_prevents_overwrite():
    b = Board(1, 1)
    b[0, 0] = Tile([])
    # la case (1,1) existe après agrandissement: elle est vide
    b[1, 1] = Tile([])  # ok
    try:
        b[1, 1] = Tile([])  # reposer au même endroit doit lever
        assert False, "Expected ValueError on occupied cell"
    except ValueError:
        pass
