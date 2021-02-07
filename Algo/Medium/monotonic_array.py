"""
Write function that takes array of ints and returns bool based on monotonic check.
Input:
    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Output:
    True

* monotonic-- an array of integers either non-increasing or non-decreasing
* None and one are monotonic
* for loop-- first element (to < or >) determines negate or increase
    with == getting a pass except on Last element (if first to be eval'ed) to Next
answer - O(N)T / O(1)S
"""
import time

def isMonotonic(array):

    non_decrease = False
    non_increase = False
    if len(array) <= 1:
        return True

    # The Failure is if Both are true
    for x in range(len(array)-1):
        if array[x] < array[x+1]:
            non_decrease = True
        elif array[x] > array[x+1]:
            non_increase = True
        else:
            pass

    return False if non_decrease and non_increase else True
        



if __name__ == "__main__":

    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    array = [1, 1, 1, 1, 1, 1]

    print(isMonotonic(array))
