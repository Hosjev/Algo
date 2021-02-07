"""
Write a function that takes in an array of distinct integers as well as an integer "k" that returns the smallest "kth" integer in that array.

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


def quickselect(arr, k):
    """
    In the grossest sense: iterate forward, keep moving the smallest ints backward
    [inf, inf, inf]
    [8, inf, inf]
    [5, 8, inf]
    [2, 5, 8]
    [2, 5, 8]
    [2, 5, 7]
    [2, 5, 6]
    [2, 3, 5]
    if last position > i: push out
    all else: move + 1
    """
    results = [float("+inf")] * k

    for x in arr:
        move_results(x, results)

    return results[-1]


def move_results(x, results):
    for i in reversed(range(len(results))):
        if x < results[i]:
            t = results[i]
            results[i] = x
            if i < len(results) - 1:
                results[i + 1] = t
        else:
            return


def quickselect(arr, k):
    """
    Write a version that uses quicksort.
    """

    recur_quicksort(arr, 0, len(arr)-1)
    # -take the kth int from left
    return arr[k-1]


def recur_quicksort(arr, start_idx, end_idx):
    # We've crossed over ourselves, return
    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    # We review these markers again b/c of multiple sorting loops
    while left_idx <= right_idx:
        if arr[left_idx] > arr[pivot_idx] and arr[right_idx] < arr[pivot_idx]:
            _swap(arr, left_idx, right_idx)
        if arr[left_idx] <= arr[pivot_idx] and arr[right_idx] < arr[pivot_idx]:
            left_idx += 1
        if arr[right_idx] >= arr[pivot_idx]:
            right_idx -= 1

    # Last step in loop
    _swap(arr, pivot_idx, right_idx)

    # Determine smaller leftover array
    left_is_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)

    if left_is_smaller:
        recur_quicksort(arr, start_idx, right_idx - 1)
        recur_quicksort(arr, right_idx + 1, end_idx)
    else:
        recur_quicksort(arr, right_idx + 1, end_idx)
        recur_quicksort(arr, start_idx, right_idx - 1)


def _swap(arr, l, r):
    arr[l], arr[r] = arr[r], arr[l]



if __name__ == "__main__":

    array = [8, 5, 2, 9, 7, 6, 3]
    k = 3
    #array = [1]
    #k = 1

    print(quickselect(array, k))
