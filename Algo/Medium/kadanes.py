"""
Write a function that takes in a non-empty array of ints and returns the maximum sum
that can be obtained by summing up all of the ints in a non-empty subarray of the input array.
A subarray can only contain adjacent numbers.

Input:
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Output:
    19 # 1...1

answer - O(N)T O(1)S
"""


def kadanesAlgorithm(array):
    running_sum = array[0]
    max_sum = array[0]

    for x in range(1, len(array)):
        # If the cumulative sum is > the current num, we stick w/it, or bail and start over
        running_sum = max((running_sum + array[x]), array[x])
        max_sum = max(max_sum, running_sum)
        print(max_sum)

    #print(comp_array)

    return max_sum



if __name__ == "__main__":

    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    #       [3, 8, -1, 1, 4, 2, 5, 9, 16, 18, 9, 15, 18, 19, 14, 18]


    print(kadanesAlgorithm(array))
