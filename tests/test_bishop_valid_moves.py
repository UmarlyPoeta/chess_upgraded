import unittest
from src.utils.valid_moves import bishop_valid_move
from src.utils.chess_board import ChessBoard
from src.utils.pieces import Bishop, Pawn


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
        self.board.board[0][0] = Bishop("black")
        self.assertTrue(bishop_valid_move((0, 0), (3, 3), self.board))

    def test_bishop_move_diagonally_with_obstacles(self):
        self.board.board[0][0] = Bishop("black")
        self.board.board[1][1] = Bishop("black")
        self.assertFalse(bishop_valid_move((0, 0), (3, 3), self.board))

    def test_bishop_invalid_horizontal_move(self):
        self.board.board[0][0] = Bishop("black")
        self.assertFalse(bishop_valid_move((0, 0), (0, 3), self.board))

    def test_bishop_invalid_vertical_move(self):
        self.board.board[0][0] = Bishop("black")
        self.assertFalse(bishop_valid_move((0, 0), (3, 0), self.board))

    def test_bishop_capture_opponent_piece(self):
        self.board.board[0][0] = Bishop("black")
        self.board.board[3][3] = Pawn("white")
        self.assertTrue(bishop_valid_move((0, 0), (3, 3), self.board))

    def test_bishop_invalid_move_blocked_by_same_color(self):
        self.board.board[0][0] = Bishop("black")
        self.board.board[3][3] = Bishop("black")
        self.assertFalse(bishop_valid_move((0, 0), (3, 3), self.board))


if __name__ == "__main__":
    unittest.main()
