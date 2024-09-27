class King:
    def __init__(self, color):
        self.color = color
        self.symbol = "K" if self.color == "black" else "k"


class Queen():
    def __init__(self, color):
        self.color = color
        self.symbol = "Q" if self.color == "black" else "q"


class Rook():
    def __init__(self, color):
        self.color = color
        self.symbol = "R" if self.color == "black" else "r"


class Bishop():
    def __init__(self, color):
        self.color = color
        self.symbol = "B" if self.color == "black" else "b"


class Knight():
    def __init__(self, color):
        self.color = color
        self.symbol = "N" if self.color == "black" else "n"


class Pawn():
    def __init__(self, color):
        self.color = color
        self.symbol = "P" if self.color == "black" else "p"
