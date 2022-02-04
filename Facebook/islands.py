from typing import List



class Solution:
    def recurse(self, row, col, grid):
        # Go as DEEP as possible, mark shit off
        grid[row][col] = "0"
        if (row + 1 < len(grid)) and (grid[row + 1][col] == "1"): # Down
            self.recurse(row + 1, col, grid)
        if (row - 1 >= 0) and (grid[row - 1][col] == "1"): # Up
            self.recurse(row - 1, col, grid)
        if (col + 1 < len(grid[0])) and (grid[row][col + 1] == "1"): # Right
            self.recurse(row, col + 1, grid)
        if (col - 1 >= 0) and (grid[row][col - 1] == "1"): # Left
            self.recurse(row, col - 1, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge Case(s)
        
        # Prime
        islands = int()
        
        # Logic
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == str(1):
                    islands += 1
                    self.recurse(row, col, grid)
        return islands



if __name__ == "__main__":
    g = [
            ["1",0,"1"],
            [0,"1",0],
            ["1",0,0],
            ["1",0,"1"]
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
