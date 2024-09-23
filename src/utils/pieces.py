from termcolor import colored


class ChessPiece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return (
            colored(self.symbol, "blue")
            if self.color == "white"
            else colored(self.symbol, "red")
        )


class King(ChessPiece):
    symbol = "K"


class Queen(ChessPiece):
    symbol = "Q"


class Rook(ChessPiece):
    symbol = "R"


class Bishop(ChessPiece):
    symbol = "B"


class Knight(ChessPiece):
    symbol = "N"


class Pawn(ChessPiece):
    symbol = "P"
