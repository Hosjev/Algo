class Solution(object):
    # This algorithm == in its entirety
    # IE--not true re.match()
    # *   and ? matches
    # 0-inf any / 1 any (not Python re rules)
    def isMatch(self, text, pattern):
        stack = {}
        def match_helper(i, j):
            if (i, j) not in stack:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    # Single match w/non regex rules is CURRENT, not prior
                    sm = i < len(text) and pattern[j] in {text[i], "?", "*"}
                    if pattern[j] == '*':
                        ans = match_helper(i, j+1) or sm and match_helper(i+1, j)
                    else:
                        ans = sm and match_helper(i+1, j+1)

                stack[i, j] = ans
            print(stack)
            return stack[i, j]

        return match_helper(0, 0)



s = "abbcb"
p = "ab*cb"

#s = "aa"
#p = "a*"

#s = "adceb"
#p = "*a*b" # T
#p = "a*b" # T
# 1st * matches empty, then a, 2nd * dce then b

s = "aaaab"
p = "?"

s = "acb"
p = "a*c"

s = "aa"
p = "*"
a = Solution()
print(a.isMatch(s, p))

s = "cb"
p = "?a"
a = Solution()
print(a.isMatch(s, p))

s = "adceb"
p = "a*b"
a = Solution()
print(a.isMatch(s, p))

s = "acdcb"
p = "a*c?b"
a = Solution()
print(a.isMatch(s, p))

s = "aa"
p = "a"
a = Solution()
print(a.isMatch(s, p))

s = "ab"
p = "?*"
a = Solution()
print(a.isMatch(s, p))
