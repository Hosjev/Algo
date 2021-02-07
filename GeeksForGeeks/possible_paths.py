# Count all possible paths from Top left to Bottom right for grid w/dimensions
# iXj i = 2, j = 2 would result in 2 possible paths given right and down turns



class Turns:
    def __init__(self, grid, r, c, value = False):
        self.start = (0, 0)
        self.R = r-1
        self.C = c-1
        self.grid = grid
        self.value = value
        self.paths = 0
        self.steps = [0 for i in range(r+c-1)]

    def valid_moves(self, i, j):
        edges = []
        if j != self.C:
            edges.append( (i, j+1) )
        if i != self.R:
            edges.append( (i+1, j) )
        return edges

    def solve(self, i, j, n):
        # What is my time complexity here?
        # N tracks the index as it changes for DFS
        #  and the value makes this extensible to grid positions and values
        if self.value:
            self.steps[n] = self.grid[i][j]
        else:
            self.steps[n] = (i,j)

        # If we reach the end, add to paths and print current steps/indices
        if (i, j) == (self.R, self.C):
            self.paths += 1
            print(self.steps)

        # Treat moves as edges
        edges = self.valid_moves(i, j)
        for e0, e1 in edges:
            #print(f"...processing edge: {e0,e1}")
            self.solve(e0, e1, n+1)


# THE BELOW functions do the same as above but in reverse
# they calculate UP and LEFT turns by adding sums
# Returns count of possible paths  
# to reach cell at row number m and  
# column number n from the topmost  
# leftmost cell (cell at 1, 1) 
def numberOfPaths(p, q): 
      
    # Create a 1D array to store  
    # results of subproblems 
    dp = [1 for i in range(q)] # dp is list of 1s size q
    for i in range(p - 1): 
        for j in range(1, q): 
            dp[j] += dp[j - 1] 
    return dp[q - 1] 
  
# Or, unpacked...
def numberOfPaths(c, r): 
    # Create a 2D table to store 
    # results of subproblems 
    # C is my columns
    # R is my rows
    count = [[0 for x in range(c)] for y in range(r)] 
    # Stay in row 0 count[0][c]
    for j in range(c): 
        count[0][j] = 1
    # Stay in column 0 count[r][0]
    for i in range(r): 
        count[i][0] = 1
    # Calculate count of paths for other 
    # cells in bottom-up  
    # manner using the recursive solution 
    for i in range(1, r): 
        for j in range(1, c):              
            count[i][j] = count[i-1][j] + count[i][j-1] 
    return count[r-1][c-1]


if __name__ == "__main__":
    r = 2
    c = 2
    grid = [ [0 for x in range(c)] for y in range(r) ]

    t = Turns(grid, r, c)
    # solve for starting row/col 0/0 count 0
    t.solve(0, 0, 0)
    print(t.paths)

    # a different kind of grid
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
       ]
    r = 3
    c = 3
    t = Turns(grid, r, c, True)
    t.solve(0, 0, 0)

    # Another possible solution
    # Driver Code 
    #print(numberOfPaths(5, 5)) 

