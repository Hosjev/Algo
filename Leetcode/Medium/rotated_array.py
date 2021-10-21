class Solution:
    def search_rotate(self, nums, target):
        def classic_bs(L, R, array, target):
            if L >= R:
                if array[L] == target:
                    return L
                else:
                    return -1
            middle = L + ((R-L) // 2)
            if array[middle] == target:
                return middle
            elif array[middle] > target:
                L, R = L, middle - 1
            else:
                L, R = middle + 1, R
            return classic_bs(L, R, array, target)

        def pattern_bs(L, R):
            # Return index
            if L == R:
                return
            M = (L + R) // 2
            if nums[M] > nums[M+1]:
                return M + 1
            left = pattern_bs(L, M)
            if not left:
                return pattern_bs(M+1, R)
            else:
                return left


        # Main
        offset = pattern_bs(0, len(nums)-1)
        if not offset:
            offset = 0
        nums.sort()
        position = classic_bs(0, len(nums) - 1, nums, target)

        return -1 if position == -1 else (position + offset) % len(nums)




n = [5, 1, 3]
t = 1
print(Solution().search_rotate(n, t))
