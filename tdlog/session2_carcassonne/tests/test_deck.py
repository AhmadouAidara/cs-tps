from tdlog.session2_carcassonne.src.deck import make_tiles
from tdlog.session2_carcassonne.src.tile import Side
from tdlog.session2_carcassonne.src.player import Color


def test_deck_count_and_distribution():
    tiles = make_tiles()
    assert len(tiles) == 36

    # 4 empty tiles
    empty = [t for t in tiles if len(t.links) == 0]
    assert len(empty) == 4

    # 8 consecutive (N-E), 2 per color
    consec_ne = [
        t
        for t in tiles
        if len(t.links) == 1 and set(t.links[0].sides) == {Side.NORTH, Side.EAST}
    ]
    assert len(consec_ne) == 8
    for c in (Color.BLUE, Color.PURPLE, Color.RED, Color.YELLOW):
        assert sum(1 for t in consec_ne if t.links[0].color == c) == 2

    # 12 opposite (N-S), 3 per color
    opp_ns = [
        t
        for t in tiles
        if len(t.links) == 1 and set(t.links[0].sides) == {Side.NORTH, Side.SOUTH}
    ]
    assert len(opp_ns) == 12
    for c in (Color.BLUE, Color.PURPLE, Color.RED, Color.YELLOW):
        assert sum(1 for t in opp_ns if t.links[0].color == c) == 3

    # 12 double links (N-E) & (S-W)
    doubles = [t for t in tiles if len(t.links) == 2]
    assert len(doubles) == 12
    for t in doubles:
        side_sets = [set(link.sides) for link in t.links]
        assert {Side.NORTH, Side.EAST} in side_sets
        assert {Side.SOUTH, Side.WEST} in side_sets
