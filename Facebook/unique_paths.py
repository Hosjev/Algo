class Solution:
    def __init__(self, m, n):
        # M = width; N = height
        # Edge Case(s)
        if m == 1 and n == 1: return 1

        # Prime
        self.grid = [[0 for y in range(m)] for x in range(n)]
        for x in range(len(self.grid[0])):
            self.grid[0][x] = 1
        for x in range(len(self.grid)):
            self.grid[x][0] = 1


    def unique_paths(self):
        for r in range(1, len(self.grid)):
            for c in range(1, len(self.grid[r])):
                up = self.grid[r-1][c]
                left = self.grid[r][c-1]
                self.grid[r][c] = up + left
        return self.grid[-1][-1]


a = Solution(4, 3)
print(a.unique_paths())
# O(m*n)
