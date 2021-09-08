"""
There's a stack of NN inflatable discs, with the ith disc from the top having an initial radius of Ri 
inches.

The stack is considered unstable if it includes at least one disc whose radius is larger than or equal to that of the disc directly under it. In other words, for the stack to be stable, each disc must have a strictly smaller radius than that of the disc directly under it.

As long as the stack is unstable, you can repeatedly choose any disc of your choice and deflate it down to have a radius of your choice which is strictly smaller than the disc’s prior radius. The new radius must be a positive integer number of inches.

Determine the minimum number of discs which need to be deflated in order to make the stack stable, if this is possible at all. If it is impossible to stabilize the stack, return -1−1 instead.

"""
from typing import List


def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    """
    Example 1
    N = 5
    R = [2, 5, 3, 6, 5]
    R = [x, x, 3, x, 5]
    R = [2, 5, 3, 13, 14]
    Ans = 3

    Example 2
    N = 3
    R = [100, 100, 100]
    Ans = 2

    Example 3
    N = 4
    R = [6, 5, 4, 3]
    Ans = -1

    Recursive solution?
    """
    
    return 0


def horribleIterative(R) -> int:
    # The time complexity Sux
    # Edge case
    if R[-1] < len(R): return -1

    min_value = int()
    idx = 0
    discs = [0 for x in R]

    while not (idx >= len(R)):
        # if our newly established minumum value is greater than current
        print(f"...currently at index {idx}")
        if min_value >= R[idx]:
            # update answer
            discs[idx] = 1
            # change prior to myself minus 1
            R[idx - 1] = R[idx] - 1
            # essentially staring over
            idx = 1
            # reset min value to prior
            min_value = R[0]
        else: # best case, less than
            # adv
            min_value = R[idx]
            idx += 1

    result = sum(discs)

    return result


def backwardIterative(R) -> int:
    # The time complexity better
    # Edge case
    if R[-1] < len(R): return -1

    max_value = R[-1]
    idx = len(R) - 2 # next to last
    changes = int()

    while (idx > -1):
        # simply update max values if needed
        if max_value <= R[idx]:
            # set array value
            R[idx] = max_value - 1
            changes += 1
        max_value = R[idx]
        idx -= 1

    print(R)

    return changes if (changes > 0 and R[0] > 0) else -1


if __name__ == "__main__":
    #print(horribleIterative([2, 5, 3, 6, 5]))
    #print(horribleIterative([6, 5, 4, 3]))
    #print(horribleIterative([6, 5, 4, 4]))
    #print(horribleIterative([100, 100, 100]))
    print(backwardIterative([2,5,3,6,5]))
    print(backwardIterative([6,5,4,3]))
    print(backwardIterative([100,100,100]))
    print(backwardIterative([6,5,4,4]))
    print(backwardIterative([1,1,3,4]))
    print(backwardIterative([1]))
