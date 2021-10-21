class Solution:
    # @param A : list of ints
    # @return list of lists
    def threeSum(self, A):
        # Edge Case(s)
        if len(A) < 3: return 0

        # Prime
        result = set()
        A.sort()

        # Main
        for pointer in range(len(A) - 2):
            L = pointer + 1
            R = len(A) - 1
            while L < R:
                local_set = (A[pointer], A[L], A[R])
                local_sum = sum(local_set)
                if local_sum == 0:
                    result.add(local_set)
                    L += 1
                    R -= 1
                elif local_sum < 0:
                    L += 1
                else:
                    R -= 1

        return [list(x) for x in result]



A = [-1, -1, -4, 0, 1, 2]
A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
A = [-5, -4, -4, -4, -3, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 3, 4, 4, 5]
A = []

print(Solution().threeSum(A))
