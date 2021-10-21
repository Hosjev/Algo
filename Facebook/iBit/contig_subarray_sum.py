class Solution:
    def maxSubArray(self, A):
        # Edge Case(s)
        if len(A) == 1: return A[0]

        # The key here is use 2 vars
        local_max = final_max = A[0]
        for i in A[1:]:
            local_max = max(i, i + local_max)
            final_max = max(final_max, local_max)

        return final_max



n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(n))
