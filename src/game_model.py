from utils.chess_board import ChessBoard
from utils.valid_moves import (
    pawn_valid_move,
    rook_valid_move,
    bishop_valid_move,
    king_valid_move,
    knight_valid_move,
    queen_valid_move,
)


class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.current_turn = "white"

    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def is_valid_move(self, start_pos, end_pos):
        # Implement basic move validation logic
        start_piece = self.board.board[start_pos[0]][start_pos[1]]

        if start_piece == ".":
            print("start piece is a .")     # Debugging
            return False

        if start_piece.color != self.current_turn:
            print("start piece is not the right color") # Debugging
            return False
        # Add more rules for specific pieces
        piece_type = type(start_piece).__name__.lower()

        match (piece_type):
            case "pawn":
                return pawn_valid_move(start_pos, end_pos, self.board)
            case "rook":
                return rook_valid_move(start_pos, end_pos, self.board)
            case "bishop":
                return bishop_valid_move(start_pos, end_pos, self.board)
            case "knight":
                return knight_valid_move(start_pos, end_pos, self.board)
            case "queen":
                return queen_valid_move(start_pos, end_pos, self.board)
            case "king":
                return king_valid_move(start_pos, end_pos, self.board)
            case _:
                print("Invalid piece type") # Debugging
                return False

    def move_piece(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            if self.board.board[end_pos[0]][end_pos[1]] != ".":
                print(f"Captured {type(self.board.board[end_pos[0]][end_pos[1]]).__name__}")
            self.board.board[end_pos[0]][end_pos[1]] = self.board.board[start_pos[0]][
                start_pos[1]
            ]
            self.board.board[start_pos[0]][start_pos[1]] = "."
            self.switch_turn()
            return True
        print("Invalid move") # Debugging
        return False

    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_turn}'s turn")
            move = input("Enter your move (e.g., e2 e4): ").strip().lower()
            try:
                start_pos = (8 - int(move[1]), int(ord(move[0]) - ord("a")))
                end_pos = (8 - int(move[4]), int(ord(move[3]) - ord("a")))
                print(start_pos, end_pos) # Debugging
                if not self.move_piece(start_pos, end_pos):
                    print("Invalid move, try again.")
            except (IndexError, ValueError):
                print("Invalid input format, please use the format 'e2 e4'.")
