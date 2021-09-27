class Sudoku:
    def __init__(self, board):
        self.board = board


    def find_avail_square(self, placeholder):
        for r in range(9):
            for c in range(9):
                if (self.board[r][c] == "."):
                    placeholder[0] = r
                    placeholder[1] = c
                    return True
        return False


    def used_in_row(self, row, num):
        for c in range(9):
            if (self.board[row][c] == num):
                return True
        return False


    def used_in_col(self, col, num):
        for r in range(9):
            if (self.board[r][col] == num):
                return True
        return False


    def used_in_box(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if (self.board[i + row][j + col] == num):
                    return True
        return False


    def num_in_square_valid(self, row, col, num):
        """
        Returns True if all tests False
        """
        return not self.used_in_row(row, num) \
           and not self.used_in_col(col, num) \
           and not self.used_in_box(row - row % 3, col - col % 3, num)


    def solve(self):
        """
        Method that recursively fills in board
        then backtracks that answer if future squares
        fail.
        """
        placeholder = [0, 0]

        if not self.find_avail_square(placeholder):
            return True

        row = placeholder[0]
        col = placeholder[1]

        for num in range(1, 10):
            if self.num_in_square_valid(row, col, str(num)):
                self.board[row][col] = str(num)
                if self.solve():
                    return True
                # Backtracking
                self.board[row][col] = "."

        return False


    def finish_board(self):
        self.solve()
        return self.board

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]


sud = Sudoku(board)
print(sud.finish_board())
