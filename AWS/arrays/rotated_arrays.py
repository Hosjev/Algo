from typing import List


class Solution:
    def _binary_offset(self, L, R, nums):
        # Establish middle
        middle = (R+L) // 2
        # Eval left
        if nums[middle] < nums[L]:
            if nums[middle] < nums[middle-1]: return middle
            return self._binary_offset(L, middle-1, nums)
        elif nums[middle] > nums[R]:
            if nums[middle] > nums[middle+1]: return middle+1
            return self._binary_offset(middle+1, R, nums)
        else: # take left!
            return L
        
    def _binary_search(self, L, R, nums, offset, target):
        if R == L:
            real_R = (R+offset) % len(nums)
            if nums[real_R] != target: return -1
            else: return real_R
        pure_mid = ((R+L) // 2)
        middle = pure_mid + offset % len(nums)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return self._binary_search(L, pure_mid-1, nums, offset, target)
        else: # right
            return self._binary_search(pure_mid+1, R, nums, offset, target)

    def search(self, nums: List[int], target: int) -> int:
        # Grab offset
        offset = self._binary_offset(0, len(nums)-1, nums)
        return self._binary_search(0, len(nums)-1, nums, offset, target)


if __name__ == "__main__":
    a = [8,9,0,1,2,3,4,5,6,7]
    #a = [7,8,9,0,1,2,3,4,5,6]
    #a = [1,0]
    print(Solution().search(a, 6))
