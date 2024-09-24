from chess_board import ChessBoard


def pawn_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    if end_pos[1] != start_pos[1] or abs(end_pos[0] - start_pos[0]) > 2:
        return False

    for row in range(start_pos[0], end_pos[0] + 1):
        if board.board[row][end_pos[1]] != ".":
            return False

    return True


def rook_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    if start_pos[0] != end_pos[0] and start_pos[1] != end_pos[1]:
        return False

    if start_pos[0] == end_pos[0]:
        step = 1 if end_pos[1] > start_pos[1] else -1
        for col in range(start_pos[1] + step, end_pos[1], step):
            if board.board[start_pos[0]][col] != ".":
                return False
    else:
        step = 1 if end_pos[0] > start_pos[0] else -1
        for row in range(start_pos[0] + step, end_pos[0], step):
            if board.board[row][start_pos[1]] != ".":
                return False
        return True


def knight_valid_move(start_pos, end_pos):
    pass


def bishop_valid_move(start_pos, end_pos):
    pass


def queen_valid_move(start_pos, end_pos):
    pass


def king_valid_move(start_pos, end_pos):
    pass
