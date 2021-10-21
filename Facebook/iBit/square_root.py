class Solution(object):
    def mySqrt(self, x):
        L, R = 0, x
        while L <= R:
            M = L + ((R-L)//2)
            print(L,R,M)
            if (M * M) <= x < (M+1)*(M+1):
                return M
            elif x < M * M:
                R = M - 1
            else:
                L = M + 1


print(Solution().mySqrt(35))
print(Solution().mySqrt(36))
