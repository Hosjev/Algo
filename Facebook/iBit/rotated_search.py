class Solution:
    def search(self, A, B):
        def pattern_bs(L, R):
            # Return index
            if L == R:
                return
            M = (L + R) // 2
            if A[M] > A[M+1]:
                return M + 1
            left = pattern_bs(L, M)
            if not left:
                return pattern_bs(M+1, R)
            else:
                return left

        def classic_bs(L, R, temp):
            if L == R:
                if temp[L] == B:
                    return L
                else:
                    return -1
            M = (L + R) // 2
            if temp[M] == B:
                return M
            if temp[M] > B:
                R = M - 1
            else:
                L = M + 1
            return classic_bs(L, R, temp)

        # Main
        offset = pattern_bs(0, len(A)-1)
        if not offset:
            offset = 0
        temp = list(A)
        temp.sort()
        idx = classic_bs(0, len(temp) - 1, temp)
        return -1 if idx == -1 else (idx + offset) % len(A)


A = (4, 5, 6, 7, 0, 1, 2, 3)
B = 6
A = ( 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 )
B = 202

print(Solution().search(A, B))
