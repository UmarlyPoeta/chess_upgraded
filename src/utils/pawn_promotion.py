from utils.chess_board import ChessBoard
from utils.pieces import Queen, Rook, Bishop, Knight

def check_pawn_promotion(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    moved_piece = board.board[end_pos[0]][end_pos[1]]
    
    # Check if the moved piece is a pawn that reached the promotion rank
    if type(moved_piece).__name__ == "Pawn":
        # White pawn reaches row 0 (black's back rank) 
        # Black pawn reaches row 7 (white's back rank)
        if (moved_piece.color == "white" and end_pos[0] == 0) or \
           (moved_piece.color == "black" and end_pos[0] == 7):
            
            print(f"Pawn promotion! {moved_piece.color} pawn reached the end.")
            promotion = input("Choose promotion piece (Q/R/B/N): ").upper()
            while promotion not in ["Q", "R", "B", "N"]:
                promotion = input("Invalid input, please enter Q, R, B, or N: ").upper()
            
            # Create the new piece
            if promotion == "Q":
                new_piece = Queen(moved_piece.color)
            elif promotion == "R":
                new_piece = Rook(moved_piece.color)
            elif promotion == "B":
                new_piece = Bishop(moved_piece.color)
            elif promotion == "N":
                new_piece = Knight(moved_piece.color)
            
            # Replace the pawn with the new piece
            board.board[end_pos[0]][end_pos[1]] = new_piece
            return True
    
    return False
