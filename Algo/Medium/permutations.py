"""
Write a function that takes in an array of ints and returns all possible permutations in no particular order. If the array is empty, return an empty.

Input:
    [1, 2, 3]

Output:


O(n)T | O(1)S
"""
import time


def getPermutations(array):
    perms = []
    permutation_loops(array, [], perms)
    return perms


def permutation_loops(array, current, perms):
    # This is the money. Where the subarray has been exhausted and we have a current
    if not len(array) and len(current):
        perms.append(current)
    else:
        for i in range(len(array)):
            sub_array = array[:i] + array[i+1:]
            # concatenate the current array iteration
            perm_local = current + [array[i]]
            permutation_loops(sub_array, perm_local, perms)


if __name__ == "__main__":

    array = [1, 2, 3, 4, 5]
    print(len(getPermutations(array)))
