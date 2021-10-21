class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def palindrome_helper(L, R):
            p = False
            while True:
                if A[L] == A[R]:
                    p = True
                    if (L - 1 < 0) or (R + 1 == len(A)):
                        break
                    else:
                        L -= 1
                        R += 1
                else:
                    if p:
                        L += 1
                        R -= 1
                    break
            return (L, R) if p else (0, 0)


        # MAIN
        # Edge Case(s)
        if len(A) == 1: return 0
        if len(set(A)) == 1: return 0
        p_length = (0, 0)

        # Prime
        for i in range(1, len(A)):
            # Odd
            if i != len(A) - 1:
                p_length = palindrome_helper(i - 1, i + 1)
                if (p_length[1] - p_length[0]) + 1 == len(A): return 0
                if p_length[1] == len(A) - 1:
                    break
            # Even
            p_length = palindrome_helper(i - 1, i)
            if (p_length[1] - p_length[0]) + 1 == len(A): return 0
            if p_length[1] == len(A) - 1:
                break

        # Checks
        if p_length[1] != len(A) - 1: return len(A) - 1
        else: return len(A) - (p_length[1] - p_length[0] + 1)

A = "abede"
print(Solution().solve(A))
A = "abbb"
print(Solution().solve(A))
A = "abcd"
print(Solution().solve(A))
A = "aabb"
print(Solution().solve(A))
A = "oqycntornscygodzdctxnhoc"
print(Solution().solve(A))
A = "uvsghsfqzryzfcadvkmkr"
print(Solution().solve(A))
A = "qyvvfrvbdqriuhtasageryqysllgf"
print(Solution().solve(A))
