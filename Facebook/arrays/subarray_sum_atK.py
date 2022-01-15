from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(N) using hashmap
        # Edge Case(s)
        if not bool(nums):
            if k == 0: return 1
            else: return 0

        # Prime
        result = int()
        accumulated = 0
        sum_hash = defaultdict(int)
        sum_hash[0] = 1

        # Logic
        for entry in nums:
            accumulated += entry
            past_accumulated = accumulated - k
            if past_accumulated in sum_hash:
                result += sum_hash[past_accumulated]
            sum_hash[accumulated] += 1

        return result


if __name__ == "__main__":
    n = [3,4,7,2,-3,1,4,2]
    obj = Solution()
    print(obj.subarraySum(n, 7))
