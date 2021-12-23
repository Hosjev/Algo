class Solution:

    def _bin_search(self, nums, L, R):
        if L == R:
            return L
        M = (L + R) // 2
        if nums[M] > nums[M + 1]:
            return self._bin_search(nums, L, M)
        # Possible peak to the right
        return self._bin_search(nums, M + 1, R)

    def findPeakElement(self, nums):
        # Return any peak index [3, 6, 5] = 1
        # Run O(log n) in rhythm of edging L/R toward higher #
        if not len(nums) > 2: return -1
        peak = self._bin_search(nums, 0, len(nums) - 1)
        return -1 if peak == len(nums) - 1 else peak


if __name__ == "__main__":
    n = [1,1,1,2,1,1,1,1,1] # example that breaks this rhythm by favoring R
    #n = [1, 1, 1, 1]
    #n = [1, 1]
    #n = [1, 3, 5, 4]
    print(Solution().findPeakElement(n))
