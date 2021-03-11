"""
You're given 2D array of (unequal) height/width containing 1s/0s. This matrix is a 2-toned image where 1==black and 0==white. Islands are defined as 1s running adjacent horizontal or vertical (but not touching sides). Remove the 1s you find qualify as islands.

Input:
    
Output:
    10

** note that a 1 touching another 1 at an edge is NOT part of an island
"""
import time


def removeIslands(matrix):
    # Write your code here.
    # these are "connected" 1s I need to find
    # add while loop to if 1

    def _positions(row, col):
        up = [row-1, col]
        down = [row+1, col]
        left = [row, col-1]
        right = [row, col+1]
        return [up, down, left, right]

    def _is_edge(r, c):
        if r == 0 or r == len(matrix) - 1:  # col
            return True
        if c == 0 or c == len(matrix[0]) - 1:  # row
            return True
        return False

    def _inbounds(r, c):
        return False if (r < 0) or (r > len(matrix) - 1) or (c < 0) or (c > len(matrix[0]) - 1) else True

    def _find_ones(row, col, arr):
        pos = _positions(row, col)
        # print(pos, arr)
        # time.sleep(.2)
        for r, c in pos:
            if _inbounds(r, c):
                if matrix[r][c] == 1:
                    if [r, c] in arr:
                        pass
                    elif _is_edge(r, c):
                        arr.append([r, c])
                    else:
                        arr.append([r, c])
                        _find_ones(r, c, arr)
        return arr

    def _island(row, col):
        # do
        ones = [[row, col]] + _find_ones(row, col, [])
        # mark as X if edged, 0 if island
        print(ones)
        is_island = True
        for r, c in ones:
            if _is_edge(r, c):
                is_island = False
                break
        if not is_island:
            for r, c in ones:
                matrix[r][c] = "X"
        else:
            for r, c in ones:
                matrix[r][c] = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][col] == 1:
                print("found starting one", row, col)
                _island(row, col)

    # remove X
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "X":
                matrix[row][col] = 1

    return matrix


def make_matrix():
    m = [[0 for y in range(5)] for x in range(5)]
    m[0][1] = 1
    m[1][1] = 1
    m[3][2] = 1
    m[1][2] = 1
    m[3][1] = 1
    m[3][4] = 1
    return m


m = make_matrix()

m = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

nm = removeIslands(m)
for i in nm:
    print(i)
