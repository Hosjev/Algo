class Solution:
    def two_sum(self, arr, target):
        cache = {}
        for i, num in enumerate(arr):
            diff = target - num
            # Match
            if num in cache:
                return [i, cache[num]]
            cache[diff] = i


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
    obj = Solution()
    print(obj.two_sum([2,7,11,15], 9))
    print(obj.two_sum([-1,-2,-3,-4,-5], -8))
    print(obj.two_sum([3,3], 6))
    print(obj.two_sum([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1], 11))
