from utils.chess_board import ChessBoard
from utils.valid_moves import (
    pawn_valid_move,
    rook_valid_move,
    bishop_valid_move,
    king_valid_move,
    knight_valid_move,
    queen_valid_move,
)


def find_king(board: ChessBoard, color: str) -> tuple:
    """Find the position of the king of the given color."""
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece != "." and type(piece).__name__ == "King" and piece.color == color:
                return (row, col)
    return None


def is_square_attacked(board: ChessBoard, pos: tuple, attacking_color: str) -> bool:
    """Check if a square is attacked by any piece of the given color."""
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece != "." and piece.color == attacking_color:
                # Check if this piece can attack the target position
                if is_valid_piece_move(piece, (row, col), pos, board):
                    return True
    return False


def is_valid_piece_move(piece, start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    """Check if a piece can make a valid move from start to end position."""
    piece_type = type(piece).__name__.lower()
    
    match piece_type:
        case "pawn":
            return pawn_valid_move(start_pos, end_pos, board)
        case "rook":
            return rook_valid_move(start_pos, end_pos, board)
        case "bishop":
            return bishop_valid_move(start_pos, end_pos, board)
        case "knight":
            return knight_valid_move(start_pos, end_pos, board)
        case "queen":
            return queen_valid_move(start_pos, end_pos, board)
        case "king":
            return king_valid_move(start_pos, end_pos, board)
        case _:
            return False


def is_in_check(board: ChessBoard, color: str) -> bool:
    """Check if the king of the given color is in check."""
    king_pos = find_king(board, color)
    if king_pos is None:
        return False
    
    opponent_color = "black" if color == "white" else "white"
    return is_square_attacked(board, king_pos, opponent_color)


def get_all_possible_moves(board: ChessBoard, color: str) -> list:
    """Get all possible moves for a given color."""
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece != "." and piece.color == color:
                # Find all valid moves for this piece
                for target_row in range(8):
                    for target_col in range(8):
                        if (target_row, target_col) != (row, col):
                            if is_valid_piece_move(piece, (row, col), (target_row, target_col), board):
                                moves.append(((row, col), (target_row, target_col)))
    return moves


def would_move_leave_king_in_check(board: ChessBoard, start_pos: tuple, end_pos: tuple, color: str) -> bool:
    """Check if making a move would leave the king in check."""
    # Make a temporary copy of the board state
    original_start = board.board[start_pos[0]][start_pos[1]]
    original_end = board.board[end_pos[0]][end_pos[1]]
    
    # Make the move temporarily
    board.board[end_pos[0]][end_pos[1]] = original_start
    board.board[start_pos[0]][start_pos[1]] = "."
    
    # Check if king is in check after the move
    in_check = is_in_check(board, color)
    
    # Restore the original board state
    board.board[start_pos[0]][start_pos[1]] = original_start
    board.board[end_pos[0]][end_pos[1]] = original_end
    
    return in_check


def get_legal_moves(board: ChessBoard, color: str) -> list:
    """Get all legal moves for a given color (moves that don't leave king in check)."""
    possible_moves = get_all_possible_moves(board, color)
    legal_moves = []
    
    for start_pos, end_pos in possible_moves:
        if not would_move_leave_king_in_check(board, start_pos, end_pos, color):
            legal_moves.append((start_pos, end_pos))
    
    return legal_moves


def is_checkmate(board: ChessBoard, color: str) -> bool:
    """Check if the given color is in checkmate."""
    return is_in_check(board, color) and len(get_legal_moves(board, color)) == 0


def is_stalemate(board: ChessBoard, color: str) -> bool:
    """Check if the given color is in stalemate."""
    return not is_in_check(board, color) and len(get_legal_moves(board, color)) == 0