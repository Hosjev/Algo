class Solution:
    """
    Input: string/string
    Ouput: bool => 1 - True; 0 - False
    """
    def isMatch(self, A, B):
        # Priming
        stack = {}
        s = A
        pattern = B

        def match_helper(i, j):
            # These keys will inevitably get mixed
            if (i, j) not in stack:
                if j == len(pattern): # End/leaf responses
                    level = i == len(s)
                else: # Eval (always len 1st to avoid IE) and advance...
                    single = i < len(s) and pattern[j] in set(f"{s[i]}?*")
                    if j < len(pattern) and pattern[j] == "*":
                        level = match_helper(i, j + 1) or \
                                single and match_helper(i + 1, j)
                    else:
                        level = single and match_helper(i + 1, j + 1)
                stack[i, j] = level
            return stack[i, j]

        # Edge Cases
        if len(B) == 0: return 0
        if B.count("*", 0, len(B)) == len(B): return 1

        # Push our winning answer up the stack
        stack = match_helper(0, 0)
        return 1 if stack else 0



# TODO: make match_helper iterative version
#       OR decorate with tail recursion
# Early Exit(s) (excl possible stars/pure chars) (add back later)
#stars = pattern.count("*", j, len(pattern))
#if len(pattern[j:])-stars > len(s[i:]):
#return False

A = "ab"
B = "a*b"
s = Solution() # 1
print(s.isMatch(A, B))

A = "ab"
B = "?*"
a = Solution() # 1
print(a.isMatch(A, B))
