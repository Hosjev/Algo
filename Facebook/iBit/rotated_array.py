class Solution:
    def binary_search(L, R):
        # Return index
        if L == R:
            return
        M = (L + R) // 2
        if A[M] > A[M+1]:
            return M + 1
        ans = self.binary_search(L, M)
        if not ans:
            return self.binary_search(M+1, R)
        else:
            return ans


    def rotatedArray(self, A):
        # Main
        # Edge Case(s) pivot 0 % len
        if A[0] < A[-1] or len(A) == 1: return A[0]

        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return A[i]


if __name__ == "__main__":
    A = [3, 4, 5, 6, 7, 0, 1, 2]
    #A = [4, 5, 6, 7, 0, 1, 2]
    #A = [1]
    #A = [1, 0]
    print(Solution().rotatedArray(A))
