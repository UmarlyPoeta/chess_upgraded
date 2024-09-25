import unittest
from src.utils.valid_moves import knight_valid_move


class TestKnightValidMove(unittest.TestCase):

    def test_knight_valid_move_L_shape(self):
        self.assertTrue(knight_valid_move((0, 0), (2, 1)))
        self.assertTrue(knight_valid_move((0, 0), (1, 2)))
        self.assertTrue(knight_valid_move((4, 4), (6, 5)))
        self.assertTrue(knight_valid_move((4, 4), (5, 6)))

    def test_knight_invalid_move_not_L_shape(self):
        self.assertFalse(knight_valid_move((0, 0), (3, 3)))
        self.assertFalse(knight_valid_move((4, 4), (4, 6)))
        self.assertFalse(knight_valid_move((4, 4), (6, 6)))
        self.assertFalse(knight_valid_move((4, 4), (3, 5)))

    def test_knight_valid_move_edge_cases(self):
        self.assertTrue(knight_valid_move((7, 7), (5, 6)))
        self.assertTrue(knight_valid_move((7, 7), (6, 5)))
        self.assertFalse(knight_valid_move((7, 7), (7, 5)))
        self.assertFalse(knight_valid_move((7, 7), (5, 7)))


if __name__ == "__main__":
    unittest.main()
