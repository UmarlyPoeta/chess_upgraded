import unittest
from src.utils.valid_moves import queen_valid_move
from src.utils.chess_board import ChessBoard


class TestQueenValidMove(unittest.TestCase):

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

    def test_queen_move_vertically_no_obstacles(self):
        self.board.board[0][0] = "Q"
        self.assertTrue(queen_valid_move((0, 0), (7, 0), self.board))

    def test_queen_move_horizontally_no_obstacles(self):
        self.board.board[0][0] = "Q"
        self.assertTrue(queen_valid_move((0, 0), (0, 7), self.board))

    def test_queen_move_diagonally_no_obstacles(self):
        self.board.board[0][0] = "Q"
        self.assertTrue(queen_valid_move((0, 0), (7, 7), self.board))

    def test_queen_move_vertically_with_obstacles(self):
        self.board.board[0][0] = "Q"
        self.board.board[3][0] = "P"
        self.assertFalse(queen_valid_move((0, 0), (7, 0), self.board))

    def test_queen_move_horizontally_with_obstacles(self):
        self.board.board[0][0] = "Q"
        self.board.board[0][3] = "P"
        self.assertFalse(queen_valid_move((0, 0), (0, 7), self.board))

    def test_queen_move_diagonally_with_obstacles(self):
        self.board.board[0][0] = "Q"
        self.board.board[3][3] = "P"
        self.assertFalse(queen_valid_move((0, 0), (7, 7), self.board))

    def test_queen_invalid_l_shaped_move(self):
        self.board.board[0][0] = "Q"
        self.assertFalse(queen_valid_move((0, 0), (2, 1), self.board))

    def test_queen_capture_opponent_piece(self):
        self.board.board[0][0] = "Q"
        self.board.board[7][7] = "p"
        self.assertTrue(queen_valid_move((0, 0), (7, 7), self.board))

    def test_queen_invalid_move_blocked_by_same_color(self):
        self.board.board[0][0] = "Q"
        self.board.board[7][7] = "P"
        self.assertFalse(queen_valid_move((0, 0), (7, 7), self.board))


if __name__ == "__main__":
    unittest.main()
