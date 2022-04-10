from typing import List


class Solution:
    def _set(self, matrix):
        self.memo = [[0 for c in r] for r in matrix]
        self.dirs = [(0,1), (1,0), (0,-1), (-1,0)] # R, D, L, U

    def _dfs(self, r, c, matrix):
        if self.memo[r][c] != 0: return self.memo[r][c]
        for d in self.dirs:
            nr, nc = r + d[0], c + d[1]
            # Can we?
            if nr >= 0 and nr < len(matrix) and \
               nc >= 0 and nc < len(matrix[r]) and \
               matrix[nr][nc] > matrix[r][c]:
                   self.memo[r][c] = max(self.memo[r][c], self._dfs(nr, nc, matrix))
        self.memo[r][c] += 1
        return self.memo[r][c]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # EC
        if not bool(matrix): return 0

        self._set(matrix)
        result = int()
        # Logic
        #   we still eval each square
        #   but instead of endlessly spiraling on each direction
        #   we store the answer already received, the MAX answer
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                result = max(result, self._dfs(r, c, matrix))
        return result


if __name__ == "__main__":
    m = [[9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]]
    obj = Solution()
    print(obj.longestIncreasingPath(m))
