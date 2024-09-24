from utils.chess_board import ChessBoard


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


def knight_valid_move(start_pos: tuple, end_pos: tuple) -> bool:
    row_diff = abs(start_pos[0] - end_pos[0])
    col_diff = abs(start_pos[1] - end_pos[1])
    return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


def bishop_valid_move(start_pos: tuple, end_pos: tuple, board: tuple):
    row_diff = abs(start_pos[0] - end_pos[0])
    col_diff = abs(start_pos[1] - end_pos[1])

    if row_diff != col_diff:
        return False

    row_step = 1 if end_pos[0] > start_pos[0] else -1
    col_step = 1 if end_pos[1] > start_pos[1] else -1

    for i in range(1, row_diff):
        if board.board[start_pos[0] + i * row_step][start_pos[1] + i * col_step] != ".":
            return False

    return row_diff == col_diff


def queen_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    return rook_valid_move(start_pos, end_pos, board) or bishop_valid_move(
        start_pos, end_pos, board
    )


def king_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    row_diff = abs(start_pos[0] - end_pos[0])
    col_diff = abs(start_pos[1] - end_pos[1])

    if max(row_diff, col_diff) > 1:
        return False

    # Check if the destination square is occupied by a piece of the same color
    if (
        board.board[end_pos[0]][end_pos[1]].isupper()
        == board.board[start_pos[0]][start_pos[1]].isupper()
    ):
        return False

    return True
