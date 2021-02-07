"""
Write a function that takes in an array of unique ints and returns its powerset.

The powerset P(X) of a set X is the set of all subsets of X. For example, the powerset of [1, 2] is [ [], [1], [2], [1, 2] ]

Input:
    [1, 2, 3]

Output:
    [ [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3] ]


O(n)T | O(1)S
"""
import time


# A recursive version using sub arrays
def powerset(array):
    current = []
    return power_subs([], array)


def power_subs(current, subset):
    if subset:
        return power_subs(current, subset[1:]) + power_subs( current + [subset[0]], subset[1:] )
    return [current]
# #####################################


# An iterative version using bits
def subsets(array):
    # Empty list to store sets
    sets = []

    # This is essentially our powerset math P(2^S)
    # So an array of 3 has 8 solutions, an array of 4 has 16, 5 has 32, etc
    # for i in 0,1,2,3,4,5,6,7 (for 3)
    # Then iterate thru index for each bit match
    # Shifting the index left gets a true bit comparison
    # Zero is my empty list b/c bitwise AND fails with no matches
    # One bit is in index 0 (shifted left); Two bit is in index 1 (shifted left)
    # Three is in zero (shifted left) and in one (shifted left)
    # The question is really: is my index (shifted left/binary representation) in my binary iteration
    # At 7 (0000-0111) all of my bits are present 1 (0000-0001) 2 (0000-0010) 4 (0000-0100)
    for i in range(1 << len(array)): # Or 2**len(array)
        subset = [ ]
        for bit in range(len(array)):
            if bit_set(i, bit):
                subset.append(array[bit])
        print("current subset:", subset)
        sets.append(subset)
    return sets


def bit_set(num, bit):
    # Num is my run through of possible subsets, bit is my list index
    return num & (1 << bit) > 0
################################


# A ridiculous cheat
from itertools import combinations
def subsets_combos(array):
    ss = []
    for cardinality in range(len(array)+1):
        yield from combinations(array, cardinality)
####################


# An iterative version from Algo
def iter_powerset(array):
    # 1. iterate thru each num in arr
    # 2. add them to an auxilary arr called ssets
    # 3. at each pass of a number, the sset gets the # and the final answer
    #    further at each pass, the sset array is called and the current idx
    #    is added to our answer and sset
    # 4. Do we need the aux array?
    # O(2^N*N)T - O(2^N*N)
    subsets = []
    subsets.append([])
    for idx in range(len(array)):
        for sset in range(len(subsets)):
            time.sleep(.3)
            new_subset = subsets[sset] + [array[idx]]
            subsets.append(new_subset)
    return subsets
###################################


def recur_powerset(array, idx = None):
    # The same rhythm as above but done w/recursive calls
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        # This is our first return to subsets. IDX = -1
        return [ [] ]

    # Name the element we're working with in this iteration of the recursion
    element = array[idx]
    subsets = recur_powerset(array, idx - 1)

    # The callback for each index of our array
    # We iterate through the subsets, adding lists together
    # NOTE: the first callback is our last element processed on a return
    #       to subsets of [ [] ]. you CAN iterate on a nested empty list
    for s_idx in range(len(subsets)):
        current_subset = subsets[s_idx]
        subsets.append(current_subset + [element])

    # Finally, the return to the previous caller (which is idx - 1)
    return subsets


if __name__ == "__main__":

    array = [1, 2, 3]
    print(powerset(array))
    print("Bitwise:", subsets(array))
    for x in subsets_combos(array):
        print(x)

    #print(iter_powerset(array))
    #array = []
    print(recur_powerset(array))
