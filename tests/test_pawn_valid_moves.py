import unittest
from src.utils.chess_board import ChessBoard
from src.utils.pieces import Pawn
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
        # White pawn at starting position (row 6)
        self.board.board[6][4] = Pawn("white")
        self.assertTrue(pawn_valid_move((6, 4), (5, 4), self.board))
        
        # Black pawn at starting position (row 1) 
        self.board.board[1][4] = Pawn("black")
        self.assertTrue(pawn_valid_move((1, 4), (2, 4), self.board))

    def test_pawn_move_forward_two_squares_from_start(self):
        # White pawn two-square move from starting position
        self.board.board[6][4] = Pawn("white")
        self.assertTrue(pawn_valid_move((6, 4), (4, 4), self.board))
        
        # Black pawn two-square move from starting position
        self.board.board[1][4] = Pawn("black")
        self.assertTrue(pawn_valid_move((1, 4), (3, 4), self.board))

    def test_pawn_move_forward_two_squares_not_from_start(self):
        # White pawn not at starting position should not be able to move two squares
        self.board.board[5][4] = Pawn("white")
        self.assertFalse(pawn_valid_move((5, 4), (3, 4), self.board))
        
        # Black pawn not at starting position should not be able to move two squares
        self.board.board[2][4] = Pawn("black")
        self.assertFalse(pawn_valid_move((2, 4), (4, 4), self.board))

    def test_pawn_capture_diagonally(self):
        # White pawn capturing diagonally
        self.board.board[6][4] = Pawn("white")
        self.board.board[5][5] = Pawn("black")
        self.assertTrue(pawn_valid_move((6, 4), (5, 5), self.board))
        
        # Black pawn capturing diagonally
        self.board.board[1][4] = Pawn("black")
        self.board.board[2][3] = Pawn("white")
        self.assertTrue(pawn_valid_move((1, 4), (2, 3), self.board))

    def test_pawn_invalid_move_sideways(self):
        # Test both colors can't move sideways
        self.board.board[6][4] = Pawn("white")
        self.assertFalse(pawn_valid_move((6, 4), (6, 5), self.board))
        
        self.board.board[1][4] = Pawn("black") 
        self.assertFalse(pawn_valid_move((1, 4), (1, 5), self.board))

    def test_pawn_invalid_move_backward(self):
        # White pawn can't move backward (toward higher row numbers)
        self.board.board[5][4] = Pawn("white")
        self.assertFalse(pawn_valid_move((5, 4), (6, 4), self.board))
        
        # Black pawn can't move backward (toward lower row numbers)  
        self.board.board[2][4] = Pawn("black")
        self.assertFalse(pawn_valid_move((2, 4), (1, 4), self.board))


if __name__ == "__main__":
    unittest.main()
