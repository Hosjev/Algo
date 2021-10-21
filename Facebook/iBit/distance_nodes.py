class Solution:
    def solve(self, A):
        # Prime
        # Parent pointer remains static
        # Child pointer moves
        # ::when our of "i" changes value, we add to depth count
        P = C = 0
        count = 1
        while P != len(A):
            try:
                if A[P] == A[C]:
                    C += 1
                else:
                    count += 1
                    P = C
            except IndexError:
                break

        return count


A = [-1, 0, 0, 0, 3]
print(Solution().solve(A))
