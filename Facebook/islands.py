class Solution:
    def _recurse(self, row, col, visited, grid):
        if (row >= len(grid)) or (row < 0) or \
           (col >= len(grid[0])) or (col < 0) or \
           (row, col) in visited:
            return
        if str(grid[row][col]) == str(1):
            if not (row, col) in visited: visited.append((row, col))
            self._recurse(row, col + 1, visited, grid)
            self._recurse(row, col - 1, visited, grid)
            self._recurse(row + 1, col, visited, grid)
            self._recurse(row - 1, col, visited, grid)

    def numIslands(self, grid) -> int:
       # Run recursion 
       # islands = [0]
       islands = int()
       visited = list()
       for i in range(len(grid)):
           for j in range(len(grid[i])):
               if str(grid[i][j]) == str(0):
                   visited.append((i, j))
               else:
                   if not (i, j) in visited:
                       islands += 1
                       self._recurse(i, j, visited, grid)
       return islands


if __name__ == "__main__":
    g = [
            [1,0,1],
            [0,1,0],
            [1,0,0],
            [1,0,1]
        ]
    print(Solution().numIslands(g))
    g = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
    print(Solution().numIslands(g))
    g = [
            ["1","0","1","1","1"],
            ["1","0","1","0","1"],
            ["1","1","1","0","1"]
            ]
    print(Solution().numIslands(g))
