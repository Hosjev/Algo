from typing import List



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Binary version?
        # at idx 4 (sum left = 10; 10 / len(L) = 2; sum R = 31; 31 / 2 = 15.5 -we know R by fraction)
        # at idx 3/4 EVEN (sum left = 6; 6 / 4 = 1.5; sum R = 24; 24 / 4 = 6 -we know R by whole)
        #                 R - (L = 9/2; R = 15/2) # on EVEN if neither whole -our num is BTW
        # Start missing
        if 0 not in nums: return 0

        # Prime
        nums.sort()
        # End missing
        if nums[-1] != len(nums): return len(nums)

        # Logic
        for i in range(1, len(nums)):
            if (nums[i - 1] + 2) == nums[i]:
                return nums[i] - 1


if __name__ == "__main__":
    n = [0,3,1]
    n = [0,1,2,3,4,5,6,7,9]
    n = [0,1,2,3,4,5,7,8]
    obj = Solution()
    print(obj.missingNumber(n))
