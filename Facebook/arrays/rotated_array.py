class Solution:
    def pivot_search(self, nums, L, R): 
        # Return index
        if L >= R:
            return
        M = (R + L) // 2
        if nums[M] > nums[M+1]:
            return M + 1 
        ans = self.pivot_search(nums, L, M)
        if not ans:
            return self.pivot_search(nums, M+1, R)
        else:
            return ans 

    def binary_search(self, L, R, pivot, nums, target):
        M = (R + L) // 2
        actual_M = (M + pivot) % len(nums)
        if L >= R: # EofS
            if nums[actual_M] == target:
                return actual_M
            else:
                return -1
        if nums[actual_M] == target:
            return actual_M
        elif nums[actual_M] > target:
            R = M - 1
        else:
            L = M + 1
        return self.binary_search(L, R, pivot, nums, target)

    def search(self, nums, target):
        # Return index of target
        pivot = self.pivot_search(nums, 0, len(nums) - 1)
        if not pivot: pivot = 0
        return self.binary_search(0, len(nums) - 1, pivot, nums, target)



if __name__ == "__main__":
    n = [4,5,6,7,0,1,2]
    t = 5
    n = [1, 3]
    print(Solution().search(n,t))
