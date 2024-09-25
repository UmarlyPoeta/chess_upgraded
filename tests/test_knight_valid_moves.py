import unittest
from src.utils.valid_moves import knight_valid_move


class MockChessBoard:
    def __init__(self, board):
        self.board = board


class TestKnightValidMove(unittest.TestCase):

    def setUp(self):
        self.empty_board = MockChessBoard([["." for _ in range(8)] for _ in range(8)])

    def test_knight_valid_move_L_shape(self):
        self.assertTrue(knight_valid_move((0, 0), (2, 1), self.empty_board))
        self.assertTrue(knight_valid_move((0, 0), (1, 2), self.empty_board))
        self.assertTrue(knight_valid_move((4, 4), (6, 5), self.empty_board))
        self.assertTrue(knight_valid_move((4, 4), (5, 6), self.empty_board))

    def test_knight_invalid_move_not_L_shape(self):
        self.assertFalse(knight_valid_move((0, 0), (3, 3), self.empty_board))
        self.assertFalse(knight_valid_move((4, 4), (4, 6), self.empty_board))
        self.assertFalse(knight_valid_move((4, 4), (6, 6), self.empty_board))
        self.assertFalse(knight_valid_move((4, 4), (3, 5), self.empty_board))

    def test_knight_valid_move_edge_cases(self):
        self.assertTrue(knight_valid_move((7, 7), (5, 6), self.empty_board))
        self.assertTrue(knight_valid_move((7, 7), (6, 5), self.empty_board))
        self.assertFalse(knight_valid_move((7, 7), (7, 5), self.empty_board))
        self.assertFalse(knight_valid_move((7, 7), (5, 7), self.empty_board))


if __name__ == "__main__":
    unittest.main()
