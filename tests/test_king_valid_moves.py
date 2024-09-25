import unittest
from src.utils.valid_moves import king_valid_move
from src.utils.chess_board import ChessBoard


class TestKingValidMove(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard()
        self.board.board = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

    def test_king_move_one_square_vertically(self):
        self.board.board[4][4] = "K"
        self.assertTrue(king_valid_move((4, 4), (5, 4), self.board))

    def test_king_move_one_square_horizontally(self):
        self.board.board[4][4] = "K"
        self.assertTrue(king_valid_move((4, 4), (4, 5), self.board))

    def test_king_move_one_square_diagonally(self):
        self.board.board[4][4] = "K"
        self.assertTrue(king_valid_move((4, 4), (5, 5), self.board))

    def test_king_move_two_squares(self):
        self.board.board[4][4] = "K"
        self.assertFalse(king_valid_move((4, 4), (6, 4), self.board))

    def test_king_move_blocked_by_same_color(self):
        self.board.board[4][4] = "K"
        self.board.board[5][5] = "P"
        self.assertFalse(king_valid_move((4, 4), (5, 5), self.board))

    def test_king_capture_opponent_piece(self):
        self.board.board[4][4] = "K"
        self.board.board[5][5] = "p"
        self.assertTrue(king_valid_move((4, 4), (5, 5), self.board))

    def test_king_invalid_l_shaped_move(self):
        self.board.board[4][4] = "K"
        self.assertFalse(king_valid_move((4, 4), (6, 5), self.board))


if __name__ == "__main__":
    unittest.main()
