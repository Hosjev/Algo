class Solution:

    def removeDuplicates(self, nums) -> int:
        # IN PLACE
        # [1, 1, 2] is [1, 2, _] or 2
        # [1, 2, 2, 3, 3, 4] is [1, 2, 3, 4, 3, 4]
        if len(nums) == 0: return nums
        static = 0
        moving = 0
        while not moving == len(nums):
            nums[static] = nums[moving]
            while not moving == len(nums) and \
                  nums[static] == nums[moving]:
                moving += 1
            static += 1
        return static


if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,2]))
    print(Solution().removeDuplicates([1,2]))
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
