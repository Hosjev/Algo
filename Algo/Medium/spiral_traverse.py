"""
Write function that takes an n-x-m 2-dimensional array (square with n/m) and returns 1-dimensional
array of all the array's elements in spiral order. 
Input:
    array = [
        [1,   2,  3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10,  9,  8, 7]
      ]
Output:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

* spiral order starts at top left corner of 2-dimensions, goes to the right and proceeds
      in spiral pattern
answer - O(N)T / O(N)S
"""
import time

def spiralTraverse(array):

    # We go across the column, down the row, reverse the column, up the row
    # I had the pattern, -1, +1. What I did wrong was trying to do it in one for loop
    res = []
    startR, endR = 0, len(array)-1
    startC, endC = 0, len(array[0])-1

    while startR <= endR and startC <= endC:
        print(f"Running 1st - col eval: {startC, endC}")
        for col in range(startC, endC + 1):
            print(f"...column: {col}")
            res.append(array[startR][col])

        print(f"Running 2nd - row eval: {startR, endR}")
        for row in range(startR + 1, endR + 1):
            print(f"...row: {row}")
            res.append(array[row][endC])

        print(f"Running 3rd - col eval: {startC, endC}")
        for col in reversed(range(startC, endC)):
            print(f"...column: {col}")
            if startR == endR: break
            res.append(array[endR][col])

        print(f"Running 4th - row eval: {startR, endR}")
        for row in reversed(range(startR + 1, endR)):
            print(f"...row: {row}")
            if startC == endC: break
            res.append(array[row][startC])

        startR += 1
        endR -= 1
        startC += 1
        endC -= 1

    return res

if __name__ == "__main__":

    array = [
        [1,   2,  3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10,  9,  8, 7]
      ]

    print(spiralTraverse(array))
