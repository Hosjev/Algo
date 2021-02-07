"""
Write a function that takes in an array of ints and returns the greatest sum acheived by a strictly increasing subsequence.

Input:
    array = [10, 70, 20, 30, 50, 11, 30]

Output:
    110 [10, 20, 30, 50]

* of the 2 solutions below, the second is the same as the first rhythmically, except the 2nd uses DP
* this problem requires storing more auxillary arrays keeping track of max's and their indices

answer - O(N^2)T / O(N^2)S
"""


def maxSumIncreasingSubsequence(array):
    """
    This rhythm looks backward through dict keys
    but only at previous numbers. We iterate forward
    looking back at less than rather than greater.
        {(10, 0): [[70], [20, 30, 50], [11, 30]], 
         (70, 1): [], 
         (20, 2): [[30, 50], [30]], 
         (30, 3): [[50]], 
         (50, 4): [],
         (11, 5): [[30]], 
         (30, 6): []}
    """

    if len(array) == 1:
        return [ array[0], array ]

    # Our keys HAVE to be (value, index) due to duplicates and
    # the nature of dicts with unique keys.
    SS_hash = { (array[idx], idx): [] for idx in range(len(array)) }
    hash_keys = list(SS_hash.keys())

    for idx in range(1, len(array)):
        for h_idx in reversed(range(idx)):
            num = array[idx] # My actual number in the array
            key = hash_keys[h_idx] # We always start with -1 of num
            if num > key[0]: # If 70 > 10
                match = False
                for SS_idx in range(len(SS_hash[key])): # SS is a list
                    SS = SS_hash[key][SS_idx]
                    if SS[-1] < num:
                        SS_hash[key][SS_idx].append(num) # hash[key][0].app
                        match = True
                        cand_arr = [key[0]] + SS_hash[key][SS_idx]
                        win_sum, win_array = check_max_sum(win_sum, cand_arr, win_array)
                if not match:
                    SS_hash[key].append([num])
                    win_sum, win_array = check_max_sum(win_sum, [key[0], num], win_array)
        # Last sum check on idx itself
        win_sum, win_array = check_max_sum(win_sum, [array[idx]], win_array)

    print(SS_hash)
    return [win_sum, win_array]


def maxSumIncreasingSubsequence(array):
    # The Dynamic Programming version

    if len(array) == 1:
        return [ array[0], array ]

    # Store the max sum which we'll use last
    # Value 0; index 1
    max_sum = (array[0], 0)

    # The accumulated sums primed with "self"
    final_sums = [x for x in array]
    
    # The storing of indices
    indices = [None] * len(array)

    # Move forward through the array starting at one
    # then looking at all previous entries starting at zero
    for idx in range(1, len(array)):
        match = None
        for p_idx in range(idx): # 0 up to myself
            if array[p_idx] < array[idx]:
                if match is not None:
                    if final_sums[p_idx] > final_sums[match]:
                        match = p_idx
                else: match = p_idx

        # If we had matches on less than, evaluate them
        if match is not None: # we point to ourself
            possible_sum = array[idx] + final_sums[match]
            # Sanity check for negative numbers
            if array[idx] > possible_sum:
                final_sums[idx] = array[idx]
            else:
                final_sums[idx] = possible_sum
                indices[idx] = match

        # Update max for this round
        max_sum = round_winner(max_sum, final_sums, idx)

    # Finally, build array from indices
    temp_arr = []
    i = max_sum[1]
    while i is not None:
        temp_arr.append(array[i])
        i = indices[i]

    return [sum(temp_arr), sorted(temp_arr)]


def round_winner(max_sum, final_sums, idx):

    if final_sums[idx] > max_sum[0]:
        max_sum = (final_sums[idx], idx)

    return max_sum


def check_max_sum(arr, arr2, mSum):
    pass



if __name__ == "__main__":

    array = [10, 70, 20, 30, 50, 11, 30]
    #array = [-1, 1] # 1
    #array = [-5, -4, -3, -2, -1] # -1
    #array = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]
    #array = [1]
    #array = [5, 4, 3, 2, 1]
    #array = [1,2,3,4,5]
    #array = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #array = [-1, 1] # 1

    print(maxSumIncreasingSubsequence(array))
