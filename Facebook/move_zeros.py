from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Move zeros RIGHT (for the record, this code gives me gas)
        # Edge Case(s) -- empty/len of 1/all 0's
        if not bool(nums) or \
           len(nums) == 1 or \
           set(nums) == set([0]):
               return nums
        if len(nums) == 2 and nums[0] == 0:
            nums[0], nums[1] = nums[1], nums[0]
            return nums

        # Prime
        try:
            zero = min([i for i,e in enumerate(nums) if not e])
            real = min([i for i,e in enumerate(nums) if e])
        except ValueError:
            return nums # no zero or no real

        # Main Logic
        while True:
            # Pre-swap, ensure positions are good
            # If our zero is already to the right
            while zero >= real and not real == len(nums) - 1:
                real += 1
            # Time to move pointers
            # If our zero is a real num
            while not zero == len(nums) - 1 and nums[zero]: # Zero int
                zero += 1
            # If our real is a zero
            while not real == len(nums) - 1 and not nums[real]: # Real int
                real += 1
            nums[real], nums[zero] = nums[zero], nums[real]
            if zero == len(nums) - 1 or real == len(nums) - 1: break

        return nums



if __name__ == "__main__":
    print(Solution().moveZeroes([0, 1, 0, 3, 12, 0]))
    print(Solution().moveZeroes([0, 1]))
    print(Solution().moveZeroes([1, 0]))
    print(Solution().moveZeroes([2, 1]))
    print(Solution().moveZeroes([1, 0, 1]))
    print(Solution().moveZeroes([0, 0, 1]))
    print(Solution().moveZeroes([1, 0, 0, 1]))
