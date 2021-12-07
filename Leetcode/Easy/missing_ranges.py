class Solution:

    def _find_range(self, i, lower_stub, result):
        if i <= lower_stub:
            return i + 1
        local_range = [lower_stub]
        end = i - 1
        if (end - lower_stub) != 0:
            local_range.append(end)
        result.append(local_range)
        return i + 1

    def findMissingRanges(self, nums, lower, upper) -> list:
        # [0, 1, 3, 50, 75] sorted
        # [(2), (4,49), (51,74), (76,99)]
        lower_stub = lower
        result = []
        for i in nums:
            lower_stub = self._find_range(i, lower_stub, result)

        if lower_stub <= upper:
            lower_stub = self._find_range(upper + 1, lower_stub, result)

        return result


if __name__ == "__main__":
    n = [0, 1, 3, 50, 75]
    print(Solution().findMissingRanges(n, 0, 99))
