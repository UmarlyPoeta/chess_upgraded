from utils.pieces import King, Queen, Rook, Bishop, Knight, Pawn
from termcolor import colored, cprint

class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [["." for _ in range(8)] for _ in range(8)]
        # Place pieces for both players
        for i in range(8):
            board[1][i] = Pawn("black")
            board[6][i] = Pawn("white")
        list_pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(list_pieces):
            board[0][i] = piece("black")
            board[7][i] = piece("white")
        return board

    def display(self):
        cprint("  a b c d e f g h", "red")
        for i, row in enumerate(self.board):
            row_display = []
            for piece in row:
                if piece == ".":
                    row_display.append(".")
                else:
                    color = "white" if piece.color == "white" else "grey"
                    attrs = ["bold"] if piece.color == "white" else []
                    row_display.append(colored(piece.symbol.upper() if piece.color == "black" else piece.symbol.lower(), color, attrs=attrs))
            cprint((colored(f"{8 - i} ", "red") + " ".join(row_display) + colored(f" {8 - i}", "red")), "white")
        cprint("  a b c d e f g h", "red")
