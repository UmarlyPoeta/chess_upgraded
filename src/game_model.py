from utils.chess_board import ChessBoard
from utils.valid_moves import pawn_valid_move


class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.current_turn = "white"

    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def is_valid_move(self, start_pos, end_pos):
        # Implement basic move validation logic
        start_piece = self.board.board[start_pos[0]][start_pos[1]]
        end_piece = self.board.board[end_pos[0]][end_pos[1]]
        if start_piece is None or start_piece.color != self.current_turn:
            return False
        if end_piece is not None and end_piece.color == self.current_turn:
            return False
        # Add more rules for specific pieces
        if start_piece.symbol == "P" and not pawn_valid_move(
            start_pos, end_pos, self.board
        ):
            return False
        return True

    def move_piece(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            self.board.board[end_pos[0]][end_pos[1]] = self.board.board[start_pos[0]][
                start_pos[1]
            ]
            self.board.board[start_pos[0]][start_pos[1]] = None
            self.switch_turn()
            return True
        return False

    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_turn}'s turn")
            start_pos = tuple(
                map(int, input("Enter start position (row col): ").split())
            )
            end_pos = tuple(map(int, input("Enter end position (row col): ").split()))
            if not self.move_piece(start_pos, end_pos):
                print("Invalid move, try again.")
