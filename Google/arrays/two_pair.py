class Solution:
    def findPairSum(self, array, total):
        # [1, 2, 4, 4]
        # {2: 0, 1: 1,  }
        cache = {}
        for idx, integer in enumerate(array):
            if integer in cache:
                value_pair_idx = cache[integer]
                return [integer, array[value_pair_idx]]
            else:
                my_diff = total - integer
                cache[my_diff] = idx

        return None


if __name__ == "__main__":
    a = [1,2,3,4,4]
    print(Solution().findPairSum(a, 8))
