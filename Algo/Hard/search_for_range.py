"""
Write a function that takes in SORTED array of ints as well as a target int. The function should use a variation of the Binary Search algorithm to find a range of indices in between which the target # is contained in the array and should return this range in the form of an array.

The 1st # in the output array should represent the 1st index at which the target # is located, while the 2nd # should represent the last index at which the target number is located. The function should return [-1, -1] if the integer isn't in the array.

Input:
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    array = [0, 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    target = 45
Output:
    [4, 9]


answer - O(N^2)T / O(N)S
"""
import time


def searchForRange(arr, target):
    """
    -In this case, I can't see much else working except to advance
     L/R pointers with an == to then less/greater steps.
    """
    # Store the original indices

    return recur_search_range(arr, target, 0, len(arr)-1)


def recur_search_range(arr, target, left_idx, right_idx):
    # We've crossed over each other and failed
    if left_idx > right_idx:
        return [-1, -1]

    if arr[left_idx] == target and arr[right_idx] == target:
        # we return both
        return [left_idx, right_idx]

    if arr[left_idx] == target:
        pass
    elif arr[left_idx] < target:
        left_idx += 1

    if arr[right_idx] == target:
        pass
    elif arr[right_idx] > target:
        right_idx -= 1

    return recur_search_range(arr, target, left_idx, right_idx)
    

def searchForRange(arr, target):
    """
    The Algo version uses the rhythm of Binary Search with middle pointer
    to establish first a left idx then a right.
    """
    result = [-1, -1]
    recur_search(arr, target, 0, len(arr) - 1, result, True)
    recur_search(arr, target, 0, len(arr) - 1, result, False)
    return result
    


def recur_search(arr, target, left_idx, right_idx, result, goLeft):
    # A more "Binary" search method
    if left_idx > right_idx:
        return

    middle_idx = (left_idx + right_idx) // 2

    # If our middle is less than target, immediately reset LEFT
    if arr[middle_idx] < target:
        recur_search(arr, target, middle_idx + 1, right_idx, result, goLeft)
    # If our middle is greater than target, immediately reset RIGHT
    elif arr[middle_idx] > target:
        recur_search(arr, target, left_idx, middle_idx - 1, result, goLeft)
    else: # our middle IS target
        if goLeft:
            # If we're at the edge OR our middle is Truely mid
            if middle_idx == 0 or arr[middle_idx - 1] != target:
                result[0] = middle_idx
            else: # keep going left, resetting right by 1
                recur_search(arr, target, left_idx, middle_idx - 1, result, goLeft)
        else: # end or go further right
            if middle_idx == len(arr) -1 or arr[middle_idx + 1] != target:
                result[1] = middle_idx
            else:
                recur_search(arr, target, middle_idx + 1, right_idx, result, goLeft)


if __name__ == "__main__":

    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    target = 45
    #array = [5, 7, 7, 8, 8, 10]
    #target = 9

    print(searchForRange(array, target))
