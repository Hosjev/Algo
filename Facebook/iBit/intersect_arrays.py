class Solution:
    def intersect(self, A, B):
        # Edge Case(s)
        if len(A) == 0 or len(B) == 0: return []

        # Prime
        result = []
        pA = pB = 0

        # Main
        while not (pA == len(A)) and not (pB == len(B)):
            if A[pA] == B[pB]:
                result.append(A[pA])
                pA += 1
                pB += 1
            elif A[pA] < B[pB]:
                pA += 1
            else:
                pB += 1

        return result


B = [0,1,3,5,6,7,9,9]
A = [2,3,3,4,5]
print(Solution().intersect(A, B))
