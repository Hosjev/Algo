class Solution:

    def remove_dups_array(self, nums):
        # return list(set(nums))
        
        # Prime
        idx = 1
        nums.sort()

        # [1,2,3,4]
        # [1,1,2,2]
        # [1,1,1,1]
        while idx < len(nums):
            previous = nums[idx - 1]
            current = nums[idx]
            while idx < len(nums) and previous == nums[idx]:
                nums.remove(nums[idx]) # 1st occurrence
            idx += 1
        return nums



if __name__ == "__main__":
    a = [0, 0, 1, 1, 1, 2, 3, 4]
    obj = Solution()
    print(obj.remove_dups_array(a))
    a = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
    obj = Solution()
    print(obj.remove_dups_array(a))
    a = [1, 2, 2]
    obj = Solution()
    print(obj.remove_dups_array(a))
    a = [1, 1]
    obj = Solution()
    print(obj.remove_dups_array(a))
    a = [0]
    obj = Solution()
    print(obj.remove_dups_array(a))
