class Solution:
    """
    Input: string/string
    Output: bool
    """
    def isMatch(self, A, B):
        # Prime
        s = A
        pattern = B
        stack = {}

        def match_helper(i, j):
            if not (i, j) in stack:
                stars = pattern.count("*", j, len(pattern))
                stars *= 2
                if len(pattern[j:]) - stars > len(s[i:]): return False
                # Main eval/branch split
                if j == len(pattern):
                    result = i == len(s)
                else:
                    single = i < len(s) and pattern[j] in set(f"{s[i]}.")
                    if j+1 < len(pattern) and pattern[j+1] == "*":
                        result = match_helper(i, j + 2) or \
                                 single and match_helper(i + 1, j)
                    else:
                        result = single and match_helper(i + 1, j + 1)

                stack[i, j] = result

            return stack[i, j] # Ends or early exits return to previous caller

        # Main logic
        # Edge Case(s)
        if B.startswith("*") or not B: return False

        answer = match_helper(0, 0)
        return 1 if answer else 0

# TODO: make an isMatch iterative version
A = "ab"
B = ".*"
a = Solution()
print(a.isMatch(A, B))
