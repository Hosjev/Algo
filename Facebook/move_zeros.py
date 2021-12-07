from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # EC
        if not bool(nums) or \
           len(nums) == 1 or \
           set(nums) == set([0]):
               return nums

        # Prime
        try:
            zero_P = min([i for i,e in enumerate(nums) if not e])
            int_P = min([i for i,e in enumerate(nums) if e])
        except ValueError:
            return nums

        # Main Logic
        while int_P < len(nums) and zero_P < len(nums):
            while zero_P >= int_P and int_P < len(nums) - 1:
                int_P += 1
            nums[int_P], nums[zero_P] = nums[zero_P], nums[int_P]
            zero_P += 1
            while zero_P < len(nums) and nums[zero_P]: # Zero int
                zero_P += 1
            int_P += 1
            while int_P < len(nums) and not nums[int_P]: # Real int
                int_P += 1

        return nums



if __name__ == "__main__":
    print(Solution().moveZeroes([0, 1, 0, 3, 12, 0]))
    print(Solution().moveZeroes([0, 1]))
    print(Solution().moveZeroes([1, 0]))
    print(Solution().moveZeroes([2, 1]))
    print(Solution().moveZeroes([1, 0, 1]))
