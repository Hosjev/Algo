class Solution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        # We'll never have len of 2
        #   cause we're guaranteed 1 non-dup amoungst dups
        #   so 1, 3+
        nums.sort()
        idx = 0
        while idx != len(nums) - 1:
            if nums[idx] != nums[idx + 1]:
                return nums[idx]
            idx += 2
        return nums[idx]
        

if __name__ == "__main__":
    n = [1, 2, 2]
    #n = [1, 1, 2]
    print(Solution().singleNumber(n))
