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
        def piece_to_unicode(piece):
            if piece is None:
                return "."
            unicode_pieces = {
                "King": {"white": "♔", "black": "♚"},
                "Queen": {"white": "♕", "black": "♛"},
                "Rook": {"white": "♖", "black": "♜"},
                "Bishop": {"white": "♗", "black": "♝"},
                "Knight": {"white": "♘", "black": "♞"},
                "Pawn": {"white": "♙", "black": "♟"},
            }
            return unicode_pieces[type(piece).__name__][piece.color]

        files = "abcdefgh"
        ranks = "87654321"

        print("  " + " ".join(files))
        for row in range(8):
            print(ranks[row], end=" ")
            for col in range(8):
                piece = self.board[row][col]
                print(piece_to_unicode(piece), end=" ")
            print(ranks[row])
        print("  " + " ".join(files))
