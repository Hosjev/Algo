"""
Write a function that takes in a SORTED array of distinct ints as well as a target int. The caveat is that the ints in the array have been shifted by some amount; in other words, they've been moved to the left or to the right by one or more positions. EX--[1, 2, 3, 4] might have turned into [3, 4, 1, 2].

The function should use a variation of the Binary Search algorithm to determine if the target int is contained in the array and should return its index if it is, otherwise -1.

Input:
    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 33
Output:
    8


answer - O(N^2)T / O(N)S
"""
import time


def shiftedBinarySearch(arr, target):
    """
    I must not understand this problem cause it seems easy.
    -write the binary search
    -do a little extra math while passing the subarray info
    -slice = [0:end]... and indices = real idx list
    -after calculating middle, calc its idx based on indices
    -or you could have an additional array whose length matches
     the array and stores indices as values, then pass those slices, too

    * you could start by dividing the arr in 2?
    * and deal with each half separately
    """
    # Store the original indices
    indices = [x for x in range(len(arr))]

    return recur_binary_search(arr, indices, target)


def recur_binary_search(arr, indices, target):
    # I'm making:
    #     -left/right/middle pointers
    #     -a subarray from the target eval
    #     -a new indices from that
    # Can I pass the original array? Then pass the L/R indices instead?
    left_idx = 0
    right_idx = len(arr) - 1
    middle_idx = (left_idx + right_idx) // 2

    # Lazy
    if len(arr) == 2:
        if target == arr[0]: return indices[0] 
        elif target == arr[1]: return indices[1]
        else: return -1
    elif len(arr) == 1: return indices[0] if arr[0] == target else -1
    elif len(arr) == 0: return -1
    if arr[middle_idx] == target: return indices[middle_idx]

    # One of these is sorted
    if arr[left_idx] < arr[middle_idx]:
        if target >= arr[left_idx] and target <= arr[middle_idx]:
            subarray, indices = get_left(arr, indices, left_idx, middle_idx)
        else:
            subarray, indices = get_right(arr, indices, middle_idx, right_idx)
    else:
        if target >= arr[middle_idx] and target <= arr[right_idx]:
            subarray, indices = get_right(arr, indices, middle_idx, right_idx)
        else:
            subarray, indices = get_left(arr, indices, left_idx, middle_idx)

    return recur_binary_search(subarray, indices, target)


def get_left(arr, indices, left_idx, middle_idx):
    new_arr = arr[left_idx:middle_idx+1]
    new_ind = indices[left_idx:middle_idx+1]
    return new_arr, new_ind


def get_right(arr, indices, middle_idx, right_idx):
    new_arr = arr[middle_idx:right_idx+1]
    new_ind = indices[middle_idx:right_idx+1]
    return new_arr, new_ind


def recur_binary_search_orig(arr, target_value):
    # This works on sorted array
    # But is NOT totally the Binary Search method
    # strictly it's Lidx + Ridx // 2 = middle
    middle_idx = len(arr) // 2
    if len(arr) == 0:
        return -1
    elif arr[middle_idx] == target_value:
        return arr[middle_idx], arr.index(target_value)
    else:
        if arr[middle_idx] < target_value:
            arr_slice = arr[middle_idx + 1:]
        elif arr[middle_idx] > target_value:
            arr_slice = arr[0:middle_idx]
        return recur_binary_search(arr_slice, target_value)
    


if __name__ == "__main__":

    array = [44, 45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 33

    print(shiftedBinarySearch(array, target))
