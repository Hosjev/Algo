class Solution(object):
    # This algorithm == in its entirety
    #   and PURE in terms of metacharacters
    # IE--not true re.match()
    # dot  == any single char
    # star == preceding char 0=>inf
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    sm = i < len(text) and pattern[j] in {text[i], '.'}
                    # For star/asterisk we must look ahead and fork here
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or sm and dp(i+1, j)
                    else:
                        ans = sm and dp(i+1, j+1)

                memo[i, j] = ans
                print(memo)
            return memo[i, j]

        # Due to excessive recursion, this is an edge case
        if pattern.startswith("*"): return False

        return dp(0, 0)



s = "aaa"
p = "a*a"

s = "abbcb"
p = "ab*cb"

s = "aa"
p = "*"

s = "aab"
p = "a*b"

s = "ab"
p = "ab*"
a = Solution()
print(a.isMatch(s, p))
