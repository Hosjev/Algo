from typing import List



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # EC
        if len(nums) < 3: return []

        # Prime
        nums.sort()
        anchor = 0
        L, R, = 1, len(nums) - 1
        result = set()

        # Logic
        while anchor < len(nums) - 2:
            while L < R:
                temp_sum = nums[anchor] + nums[L] + nums[R]
                if temp_sum == 0:
                    result.add((nums[anchor], nums[L], nums[R]))
                    L += 1
                    R -= 1
                    continue
                elif temp_sum < 0:
                    L += 1
                else:
                    R -= 1
            # advance
            anchor += 1
            L = anchor + 1
            R = len(nums) - 1

        return [list(i) for i in result]


if __name__ == "__main__":
    n = [-1,-1,0,2,1,-4]
    obj = Solution()
    print(obj.threeSum(n))
