"""
Given an array of pairs of integers, find the single-to-multi pair answer that best meets: up to but not over the capacity int given, and with the greatest value. [value, capacity]

Input:
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10

Output:
    [10, [1, 3]]

answer - O(NC)T O(NC)S
"""

def knapsackProblem(items, capacity):
    """
    Create 2D array of maximum capacities for every weight btw 0 and C. Use the items to build the array.
                     capacity
               0 1 2 3 4 5 6 7 8 9 10
    i 0 []     0 0 0 0 0 0 0 0 0 0  0
    t 1 [1,2]  0 0 1 1 1 1 1 1 1 1  1
    e 2 [4,3]  0 0 1 4 4 5 5 5 5 5  5
    m 3 [5,6]  0 0 1 4 4 5 5 5 6 9  9
    s 4 [6,7]  0 0 1 4 4 5 5 6 6 9 10

    * iterate and execute max_vals[row][col] = max(max_vals[row-1][col],
                                                   max_vals[row-1][col-myWeight]+myValue)
    * Like, I Officially HATE this problem.
    * I need to return the original index # to them
    """
    #items.sort(key=lambda idx: idx[1])

    max_values = [ [None for col in range(capacity+1)] for row in range(len(items)+1) ]

    # Prime the matrix
    for row in range(len(max_values)):
        max_values[row][0] = 0

    for col in range(len(max_values[0])):
        max_values[0][col] = 0

    # Straight iterate
    for row in range(1, len(max_values)):
        item = items[row-1]
        value = item[0]
        weight = item[1]
        for col in range(len(max_values[row])):
            # Here, col is idx and unit of capacity
            if col < weight: max_values[row][col] = max_values[row-1][col]
            # Else, we're greater than or equal to unit of C 
            else:
                max_values[row][col] = max(max_values[row-1][col], \
                                           max_values[row-1][col-weight]+value)

    print(max_values)
    print(items)
    # 10 and [4][11]
    position_value = max_values[-1][-1]
    max_value = position_value
    row = len(max_values)-1
    col = len(max_values[0])-1
    answer = [] # Contains index values

    # To unconfuse this fuckery below:
    #     if the row above me, same col is not the same, add myself
    #     myself meaning from the original array of items (so minus 1)
    while position_value != 0:
        if position_value != max_values[row-1][col]:
            answer.append(row-1)
            weight = items[row-1][1]
            row -= 1
            col = col - weight
        else:
            row -= 1
        position_value = max_values[row][col]

    return [ max_value, sorted(answer) ]


if __name__ == "__main__":

    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    #items = [[1, 2], [70, 70], [30, 30], [69, 69], [99, 100]]

    print(knapsackProblem(items, 10))
