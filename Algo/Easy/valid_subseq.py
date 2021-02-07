"""
Given 2 non-empty arrays of ints, function that determines whether 2nd array is subsequence
of 1st.
Input:
    [5, 1, 22, 25, 6, -1, 8, 10]
    [1, 6, -1, 10]
Output:
    True/False

*subsequence of array is set of numbers that aren't necessarily adjacent in array
 but are in same ORDER as in array.
*a single number is a valid "sequence"
*I'm looking for patterns
"""

import time


def isValidSubsequence(array, sequence):
    # The ENTIRE SS needs to be in ORDER for True
    index = 0
    la = len(array)
    for x in range(len(sequence)): # O(M)
        # Edge case
        if index >= la: return False
        for y in range(index, la): # O(N) approaching log
            if sequence[x] == array[y]: # O(1)
                index = y+1 # O(1)
                break
            if y == la-1: return False # O(1)
    return True



if __name__ == "__main__":
    arr = [5, 1, 22, 25, 6, -1, 8, 10]
    arr6= [5, 5, 5, 5]
    arr8= [1, 1, 6, 1]
    sub = [1, 6, -1, 10]
    sub2 = [6]
    sub3 = [6, 1]
    sub4 = [1, 6, 22, -1]
    sub5 = [5, 1, 22, 25, 6, -1, 8, 10]
    sub6 = [5, 5, 5]
    sub7 = [5, 1, 22, 22, 25, 6, -1, 8, 10]
    sub8 = [1, 1, 1, 6]

    print(isValidSubsequence(arr, sub2))
    print(isValidSubsequence(arr, sub3))
    print(isValidSubsequence(arr, sub4))
    print(isValidSubsequence(arr, sub5))
    print(isValidSubsequence(arr6, sub6))
    print(isValidSubsequence(arr, sub7))
    print(isValidSubsequence(arr8, sub8))
