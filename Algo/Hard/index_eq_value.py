"""
Write a function that takes in an array of distinct integers as well as an integer "k" that returns the smallest "kth" integer in that array.

The function should do this in linear time, on average.

Input:
    array = [-5, -3, 0, 3, 4, 5, 9]

Output:
    3

* so I understand this as: 2, 3, 5 is the 3rd smallest, b/c 2 < 3 < 5
answer - O(N^2)T / O(N)S
"""
import time


def indexEqualsValue(arr):
    """
    """
    result = None
    for x in range(len(arr)):
        if x == arr[x]:
            return x

    return -1



if __name__ == "__main__":

    array = [-5, -3, 0, 3, 4, 5, 9]

    print(indexEqualsValue(array))
