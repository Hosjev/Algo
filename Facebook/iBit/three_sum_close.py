class Solution:
    def threeSumClosest(self, A, B):
        # Edge Case(s)
        if len(A) == 3: return sum(A)

        # Prime
        closest = float("-inf")
        A.sort()

        for pointer in range(len(A) - 2):
            L = pointer + 1
            R = len(A) - 1
            while L < R:
                local_sum = A[pointer] + A[L] + A[R]
                print(local_sum)
                if B == local_sum: return local_sum
                if abs((B) - (local_sum)) < abs((B) - (closest)):
                    closest = local_sum
                if local_sum < B:
                    L += 1
                else:
                    R -= 1


        return closest


A = [-1, 2, 1, -4]
#A = [-9, -8, -8, -8, -7, 1, 2, 2, 2, 3]
#A = [-6, -4, -4, -4, -4, -3, -3, -2, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 9, 9, 10]
B = 1
print(Solution().threeSumClosest(A, B))
