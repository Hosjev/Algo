from typing import List


class Solution:
    """ O(N) """

    def subarraySum(self, nums: List[int], k: int) -> int:
        # Edge Case
        if not bool(nums): return 0
        
        # Prime
        accu_sum = int()
        answer_int = int()
        cache = {0: 1}

        # Main logic
        for integer in nums:
            accu_sum += integer
            key = accu_sum - k
            # Have I already reached this difference?
            if key in cache:
                answer_int += cache[key]
            # Is the current sum already present?
            # (useful for Long arrays where accumulations build up)
            if accu_sum in cache:
                cache[accu_sum] += 1
            else:
                cache[accu_sum] = 1

        return answer_int


if __name__ == "__main__":
    obj = Solution()
    print(obj.subarraySum([1,2,3], 3))
    print(obj.subarraySum([1,1,1], 2))
    print(obj.subarraySum([1,1], 2))
    print(obj.subarraySum([1], 2))
    print(obj.subarraySum([3,4,7,2,-3,1,4,2], 7))
