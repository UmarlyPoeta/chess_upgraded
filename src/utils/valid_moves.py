from chess_board import ChessBoard


def pawn_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    if end_pos[1] != start_pos[1] or abs(end_pos[0] - start_pos[0]) > 2:
        return False

    for position_to_check in range(start_pos[0], end_pos[0] + 1):
        if board.board[position_to_check][end_pos[1]] != ".":
            return False

    return True


def rook_valid_move(start_pos, end_pos):
    pass


def knight_valid_move(start_pos, end_pos):
    pass


def bishop_valid_move(start_pos, end_pos):
    pass


def queen_valid_move(start_pos, end_pos):
    pass


def king_valid_move(start_pos, end_pos):
    pass
