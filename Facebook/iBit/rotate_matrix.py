class Solution:
    def rotate(self, A):
        # Horizontal axis flip
        def flip_rows():
            # Logic
            # Prime
            row = 0
            while not row == len(A):
                L = 0
                R = len(A[0]) - 1
                while not L >= R:
                    A[row][L], A[row][R] = A[row][R], A[row][L]
                    L += 1
                    R -= 1
                row += 1

        # Diagonal left axis flip
        def flip_diag():
            # Logic
            # Prime
            row = 0
            col = row + 1
            while not row == len(A):
                while not col == len(A[row]):
                    A[row][col], A[col][row] = A[col][row], A[row][col]
                    col += 1
                row += 1
                col = row + 1

        # Edge Case(s)
        if len(A) == 1: return [[x] for x in A[0]]
        if len(A[0]) == 1: return [x[0] for x in reversed(A)] 

        flip_diag()
        flip_rows()
        return A


m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

#m = [[1, 2, 3, 4]]
#m = [
    #[1],
    #[2],
    #[3]
#]
a = Solution()
print(a.rotate(m))

