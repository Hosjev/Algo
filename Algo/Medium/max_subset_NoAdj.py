"""
Write a function that takes in an array of positive ints and returns the maximum
sum of non-adjacent ints.

Input:
    array = [75, 105, 120, 75, 90, 135]
Output:
    330 # 75 + 120 + 135

* Dynamic Programming
* recursive best answer
answer - O(N)T O(d)S --N=nodes, d=depth
"""


def maxSubsetSumNoAdjacent(array):

    if len(array) == 0: # Edge case no elements
        return 0
    elif len(array) == 1: # Edge case one element
        return array[0]
    elif len(array) == 2: # Edge case two elements
        return max(array)
    else:
        subsets = [0] * len(array)
        # First two elements in answer array are set to themselves
        subsets[0] = array[0]
        subsets[1] = max(array[0], array[1])

        # Now we call the recursive function to iterate
        return maximum_subset(array, subsets, 2)
 


def maximum_subset(array, subsets, position):
    if position > len(array)-1:
        return subsets[-1]

    # Start position always index 2
    # ...compare values
    #    array current index + previous accumulation in subset
    #    to previous accumulation in subset
    max_sum = max( (array[position] + subsets[position-2]), subsets[position-1] )
    subsets[position] = max_sum
    return maximum_subset(array, subsets, position+1)


def max_subset(array, max_set, position):
    # Exit at the first sign we've exhausted the array
    # TO fix this, go backward as you go forward.
    if position > len(array)-1:
        return max_set

    if position == len(array)-1:
        max_set += array[position]
        position += 1
    else:
        if array[position] > array[position+1]:
            winner_idx = position
        else:
            winner_idx = position + 1
        max_set += array[winner_idx]
        position = winner_idx + 2

    return max_subset(array, max_set, position)
    

if __name__ == "__main__":

    array = [75, 105, 120, 75, 90, 135]
    array = [4, 3, 5, 200, 5, 3] # 207
    array = [4, 200, 5] # 200


    print(maxSubsetSumNoAdjacent(array))
