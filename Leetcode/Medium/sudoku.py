class Sudoku:
    def __init__(self, board):
        self.board = board


    def elsewhere_in_row(self, row, num):
        count = 0
        for i in range(9):
            if(self.board[row][i] == num):
                count += 1
        return True if count > 1 else False


    def elsewhere_in_col(self, col, num):
        count = 0
        for i in range(9):
            if(self.board[i][col] == num):
                count += 1
        return True if count > 1 else False


    def elsewhere_in_box(self, row, col, num):
        count = 0
        for i in range(3):
            for j in range(3):
                if(self.board[i + row][j + col] == num):
                    count += 1
        return True if count > 1 else False


    def num_in_square_valid(self, row, col, num):
        """
        Returns True if all tests False
        """
        return not self.elsewhere_in_row(row, num) \
           and not self.elsewhere_in_col(col, num) \
           and not self.elsewhere_in_box(row - row % 3, col - col % 3, num)


    def validate_square(self):
        """
        Method simply validates that number present in square is not duplicated
        """
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                try:
                    num = int(self.board[row][col])
                    if not self.num_in_square_valid(row, col, str(num)):
                        return False
                except ValueError:
                    pass
        return True


board = [
    ["8","3",".", ".","7",".",".",".","."],
    ["6",".",".", "1","9","5",".",".","."],
    [".","9","8", ".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

sud = Sudoku(board)
print(sud.validate_square())
print(Sudoku(board).validate_square())
