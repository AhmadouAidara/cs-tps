from tdlog.session2_carcassonne.src.game import Game
from tdlog.session2_carcassonne.src.player import HumanPlayer, AIPlayer, Color
from tdlog.session2_carcassonne.src.board import Board


def test_game_init_and_turns():
    players = [
        HumanPlayer(Color.BLUE, name="A"),
        AIPlayer(Color.RED, difficulty="easy"),
    ]
    g = Game(players, Board())
    assert g.remaining_tiles() == 36
    assert g.current_player().color == Color.BLUE

    tile = g.draw_tile()
    assert tile is not None
    g.place_current_tile(0, 0)
    g.next_player()
    assert g.current_player().color == Color.RED


def test_game_deck_runs_out():
    players = [HumanPlayer(Color.YELLOW, name="Y")]
    g = Game(players, Board())
    while g.remaining_tiles():
        g.draw_tile()
        g.place_current_tile(0, 0)
    assert g.is_over()
