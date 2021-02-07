"""
Write a function that takes in an array of distinct integers and uses "quicksort" method to sort.

The function should do this in linear time, on average.

Input:
    array = [8, 5, 2, 9, 7, 6, 3]
    k = 3

Output:
    5

* so I understand this as: 2, 3, 5 is the 3rd smallest, b/c 2 < 3 < 5
answer - O(N^2)T / O(N)S
"""
import time


def quickSort(arr):
    """
    Do this the Algo way, since this is a "thing" -- quicksort.
    """
    recur_quicksort(arr, 0, len(arr) - 1)
    return arr


def recur_quicksort(arr, start_idx, end_idx):
    # This takes us completely out. Arr length 1 or smaller.
    if start_idx >= end_idx:
        return

    print(start_idx, end_idx)
    # Frame variables
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    while left_idx <= right_idx:
        time.sleep(.2)
        # sTuck here: P = =i -4; L = -4; R = -5
        print("L/R:", left_idx, right_idx)
        if (arr[left_idx] > arr[pivot_idx]) and (arr[right_idx] < arr[pivot_idx]):
            _swap(left_idx, right_idx, arr)
        if (arr[left_idx] <= arr[pivot_idx]) and (arr[right_idx] < arr[pivot_idx]):
            left_idx += 1
        if arr[right_idx] >= arr[pivot_idx]:
            right_idx -= 1

    # Swap pivot and right
    _swap(pivot_idx, right_idx, arr)

    # Determine who goes 1st 0...6
    # We look at right side -1 to be noninclusive b/c we just swapped
    # then we subtract start_idx b/c we could be on a recursive right-side call
    left_is_smaller = (right_idx - 1) - start_idx < end_idx - (right_idx + 1)

    if left_is_smaller: # Go left 1st
        recur_quicksort(arr, start_idx, right_idx - 1)
        recur_quicksort(arr, right_idx + 1, end_idx)
    else: # Go right 1st
        recur_quicksort(arr, right_idx + 1, end_idx)
        recur_quicksort(arr, start_idx, right_idx - 1)


def _swap(l, r, arr):
    arr[l], arr[r] = arr[r], arr[l]
    



if __name__ == "__main__":

    array = [8, 5, 2, 9, 7, 6, 3]
    array = [1]
    array = [1, 2]
    array = [2, 1]
    #array = [1, 2, 3]
    array = [ -4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8 ]

    print(quickSort(array))
