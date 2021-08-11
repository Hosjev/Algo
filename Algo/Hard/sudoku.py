"""
Solve Sudoku board.

Input:
    grid

Output:
    grid solved

** this is the PINNACLE example of recursion, both in code and stack traversal
"""
import time


def solveSudoku(board):
    solve_partial(0, 0, board)
    return board


def solve_partial(row, col, board):
    curr_row = row
    curr_col = col

    # END of row, last column, GO to next row/col 0
    if curr_col == len(board[curr_row]):
        curr_row += 1
        curr_col = 0
        if curr_row == len(board):  # we're OOB and finished
            return True

    # Position empty
    if board[curr_row][curr_col] == 0:
        return try_running_digits(curr_row, curr_col, board)

    # Go ACROSS
    return solve_partial(curr_row, curr_col + 1, board)


def try_running_digits(row, col, board):
    # run 0-9
    for digit in range(1, 10):
        if is_valid_at_position(digit, row, col, board):
            # this is where we temporarily set our digit on the board
            board[row][col] = digit
            # THIS is where we tie in backtracking, as EVERY other digit set
            # MUST be resolved (even if the next call in the stack resolves, another
            # could fail, the catch below reverts that)
            # This return below gets us out of the for loop
            # SO, most of these for loops will be partially completed due to the returns
            # AFTER setting their digits and mostly, returning True to previous caller
            if solve_partial(row, col + 1, board):
                return True

    # if 0-9 do NOT work, we backtrack to previous caller
    board[row][col] = 0
    return False


def is_valid_at_position(value, row, col, board):
    # helper function for every integer we try to place
    # we return 1st False IF our integer is in the row or col
    # then we return False IF the integer is anywhere in the subgrid
    # if neither of these happen, we return True
    row_is_valid = value not in board[row]
    # [digit] not in [ [x for i, x in enumerate(y) if i==col] for y in board]
    col_is_valid = value not in map(lambda r: r[col], board)

    if not row_is_valid or not col_is_valid:
        return False

    subgrid_row_start = (row // 3) * 3
    subgrid_col_start = (col // 3) * 3

    for row_idx in range(3):
        for col_idx in range(3):
            row_to_check = subgrid_row_start + row_idx
            col_to_check = subgrid_col_start + col_idx
            current_value = board[row_to_check][col_to_check]
            if current_value == value:
                return False

    return True  # Finally


if __name__ == "__main__":

    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    print(solveSudoku(board))
