class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: return nums
        if (k % len(nums)) == 0: return nums
        
        nums = nums[len(nums) - (k % len(nums)):] + nums[:len(nums) - (k % len(nums))]
        return nums


nums = [2, 4, 6, 8, 9]
nums = [-1, -100, 3, 99]
nums = [1,2,3,4,5,6,7,8,9]
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(Solution().rotate(nums, k))
