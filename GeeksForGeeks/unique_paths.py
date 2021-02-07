""" Given grid size of m * n, start at 0,0 to m,n, count all unique paths, given obstacles
Input: [[0,0,0],
        [0,1,0],
        [0,0,0]]

Output: 2
"""


class UniquePath:
    def __init__(self, r, c, grid):
        # Run this as DFS
        self.R = r - 1
        self.C = c - 1
        self.grid = grid
        self.upaths = 0
        self.paths = [0 for x in range(r+c-1)]

    def valid_moves(self, i, j):
        # If not blocked, favor right then down
        edges = []
        if self.grid[i][j] != 1:
            if j != self.C:
                edges.append( (i,j+1) )
            if i != self.R:
                edges.append( (i+1,j) )
        return edges

    def solve_util(self, i, j, n):
        self.paths[n] = (i,j)

        if (i, j) == (self.R, self.C):
            self.upaths += 1
            print(self.paths)

        edges = self.valid_moves(i, j)
        for e0, e1 in edges:
            self.solve_util(e0, e1, n+1)

        return True

    def solve(self):
        if self.grid[0][0] == 1:
            return "Starting grid blocked."
        if self.solve_util(0,0,0):
            return self.upaths
        return "No valid paths in grid"


if __name__ == "__main__":
    r = 4
    c = 4
    grid = [ [0 for x in range(c)] for y in range(r)]
    grid[1][1] = 1
    grid[1][0] = 1
    u = UniquePath(r, c, grid)
    print(u.solve())
