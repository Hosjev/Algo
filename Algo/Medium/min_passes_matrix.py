"""
Write a function that takes in an integer matrix of potentially unequal height and width and returns the min number of passes required to convert all negative ints in the matrix to positive ints.

A negative int in the matrix can only be converted to a positive int if one or more of its adjacent elements is positive. An adjacent element is an element that is to the left, right, above, or below the current element in the matrix. Converting a negative to a positive simply involves multiplying it by -1.

Note that the 0 value is neither positive nor negative, meaning that a 0 can't convert an adjacent negative to a positive.

A single pass through the matrix involves converting all the negative ints that CAN be converted at a particular point in time.

Ex = 2:
[
    [0, -2, -1],
    [-5, 2, 0],
    [-6, -2, 0]
]

1st pass, only 3 converted.
[
    [0, 2, -1],
    [5, 2, 0],
    [-6, 2, 0]
]

2nd pass, rest converted.
[
    [0, 2, 1],
    [5, 2, 0],
    [6, 2, 0]
]

Ex = -1:
[
    [0, -2, 0],
    [-5, 0, 0], # only -5 converted on 1st pass
    [6,  2, 0]
]

Input:
    matrix = [
        [0, -1, -3,  2,  0],
        [1, -2, -5, -1, -3],
        [3,  0,  0, -4, -1]
    ]

Output:
    3

** input matrix always contains at least one element.
** if neg ints in the input matrix can't all be converted, return -1
** how do you STOP iterating and exit? When we FAIL twice
** O(w * h)T | O(w * h)S
"""
import time
import copy


def build_subarray(matrix, row, col):
    subarray = []

    if col-1 >= 0:
        subarray.append(matrix[row][col-1])  # left
    if not col+1 >= len(matrix[row]):
        subarray.append(matrix[row][col+1])  # right
    if row-1 >= 0:
        subarray.append(matrix[row-1][col])  # up
    if not row+1 >= len(matrix):
        subarray.append(matrix[row+1][col])  # down
    return subarray


def minimumPassesOfMatrix(matrix):
    # Write your code here.
    # O(w * h) * O(nlog)
    # Set variable for number of passes
    num_of_passes = -1
    # Build matrix for holding new values
    c_matrix = copy.deepcopy(matrix)
    # Set variable for changes made
    change_made = 1
    neg_num_found = 0

    while (change_made != 0):
        neg_num_found = 0
        change_made = 0
        # Update number of passes
        num_of_passes += 1
        # Iterate through matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                # If current square is negative
                if matrix[row][col] < 0:
                    neg_num_found += 1
                    subarray = build_subarray(matrix, row, col)
                    a = True in [True for x in subarray if x > 0]
                    if a:
                        change_made += 1
                        c_matrix[row][col] = matrix[row][col] * -1

        # After last iteration, copy it back
        matrix = copy.deepcopy(c_matrix)

    return -1 if (change_made == 0 and neg_num_found > 0) else num_of_passes


def minimumPassesOfMatrix(matrix):
    passes = convertNegatives(matrix)
    return passes - 1 if not containsNegative(matrix) else -1


def convertNegatives(matrix):
    # This function identifies positives then exhausts them
    # (we don't care about negs until the final eval)
    nextPassQueue = getAllPositives(matrix)  # do once

    passes = 0

    while (len(nextPassQueue) > 0):
        # Rewrite/swap list/Q of next into current
        currentPassQueue = nextPassQueue
        nextPassQueue = []

        while (len(currentPassQueue) > 0):
            # O(n) below b/c pop(0) has to read index
            # instead of proper queue which would be O(1)
            currentRow, currentCol = currentPassQueue.pop(0)

            adjacentPositions = getAdjacentPos(currentRow, currentCol, matrix)

            # If any available adjacent position is negative
            # rewrite it then add itself to positive queue
            for row, col in adjacentPositions:
                value = matrix[row][col]
                if value < 0:  # a neg
                    matrix[row][col] = value * -1
                    nextPassQueue.append([row, col])

        passes += 1

    return passes


def getAllPositives(matrix):
    positivePositions = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                positivePositions.append([row, col])

    return positivePositions


def getAdjacentPos(row, col, matrix):
    # All constant time ops
    adjacentPositions = []

    if row > 0:  # up
        adjacentPositions.append([row-1, col])
    if row < len(matrix) - 1:  # bottom
        adjacentPositions.append([row+1, col])
    if col > 0:  # left
        adjacentPositions.append([row, col-1])
    if col < len(matrix[row]) - 1:  # right
        adjacentPositions.append([row, col+1])

    return adjacentPositions


def containsNegative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True

    return False


if __name__ == "__main__":

    matrix = [
        [0, -1, -3,  2,  0],
        [1, -2, -5, -1, -3],
        [3,  0,  0, -4, -1]
    ]

    # answer = 3

    print(minimumPassesOfMatrix(matrix))
