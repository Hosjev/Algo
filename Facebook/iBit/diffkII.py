class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer bool 0/1 F/T
	def diffPossible(self, A, B):
            # This rhythm only works on sorted
            A_sorted = sorted(A)
            i = 1
            j = 0
            while not j >= len(A) and not i >= len(A):
                local_diff = (A_sorted[i]) - (A_sorted[j])
                if local_diff == B:
                    return 1
                elif local_diff < B:
                    i += 1
                else:
                    j += 1
                    if j == i: i += 1 

            return 0

A = (1, 5, 3)
B = 0
print(Solution().diffPossible(A, B))
