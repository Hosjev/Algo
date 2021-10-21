class Solution:
    def diffPossible(self, A, B) -> int: 
        # Edge Case(s)
        i = 1
        j = 0
        while not i == len(A):
            local_diff = (A[i]) - (A[j])
            if local_diff == B:
                return 1
            elif local_diff < B:
                i += 1
            else:
                j += 1
                if j == i: i += 1

        return 0


A = [1, 3, 3, 14, 15]
#A = [1,1,1,1,1,1]
print(Solution().diffPossible(A, 0))
