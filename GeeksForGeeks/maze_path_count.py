# Count number of paths available in grid maze.
# (i + 1, j) and (i, j + 1) valid moves
# As far as I can see, the logic is:
#    Split successful? increase path count
#    Blockade? decrease path count
# Constant time


class MazePath:
    def __init__(self, N, grid):
        self.steps = N
        self.grid = self.grid_alter(grid)
        self.end = (N -1, N -1)
        self.edge = N-1
        self.m_paths = 0

    def grid_alter(self, grid):
        # Change this to 1=valid step, 0=blockade
        for row in range(self.steps):
            for col in range(self.steps):
                if grid[row][col] == 0: grid[row][col] = 1
                if grid[row][col] == -1: grid[row][col] = 0
        return grid

    def at_right_edge(self, coor):
        return (self.edge == coor[1])

    def at_bottom_edge(self, coor):
        return (self.edge == coor[0])

    def maze_util(self, c1, c2):
        # We reached the end node
        if (c1, c2) == self.end: return
        # We hit a blockade. Do not explore this path or its edges
        if self.grid[c1][c2] == 0: return

        print(f"...maze coordinates: {c1, c2}")

        # Did we reach edges?
        go_right = False
        go_down = False
        if self.at_right_edge( (c1, c2) ):
            go_down = True
            corner_sum = self.grid[c1+1][c2] + 0
        elif self.at_bottom_edge( (c1, c2) ):
            go_right = True
            corner_sum = self.grid[c1][c2+1] + 0
        else:
            go_down = go_right = True
            corner_sum = self.grid[c1+1][c2] + self.grid[c1][c2+1]

        # Finally, evaluate
        if corner_sum == 2:
            self.m_paths += 1
            print(f"...we added a new path at vertex: {c1, c2}")
        if corner_sum == 0:
            self.m_paths -= 1
            print(f"...we reached a closed block: {c1, c2}")
        if go_right: self.maze_util(c1, c2+1)
        if go_down: self.maze_util(c1+1, c2)


    def maze_solve(self):
        # If we start or end with blocks, return no paths
        if not self.grid[0][0] or not self.grid[-1][-1]:
            return 0
        else:
            self.m_paths = 1
        # Fire!
        self.maze_util(0, 0)
        return self.m_paths



if __name__ == "__main__":
    # Setup our maze
    maze_grid = [
        [ 0, 0, 0, 0 ],
        [ 0, -1, 0, 0 ],
        [ 0, 0, 0, 0 ],
        [ 0, -1, 0, 0 ]
       ]
    
    m = MazePath(4, maze_grid)
    print(m.maze_solve())
