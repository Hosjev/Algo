from typing import List



class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # EC
        if len(nums) == 1: return nums

        # Prime
        of_left = [1] * len(nums)

        # Main
        # 1 - run thru nums and calc of left
        for L in range(1, len(nums)):
            of_left[L] = of_left[L - 1] * nums[L - 1]

        # 2 - run thru nums backward and calc of R/both
        right_multiplier = 1
        for R in range(len(nums) - 2, -1, -1):
            right_multiplier = right_multiplier * nums[R + 1]
            of_left[R] = of_left[R] * right_multiplier

        return of_left



if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelf([3,4]))
