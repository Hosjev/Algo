"""
You're given 2 ints repping width and height of a grid/graph. Write function that returns # of ways to reach bottom right from top left corner. Only directions allowed are DOWN and RIGHT.


Input:
    4, 3
Output:
    10

** will always be >= 2
"""
import time


def numberOfWaysToTraverseGraphDP(width, height):
    # Write your code here.
    # dynamic programming DP problem

    grid = [[0 for y in range(width)] for x in range(height)]
    # every row, col zero
    for i in range(len(grid)):
        grid[i][0] = 1
    # 1st row, top of every col
    for i in range(len(grid[0])):
        grid[0][i] = 1

    # we go 1st row, across cols start at 1, 1
    for row in range(1, len(grid)):
        for col in range(1, len(grid[row])):
            ways_to_get_here = grid[row-1][col] + grid[row][col-1]
            grid[row][col] = ways_to_get_here

    return grid[-1][-1]


# OR cheating
def numberOfWaysToTraverseGraph(width, height):
    import math
    dividend = math.factorial((width - 1) + (height - 1))
    divisor = math.factorial((width - 1)) * math.factorial((height - 1))
    return int(dividend / divisor)


if __name__ == "__main__":
    print(numberOfWaysToTraverseGraph(3, 2))
