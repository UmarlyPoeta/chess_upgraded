from utils.pieces import King, Queen, Rook, Bishop, Knight, Pawn


class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
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
        for row in self.board:
            print(" ".join([str(piece) if piece else "." for piece in row]))
