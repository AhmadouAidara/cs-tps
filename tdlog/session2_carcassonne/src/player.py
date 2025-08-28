import enum


class Color(enum.Enum):
    """
    The possible colors of a player.
    """

    BLUE = "blue"
    PURPLE = "purple"
    RED = "red"
    YELLOW = "yellow"


COLOR_LETTER = {
    Color.BLUE: "B",
    Color.PURPLE: "P",
    Color.RED: "R",
    Color.YELLOW: "Y",
}


class Player:
    def __init__(self, color: Color, remaining_pawns: int = 8):
        self.remaining_pawns = remaining_pawns
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}({self.color.value}, pawns={self.remaining_pawns})"


class HumanPlayer(Player):
    def __init__(self, color: Color, name: str, remaining_pawns: int = 8):
        super().__init__(color, remaining_pawns)
        self.name = name

    def __str__(self):
        return f"HumanPlayer(name={self.name}, color={self.color.value}, pawns={self.remaining_pawns})"


class AIPlayer(Player):
    def __init__(self, color: Color, difficulty: str, remaining_pawns: int = 8):
        super().__init__(color, remaining_pawns)
        if difficulty not in {"easy", "hard"}:
            raise ValueError("difficulty must be in 'easy' or 'hard'")
        self.difficulty = difficulty

    def __str__(self):
        return f"AIPlayer(color={self.color.value}, difficulty={self.difficulty}, pawns={self.remaining_pawns})"


class RandomPlayer(Player):
    def __init__(self, color: Color, remaining_pawns: int = 8):
        super().__init__(color, remaining_pawns)

    def __str__(self):
        return f"RandomPlayer(color={self.color.value}, pawns={self.remaining_pawns})"
