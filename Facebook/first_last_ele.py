from typing import List



class Solution:
    def _binary(self, nums, L, R, target):
        M = (L + R) // 2
        if L >= R:
            if nums[M] == target: return M
            else: return
        if nums[M] == target:
            return M
        if nums[M] > target:
            return self._binary(nums, L, M - 1, target)
        else:
            return self._binary(nums, M + 1, R, target)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # EC
        if not bool(nums): return [-1, -1]
        present = self._binary(nums, 0, len(nums) - 1, target)
        if present is None: return [-1, -1]
        L, R = present, present
        while not L == 0 and (nums[L - 1] == target):
            L -= 1
        while not R == len(nums) - 1 and (nums[R + 1] == target):
            R += 1
        
        return [L, R]


if __name__ == "__main__":
    obj = Solution()
    n = [1,3,4,5,5,5,6,6,6,7]
    t = 6
    #n = [1]
    print(obj.searchRange(n, t))
