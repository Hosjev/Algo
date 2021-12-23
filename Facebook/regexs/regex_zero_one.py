class Solution:
    # @param A : string
    # @param B : string
    # @return an integer bool 0 False 1 True
    # TODO: optimize a length btw A/B, can I do it w/o waiting for a return from stack?
    def isMatch(self, A, B):
        # Priming
        stack = {}
        s = A
        pattern = B

            
        def match_helper(i, j):
            # Moving T/F up stack, we favor T w/or
            if (i, j) not in stack:
                # Early exit opportunity
                star_count = pattern.count("*", j, len(pattern))
                if len(pattern[j:]) - star_count > len(s[i:]):
                    return False
                if j == len(pattern):
                    answer = i == len(s)
                else: # single match set
                    sm = i < len(s) and pattern[j] in {s[i], "?", "*"}
                    if j < len(pattern) and pattern[j] == "*": # fork/spawn
                        answer = match_helper(i, j + 1) or \
                                 sm and match_helper(i + 1, j)
                    else: # move each
                        answer = sm and match_helper(i + 1, j + 1)
                # Store answer in stack as tuple
                stack[i, j] = answer
            return stack[i, j]

        # Edge Case(s)
        # Assuming B is pattern
        # NO pattern
        # Pattern all stars
        if not B: return 0
        if len(B) == B.count("*", 0, len(B)): return 1

        answer = match_helper(0, 0)
        return 1 if answer else 0



# InterviewBit ?*
A = "a" * 800
B = "*"
B += "a" * 801
#A = "aaaaaaaaaaaaaaaaaaaa"
#B = "*aaaaaaaaaaaaaaaaaaaaa"
#A = "aaa"
#B = "a*************"
a = Solution() # 1
print(a.isMatch(A, B))

#A = "ab"
#B = "?*"
#a = Solution() # 1
#print(a.isMatch(A, B))

#A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#B = "*b"
#a = Solution() # 0
#print(a.isMatch(A, B))

#A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#B = "a**************************************************************************************"
#a = Solution() # 1
#print(a.isMatch(A, B))
