"""
Write function that takes in a non-empty array of ints that are sorted in ASC order and returns a new array of same length with squares of original numbers in ASC order.
Input:
    array = [1, 2, 3, 5, 6, 8, 9]
Output:
    [1, 2, 9, 25, 36, 64, 81]

* watch space and time complexity
"""
import time


def sortedSquaredArray(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i**2)
    return sorted(new_arr)


arr = [1, 2, 3, 5, 6, 8, 9]
arr = [-2, -1]
new_arr = sortedSquaredArray(arr)
print(new_arr)
