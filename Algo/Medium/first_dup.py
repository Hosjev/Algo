"""
Write a function that takes in an array of ints from 1 to nth. Return 1st duplicate int.

Input:
    input = [2, 1, 5, 2, 3, 3, 4]
Output:
    2

** can mutate input array
** however, sorting it breaks their rules
** we could calc all (2) matches then sum the indices? the lower wins
"""
import time


def firstDuplicateValue(array):
    # Write your code here.

    idx = 0
    min_index = float("inf")
    while (idx < len(array)):
        try:
            num_to_match = array[idx]
            sub_array = array[idx+1:]
            if num_to_match in sub_array:
                match_index = idx + sub_array.index(num_to_match) + 1
                min_index = min(min_index, match_index)
                # print(f"we have match at ending in {sub_array} idx {match_index}")
            # advance
            idx += 1
        except IndexError:
            # catch empty arrays
            return -1

    return -1 if min_index == float("inf") else array[min_index]


arr = [2, 1, 5, 2, 3, 3, 4]  # 2
#      0, 1, 2, 3, 4, 5, 6 = 7
arr = [2, 1, 5, 3, 3, 2, 4]  # 3
arr = [1, 2, 3, 4]
print(firstDuplicateValue(arr))
