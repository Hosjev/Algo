def two_sum(array, target):
    """
    O(N) -- worst case
    """
    for i in range(len(array)):
        difference = target - array[i]
        if difference in array and \
            array.index(difference) != i:
                return [array[i], difference]


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))

    print(two_sum([-1,-2,-3,-4,-5], -8))
