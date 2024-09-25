import unittest
from src.utils.valid_moves import bishop_valid_move
from src.utils.chess_board import ChessBoard


class TestBishopValidMove(unittest.TestCase):

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

    def test_bishop_move_diagonally_no_obstacles(self):
        self.board.board[0][0] = "B"
        self.assertTrue(bishop_valid_move((0, 0), (3, 3), self.board))

    def test_bishop_move_diagonally_with_obstacles(self):
        self.board.board[0][0] = "B"
        self.board.board[1][1] = "P"
        self.assertFalse(bishop_valid_move((0, 0), (3, 3), self.board))

    def test_bishop_invalid_horizontal_move(self):
        self.board.board[0][0] = "B"
        self.assertFalse(bishop_valid_move((0, 0), (0, 3), self.board))

    def test_bishop_invalid_vertical_move(self):
        self.board.board[0][0] = "B"
        self.assertFalse(bishop_valid_move((0, 0), (3, 0), self.board))

    def test_bishop_capture_opponent_piece(self):
        self.board.board[0][0] = "B"
        self.board.board[3][3] = "p"
        self.assertTrue(bishop_valid_move((0, 0), (3, 3), self.board))

    def test_bishop_invalid_move_blocked_by_same_color(self):
        self.board.board[0][0] = "B"
        self.board.board[3][3] = "P"
        self.assertFalse(bishop_valid_move((0, 0), (3, 3), self.board))


if __name__ == "__main__":
    unittest.main()
