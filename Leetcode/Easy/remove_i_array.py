class Solution:

    def _remove_val_array(self, nums, val):
        # Returns no object, alters in place
        # Edge Case(s)
        if val not in nums:
            return nums
        idx = 0
        nums.sort()
        while idx < len(nums):
            while idx < len(nums) and nums[idx] == val:
                nums.remove(val)
            idx += 1
        return


    def remove_val_array(self, nums, val):
        # Returns new object
        # Edge Case(s)
        if val not in nums: return nums

        # Prime
        pointer = len(nums) - 1
        nums.sort()
        for i, n in enumerate(nums):
            if n == val:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer -= 1
            if pointer <= i: break
        return nums[0:pointer + 1]


if __name__ == "__main__":
    a = [0, 0, 1, 1, 1, 2, 3, 4]
    a = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
    a = [0, 0, 1, 1]
    a = [1, 3, 4, 2, 5, 6, 7, 2, 2, 2, 2, 2]
    a = [2, 2]
    a = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
    a = [1, 3, 4, 2, 5, 6, 7, 2, 2, 2, 2, 2]
    t = 2
    obj = Solution()
    n = obj.remove_val_array(a, t)
    print(n)
