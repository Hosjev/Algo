class Solution:
	# @param A : list of integers
	# @return a list of integers
	def equal(self, A):
            def precedent(cur, new):
                if (new[0] < cur[0]) or \
                   (new[0] == cur[0] and new[1] < cur[1]) or \
                   (new[0] == cur[0] and new[1] == cur[1] and new[2] < cur[2]) or \
                   (new[0] == cur[0] and new[1] == cur[1] and new[2] == cur[2] and new[3] < cur[3]):
                    return True
                else: return False

            # Edge Case(s)
            if len(A) < 4: return []

            # Prime
            sum_hash = {}
            current = [float("inf")] * 4

            # of [0] if len(vals) > 2, take 1st pair and eval
            l = 0
            p = l + 1
            while l != len(A) - 1:
                while p != len(A):
                    pair = A[l] + A[p]
                    try:
                        sum_hash[pair].append([l, p])
                    except KeyError:
                        sum_hash[pair] = [[l, p]]
                    p += 1
                l += 1
                p = l + 1

            # Iter thru hash
            for k, v in sum_hash.items():
                if len(v) > 1:
                    left_pair = v[0]
                    for i in range(1, len(v)):
                        if (not left_pair[0] in v[i]) and (not left_pair[1] in v[i]):
                            if precedent(current, left_pair + v[i]):
                                current = left_pair + v[i]
                                break

            return current if not float("inf") in current else []


A = [3, 4, 7, 1, 2, 9, 8]
#A = [ 9, 5, 4, 9, 3, 6, 8, 7, 1, 2, 8, 7, 2, 9, 7, 1, 3, 9, 7, 8, 1, 0, 5, 5 ]
# [0, 1, 3, 22]

print(Solution().equal(A))
