class Solution:
    def _recurse(self, idx, nums):
        if idx is None:
            idx = len(nums) - 1
        if idx < 0:
            return [[]]
        element = nums[idx]
        result = self._recurse(idx - 1, nums)
        for i in range(len(result)):
            result.append(result[i] + [element])
        return result

    def subsets(self, nums):
        # Return nested list
        # EC
        if not bool(nums): return [[]]

        # Logic
        return self._recurse(None, nums)


if __name__ == "__main__":
    obj = Solution()
    print(obj.subsets([1, 2, 3]))
