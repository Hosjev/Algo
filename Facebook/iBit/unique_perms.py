class Solution:
    # @param A : array of ints
    # @return nested array of arrays
    def permute(self, A):
        def permute_helper(subarray, placeholder, uniques):
            if len(placeholder) == len(A):
                uniques.append(placeholder)
                return uniques

            for idx in range(len(subarray)):
                # B/c we're breaking SA down, eventually 0 and -1 will match
                if len(subarray) > 1 and subarray[idx] == subarray[idx - 1]:
                    # If our eval isn't top level, cont
                    if not idx == 0:
                        continue
                local_placeholder = placeholder + [subarray[idx]]
                local_subarray = subarray[:idx] + subarray[idx + 1:]
                permute_helper(local_subarray, local_placeholder, uniques)

            return uniques


        # Main
        # Edge Case(s)
        if len(A) == 1: return [A]

        A.sort()
        return permute_helper(A, [], [])


A = [1, 1, 2]
print(Solution().permute(A))
