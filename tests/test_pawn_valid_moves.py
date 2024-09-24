import unittest
from src.utils.chess_board import ChessBoard
from src.utils.valid_moves import pawn_valid_move


class TestPawnValidMove(unittest.TestCase):

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

    def test_pawn_move_forward_one_square(self):
        self.board.board[6][4] = "P"
        self.assertTrue(pawn_valid_move((6, 4), (5, 4), self.board))

    def test_pawn_move_forward_two_squares_from_start(self):
        self.board.board[6][4] = "P"
        self.assertTrue(pawn_valid_move((6, 4), (4, 4), self.board))

    def test_pawn_move_forward_two_squares_not_from_start(self):
        self.board.board[5][4] = "P"
        self.assertFalse(pawn_valid_move((5, 4), (3, 4), self.board))

    def test_pawn_capture_diagonally(self):
        self.board.board[6][4] = "P"
        self.board.board[5][5] = "p"
        self.assertTrue(pawn_valid_move((6, 4), (5, 5), self.board))

    def test_pawn_invalid_move_sideways(self):
        self.board.board[6][4] = "P"
        self.assertFalse(pawn_valid_move((6, 4), (6, 5), self.board))

    def test_pawn_invalid_move_backward(self):
        self.board.board[5][4] = "P"
        self.assertFalse(pawn_valid_move((5, 4), (6, 4), self.board))


if __name__ == "__main__":
    unittest.main()
