"""
You're given a 2-dimensional array (matrix) of distinct ints and a target integer. Each row in the matrix is sorted and each column is also sorted; the matrix doesn't necessarily have the same height and width.

Write a function that returns an array of the row and column of indices of the target int if it's contained in the matrix, OR [-1, -1]

Input:
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]
    target = 44

Output:
    [3, 3]


O(n)T | O(1)S
"""
import time


def both_greater(right, down, target):
    # Forward positions are Row 0 Col +1 and Row +1 and Col 0
    return True if right > target and down > target else False


def swap(np, a, b):
    if np == a:
        return b
    else:
        return a


def searchInSortedMatrix(array, target):
    # while iterative version
    row = 0
    col = len(array[0]) - 1
    while row < len(array) and col >= 0:
        if target < array[row][col]:
            col -= 1
        elif target > array[row][col]:
            row += 1
        else:
            return [row, col]
    return [-1, -1]


def searchInSortedMatrix(array, target):
    # My tuple is the starting row/col/# of false edges
    if target == array[0][0]:
        return [0, 0]
    elif target < array[0][0]:
        return [-1, -1]
    else:
        for r in array: r.append(float("inf")) # Add column
        array.append([float("inf")] * len(array[0])) # Add row
        res = sorted_matrix_recur([0,0], array, target)
        return res if res else [-1, -1]


def sorted_matrix_recur(position, array, target):
    # Eval 31 (success CHECK) then 8 (a return on recur) then 10 (a pos 2 fail)
    print("I won:", array[position[0]][position[1]])
    if array[position[0]][position[1]] == float("inf"):
        print("check")
        return [-1, -1]

    # New positions and values
    right = [position[0], position[1] + 1]
    down = [position[0] + 1, position[1]]
    val_R = array[right[0]][right[1]]
    val_D = array[down[0]][down[1]]

    if target == val_R: return right
    if target == val_D: return down

    # Keep track of turns per position change. If more than 1, return False
    if both_greater(val_R, val_D, target):
        return [-1, -1]

    # Go right, if not go down
    # What about for loop, for R and D
    if abs(target - val_R) < abs(target - val_D):
        new_position = right
    else:
        new_position = down
    for x in range(2):
        #if sorted_matrix_recur(new_position, array, target) != [-1, -1]:
        result = sorted_matrix_recur(new_position, array, target)
        if result != [-1, -1]: return result
        print("resetting...")
        new_position = swap(new_position, right, down)

        



if __name__ == "__main__":

    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]
    target = 1001

    print(searchInSortedMatrix(matrix, target))
