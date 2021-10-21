class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
            # Edge Case(s)
            # Prime
            d_hash = {}
            idx = 0
            # Outer add to hash
            while not idx == len(A):
                if A[idx] in d_hash:
                    return [d_hash[A[idx]][0], idx]
                diff = B - (A[idx])
                try:
                    d_hash[diff].append(idx)
                except KeyError:
                    d_hash[diff] = [idx]
                idx += 1

            return []

A = [2, 7, 11, 15]
B = 9
A = ( 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ) # 4, 8
#     0  1   2  3  4  5  6   7   8
B = -3
# 3, 7
print(Solution().twoSum(A, B))
