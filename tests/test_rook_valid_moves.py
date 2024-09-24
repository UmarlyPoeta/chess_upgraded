import unittest
from src.utils.valid_moves import rook_valid_move
from src.utils.chess_board import ChessBoard


class TestRookValidMove(unittest.TestCase):

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

    def test_rook_move_vertically_no_obstacles(self):
        self.board.board[0][0] = "R"
        self.assertTrue(rook_valid_move((0, 0), (7, 0), self.board))

    def test_rook_move_horizontally_no_obstacles(self):
        self.board.board[0][0] = "R"
        self.assertTrue(rook_valid_move((0, 0), (0, 7), self.board))

    def test_rook_move_vertically_with_obstacles(self):
        self.board.board[0][0] = "R"
        self.board.board[3][0] = "P"
        self.assertFalse(rook_valid_move((0, 0), (7, 0), self.board))

    def test_rook_move_horizontally_with_obstacles(self):
        self.board.board[0][0] = "R"
        self.board.board[0][3] = "P"
        self.assertFalse(rook_valid_move((0, 0), (0, 7), self.board))

    def test_rook_invalid_diagonal_move(self):
        self.board.board[0][0] = "R"
        self.assertFalse(rook_valid_move((0, 0), (7, 7), self.board))

    def test_rook_capture_opponent_piece(self):
        self.board.board[0][0] = "R"
        self.board.board[7][0] = "p"
        self.assertTrue(rook_valid_move((0, 0), (7, 0), self.board))

    def test_rook_invalid_move_blocked_by_same_color(self):
        self.board.board[0][0] = "R"
        self.board.board[7][0] = "P"
        self.assertFalse(rook_valid_move((0, 0), (7, 0), self.board))


if __name__ == "__main__":
    unittest.main()
