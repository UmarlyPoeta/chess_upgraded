from utils.chess_board import ChessBoard

def check_pawn_promotion(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    if board.board[start_pos[0]][start_pos[1]].symbol == "P" and end_pos[0] == 0:
        print("Promote pawn to: ")
        promotion = input("Q, R, B, or N: ").upper()
        while promotion not in ["Q", "R", "B", "N"]:
            promotion = input("Invalid input, please enter Q, R, B, or N: ").upper()
        board.board[end_pos[0]][end_pos[1]].symbol = promotion
        board.board[start_pos[0]][start_pos[1]].symbol = None  # Clear the original pawn position
        return True
    return False
