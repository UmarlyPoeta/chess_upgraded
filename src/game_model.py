from utils.chess_board import ChessBoard
from utils.valid_moves import (
    pawn_valid_move,
    rook_valid_move,
    bishop_valid_move,
    king_valid_move,
    knight_valid_move,
    queen_valid_move,
)
from utils.pawn_promotion import check_pawn_promotion
from utils.game_logic import (
    is_in_check,
    is_checkmate,
    is_stalemate,
    would_move_leave_king_in_check,
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
            return False

        if start_piece.color != self.current_turn:
            return False
        
        # Check basic piece movement rules
        piece_type = type(start_piece).__name__.lower()
        if not self._is_basic_move_valid(piece_type, start_pos, end_pos):
            return False
        
        # Check if the move would leave the king in check
        if would_move_leave_king_in_check(self.board, start_pos, end_pos, self.current_turn):
            return False
            
        return True
    
    def _is_basic_move_valid(self, piece_type, start_pos, end_pos):
        """Check basic piece movement rules without considering check."""
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
                return False
    
    def move_piece(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            if self.board.board[end_pos[0]][end_pos[1]] != ".":
                print(f"Captured {type(self.board.board[end_pos[0]][end_pos[1]]).__name__}") 
            
            # Move the piece
            self.board.board[end_pos[0]][end_pos[1]] = self.board.board[start_pos[0]][
                start_pos[1]
            ]
            self.board.board[start_pos[0]][start_pos[1]] = "."
            
            # Check for pawn promotion after the move
            check_pawn_promotion(start_pos, end_pos, self.board)
            
            self.switch_turn()
            return True
        return False

    def play(self):
        print("Welcome to Chess Upgraded!")
        print("Enter moves in format 'e2 e4' or 'quit' to exit")
        print("=" * 40)
        
        while True:
            self.board.display()
            
            # Check for game ending conditions
            if is_checkmate(self.board, self.current_turn):
                winner = "Black" if self.current_turn == "white" else "White"
                print(f"\n🏆 CHECKMATE! {winner} wins!")
                break
            elif is_stalemate(self.board, self.current_turn):
                print(f"\n🤝 STALEMATE! The game is a draw.")
                break
            elif is_in_check(self.board, self.current_turn):
                print(f"\n⚠️  CHECK! {self.current_turn.capitalize()} king is in check!")
            
            print(f"\n{self.current_turn.capitalize()}'s turn")
            move = input("Enter your move (e.g., e2 e4) or 'quit' to exit: ").strip().lower()
            
            if move == 'quit':
                print("Thanks for playing!")
                break
                
            try:
                start_pos = (8 - int(move[1]), int(ord(move[0]) - ord("a")))
                end_pos = (8 - int(move[4]), int(ord(move[3]) - ord("a")))
                
                if not self.move_piece(start_pos, end_pos):
                    print("❌ Invalid move, try again.")
                    
            except (IndexError, ValueError):
                print("❌ Invalid input format, please use the format 'e2 e4'.")
                
        print("\nGame Over!")
