class ChessPiece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.symbol


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
