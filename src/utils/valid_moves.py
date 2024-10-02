from utils.chess_board import ChessBoard


def pawn_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    try:
        if (
            board.board[end_pos[0]][end_pos[1]].symbol.isupper()
            == board.board[start_pos[0]][start_pos[1]].symbol.isupper()
        ):
            print("Invalid move: destination square is occupied by a piece of the same color")
            return False
    except Exception:
        pass

    try:
        direction = 1 if board.board[start_pos[0]][start_pos[1]].symbol.isupper() else -1
    except Exception:
        print("Invalid move: start position is empty")
        return False
    
    start_row = 1 if direction == 1 else 6

    if end_pos[1] == start_pos[1]:  # Moving forward
        print("Valid move, moving forward")
        if end_pos[0] - start_pos[0] == direction:
            print("Valid move, moving one square")
            if board.board[end_pos[0]][end_pos[1]] != ".":
                print("Invalid move, destination square is occupied")
                return False
            return True
        elif end_pos[0] - start_pos[0] == 2 * direction and start_pos[0] == start_row:
            print("Valid move, moving two squares")
            if board.board[start_pos[0] + direction][start_pos[1]] != "." and board.board[end_pos[0]][end_pos[1]] != ".":
                print("Invalid move, path is blocked")
                return False
            return True
    elif abs(end_pos[1] - start_pos[1]) == 1 and end_pos[0] - start_pos[0] == direction:
        print("Valid move, capturing opponent piece")
        return board.board[end_pos[0]][end_pos[1]] != "."
    print("Invalid move, pawn can't move to that square")
    return False


def rook_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    if start_pos[0] != end_pos[0] and start_pos[1] != end_pos[1]:
        print("Invalid move: rook can't move diagonally")
        return False
    try:
        if (
            board.board[end_pos[0]][end_pos[1]].symbol.isupper()
            == board.board[start_pos[0]][start_pos[1]].symbol.isupper()
        ):
            print("Invalid move: destination square is occupied by a piece of the same color")
            return False
    except Exception:
        pass
    
    if start_pos[0] == end_pos[0]:
        step = 1 if end_pos[1] > start_pos[1] else -1
        for col in range(start_pos[1] + step, end_pos[1], step):
            if board.board[start_pos[0]][col] != ".":
                print("Invalid move: path is blocked")
                return False
        return True
    else:
        step = 1 if end_pos[0] > start_pos[0] else -1
        for row in range(start_pos[0] + step, end_pos[0], step):
            if board.board[row][start_pos[1]] != ".":
                print("Invalid move: path is blocked")
                return False
        return True


def knight_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    row_diff = abs(start_pos[0] - end_pos[0])
    col_diff = abs(start_pos[1] - end_pos[1])
    
    try:
        if (
            board.board[end_pos[0]][end_pos[1]].symbol.isupper()
            == board.board[start_pos[0]][start_pos[1]].symbol.isupper()
        ):
            print("Invalid move: destination square is occupied by a piece of the same color")
            return False
    except Exception:
        pass
    
    print("Valid move, knight can move to that square")
    
    if row_diff == 0 or col_diff == 0:
        print("Invalid move: knight can't move in a straight line")
        return False
    
    return(row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


def bishop_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    row_diff = abs(start_pos[0] - end_pos[0])
    col_diff = abs(start_pos[1] - end_pos[1])

    if row_diff != col_diff:
        print("Invalid move: bishop can only move diagonally")
        return False

    row_step = 1 if end_pos[0] > start_pos[0] else -1
    col_step = 1 if end_pos[1] > start_pos[1] else -1

    for i in range(1, row_diff):
        if board.board[start_pos[0] + i * row_step][start_pos[1] + i * col_step] != ".":
            print("Invalid move: path is blocked")
            return False

    try:
        if (
            board.board[end_pos[0]][end_pos[1]].symbol.isupper()
            == board.board[start_pos[0]][start_pos[1]].symbol.isupper()
        ):
            print("Invalid move: destination square is occupied by a piece of the same color")
            return False
    except Exception:
        pass
    print("Valid move, bishop can move to that square")
    return True


def queen_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    return rook_valid_move(start_pos, end_pos, board) or bishop_valid_move(
        start_pos, end_pos, board
    )


def king_valid_move(start_pos: tuple, end_pos: tuple, board: ChessBoard) -> bool:
    row_diff = abs(start_pos[0] - end_pos[0])
    col_diff = abs(start_pos[1] - end_pos[1])

    if max(row_diff, col_diff) > 1:
        print("Invalid move: king can only move one square")
        return False

    # Check if the destination square is occupied by a piece of the same color
    try:
        if (
            board.board[end_pos[0]][end_pos[1]].symbol.isupper()
            == board.board[start_pos[0]][start_pos[1]].symbol.isupper()
        ):
            print("Invalid move: destination square is occupied by a piece of the same color")
            return False
    except Exception:
        print("Valid move, king can move to that square")

    return True
