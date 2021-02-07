"""
Write function that takes an array of at least 3 ints, and w/o sorting the input array
returns a sorted array of the 3 largest ints from input.
Input:
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Output:
    [18, 141, 541]

* func should return dup ints if necessary, or present, ie: [10, 10, 12] from [10, 5, 9, 10, 12]
"""
import time

high = 0


def findThreeLargestNumbers(array):
    def rec_find(indx, high):
        if indx < len(array):
            item = array[indx]
            high = max(high, item)
            return rec_find(indx+1, high)
        return (indx, high)


    # The rec version O(N3+M3)
    def iter_find(high):
        for item in array:
            high = max(item, high)
        return high

    # The iter version O(N3+M3)
    res = []
    #for run in range(3):
        #item = iter_find(array[0])
        #(n, item) = rec_find(1, array[0])
        #res.insert(0, item)
        #array.remove(item)

    three = [None, None, None]
    for num in array:
        upd_L(three, num)
    return three


def upd_L(three, num):
    # For each item, compare its size to the largest first, working backward
    if three[2] is None or num > three[2]:
        shift(three, num, 2)
    elif three[1] is None or num > three[1]:
        shift(three, num, 1)
    elif three[0] is None or num > three[0]:
        shift(three, num, 0)

def shift(array, num, idx):
    # THEN, if your num equals that index greater than, go ahead and fill it in
    # else shift the other numbs to the LEFT
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
            print(f"...item being stored: {num, i}")
        else:
            print(f"...shift condition met: {num, i}")
            array[i] = array[i + 1]
            print(f"...: {array}")


if __name__ == "__main__":
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    #array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
    print(findThreeLargestNumbers(array))
