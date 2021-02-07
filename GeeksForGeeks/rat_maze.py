# 1. Create a solution matrix, initially filled with 0’s.
# 2. Create a recursive funtion, which takes initial matrix, output matrix and position of rat (i, j).
# 3. if the position is out of the matrix or the position is not valid then return.
# 4. Mark the position output[i][j] as 1 and check if the current position is destination or not. If destination is reached print the output matrix and return.
# 5. Recursively call for position (i+1, j) and (i, j+1).
# 6. Unmark position (i, j), i.e output[i][j] = 0.
# IE-create a contiguous path through grid where 1 exists
# This is DFS, until it's not

# Input: {1, 0, 0, 0}
#        {1, 1, 0, 1}
#        {0, 1, 0, 0}
#        {1, 1, 1, 1}

# Output: {1, 0, 0, 0}
#         {1, 1, 0, 0}
#         {0, 1, 0, 0}
#         {0, 1, 1, 1}


class RatMaze:
    def __init__(self, N, grid):
        if (N ** 2) != (len(grid) * len(grid)):
            return "Vector count off from grid."
        self.grid = grid
        self.maze = [ [0 for x in range(N)] for y in range(N) ]
        self.start = (0, 0)
        self.end = (N-1, N-1)

    def maze_fini(self):
        for x in self.maze:
            print(x)

    def valid_moves(self, i, j):
        return [ (i, j+1), (i+1, j) ]

    def is_edge(self, e0, e1):
        return (e0 > self.end[0]) or (e0 < self.start[0]) or (e1 > self.end[0]) or (e1 < self.start[0])

    def rat_util(self, i, j):
        if self.maze[-1][-1] == 1: return True

        edges = self.valid_moves(i, j)
        for e0,e1 in edges: # this for loop allows backtracking
            print(f"...working edge: {e0,e1}")
            if not self.is_edge(e0, e1) and self.grid[e0][e1] == 1:
                print(f"...working inner edge: {e0,e1}")
                self.maze[e0][e1] = 1
                if self.rat_util(e0, e1):
                    return True
                self.maze[e0][e1] = 0 # we reset last square

        return False # A final return if nothing else works

    def solve(self):
        if self.grid[0][0] != 1:
            return "Starting square empty"
        self.maze[0][0] = 1
        if not self.rat_util(self.start[0], self.start[1]):
            return "No path exists"
        else:
            return self.maze


if __name__ == "__main__":
    rat_grid = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

    r = RatMaze(4, rat_grid)
    res = r.solve()
    print(res)
    r.maze_fini()
