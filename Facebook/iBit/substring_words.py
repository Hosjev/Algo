class Solution:
	# @param A : string
	# @param B : tuple of strings
	# @return a list of integers
	def findSubstring(self, A, B):

            def helper(subarray, idx):
                if not subarray:
                    return True
                word = A[idx:idx+len(B[0])]
                if word in subarray:
                    word_idx = subarray.index(word)
                    local_subarray = subarray[:word_idx] + subarray[word_idx+1:]
                    return helper(local_subarray, idx+len(B[0]))
                else:
                    return False


            # Main
            # Edge Case(s)
            # Prime
            result = []
            i_chunk = len(B[0])
            t_chunk = i_chunk * len(B)
            starters = [x[0] for x in B]
            for idx, char in enumerate(A):
                if idx <= len(A) - t_chunk:
                    if helper(B, idx):
                        result.append(idx)

            return result


A = "barfoothefoobartheman"
B = ["foo", "bar"]
A = "aaaaaa"
B = ["aa", "aa"]
print(Solution().findSubstring(A, B))
