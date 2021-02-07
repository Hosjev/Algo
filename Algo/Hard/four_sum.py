"""
Write function that takes non-empty array of distinct ints and an int representing the target sum.
The function should find all quadruplets in the array that sum up to the target and return a 2D array of the quads.

Input:
    array = [ 7, 6, 4, -1, 1, 2 ]
    targetSum = 16
Output:
    [ [7, 6, 4, -1], [7, 6, 1, 2] ]

* note that the answer above is in order of the orig array

answer - O(N^2)T / O(N)S
"""

def fourNumberSum(arr, ts):
    # This doesn't work unless you for loop the outer arrays
    # to keep going inward until quad length exhausted
    # For ex: on len of 6, there'd be 2 outer loops
    # (len of array // 2) - 1 --this turns into a time complexity horror
    if len(arr) < 4: return []

    quads = []
    arr.sort()

    # We iterate twice through:
    #     1st time--L advances till inner array < 2
    #     2nd time--R decrements till inner array < 2
    # Inner iterations advance thru array until crossing over
    #     each other and incr/decr by 1 if <>

    for x in range((len(arr) // 2) - 1):
        # We advance outer Left first
        print(x, (len(arr) -x) -1)
        quads += sum_by_four(arr, ts, x, (len(arr) - x) - 1, direct = "L")
        # Now we advance outer right (decrement)
        quads += sum_by_four(arr, ts, x, (len(arr) - x) - 2, direct = "R")

    return quads


def sum_by_four(arr, ts, L, R, direct):
    i_quads = []
    inner_left = L + 1
    inner_right = R - 1
    while (R - L) > 2:
        if inner_left >= inner_right:
            if direct == "L": L += 1
            else: R -= 1
            inner_left = L + 1
            inner_right = R - 1
            continue
        inner_sum = (arr[L] + arr[inner_left] + arr[inner_right] + arr[R])
        if inner_sum < ts: # advance left
            inner_left += 1
        elif inner_sum > ts:
            inner_right -= 1
        else: # we matched
            i_quads.append([arr[L], arr[inner_left], arr[inner_right], arr[R]])
            # Advance both inner positions
            inner_left += 1
            inner_right -= 1

    return i_quads


def fourNumberSum(arr, ts):
    # This solution isn't Much better in TC and uses pairs and hash to store pairs
    # Outer loop iters at high level
    # Inner forward looks for sum matches
    # Inner backward forms the pairs

    sum_hash = {}
    quads = []

    for idx in range(len(arr)):
        for f_idx in range(idx + 1, len(arr)):
            pair = arr[idx] + arr[f_idx]
            diff = ts - pair
            if diff in sum_hash.keys():
                for x in sum_hash[diff]:
                    quads.append(x + [arr[idx], arr[f_idx]])
        for r_idx in reversed(range(0, idx)):
            rev_match = arr[idx] + arr[r_idx]
            if rev_match not in sum_hash.keys():
                sum_hash[rev_match] = [ [arr[idx], arr[r_idx]] ]
            else: # It IS
                sum_hash[rev_match].append([arr[idx], arr[r_idx]])

    return quads


if __name__ == "__main__":
    array = [ 7, 6, 4, -1, 1, 2 ]
    target_sum = 26
    target_sum = 16
    array = [ 5, 3, 2, -2, -3, -5 ]
    target_sum = 0
    array = [-10, -3, -5, 2, 15, -7, 28, -6, 12, 8, 11, 5]
    target_sum = 20

    print(fourNumberSum(array, target_sum))
