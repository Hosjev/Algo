class Solution:
    # @param A: list ints (non-neg)
    # @return int
    def maxArea(self, A) -> int:
        # Edge Case(s)
        if len(A) <= 1: return 0

        # Prime
        L = 0
        R = len(A) - 1
        m_area = 0

        # Main
        while L <= R:
            shorter = min(A[L], A[R])
            local_max = (R - L) * shorter
            m_area = max(local_max, m_area)
            if A[L] < A[R]:
               L += 1
            else:
               R -= 1

        return m_area


A = [1, 5, 3, 3, 3, 4, 3]
print(Solution().maxArea(A))
