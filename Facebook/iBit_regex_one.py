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
                # Early Exit(s) (excl possible stars/pure chars)
                stars = pattern.count("*", j, len(pattern))
                if len(pattern[j:])-stars > len(s[i:]):
                    return False
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
        # Pattern empty
        # Pattern full of stars (this TC would be awful)
        if len(B) == 0: return 0
        if B.count("*", 0, len(B)) == len(B): return 1

        # Push our winning answer up the stack
        stack = match_helper(0, 0)
        return 1 if stack else 0



# TODO: make match_helper iterative version
A = "accfxysb"
B = "a*fxysb"
s = Solution() # 1
print(s.isMatch(A, B))

A = "a" * 800
B = "*"
B += "a" * 801
a = Solution() # 0
print(a.isMatch(A, B))

A = "ab"
B = "?*"
a = Solution() # 1
print(a.isMatch(A, B))

A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
B = "*b"
a = Solution() # 0
print(a.isMatch(A, B))

A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
B = "a**************************************************************************************"
a = Solution() # 1
print(a.isMatch(A, B))

