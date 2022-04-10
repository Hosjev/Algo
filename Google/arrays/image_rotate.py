from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1 - modify via diagonal axis flip
        # 2 - modify via horizontal axis flip
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix[row])):
                # swap diagonal
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        self._print(matrix)

        # mirror
        L, R = 0, len(matrix) - 1
        row = 0
        while row < len(matrix):
            while L < R:
                matrix[row][L], matrix[row][R] = matrix[row][R], matrix[row][L]
                L += 1
                R -= 1
            row += 1
            L, R = 0, len(matrix) - 1
        self._print(matrix)

    def _print(self, m):
        for i in m:
            print(i)

if __name__ == "__main__":
    m = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ]
    obj = Solution()
    print(obj.rotate(m))
