class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Priming
        minPositive = int()
        nums.sort()

        for integer in nums:
            # Ignore negs and non-negs
            if integer * -1 >= 0:
                continue
            # Eval
            if integer == minPositive:
                continue
            elif integer == minPositive + 1:
                minPositive = integer
            else:
                break

        return minPositive + 1

n = [0, 1, 1, 2, 2]
a = Solution()
print(a.firstMissingPositive(n))
