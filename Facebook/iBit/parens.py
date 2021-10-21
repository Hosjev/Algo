class Solution:
    def generateParenthesis(self, n: int) -> list:
        result = []
        def paren_helper(str_obj, L, R):
            if len(str_obj) == 2 * n:
                result.append("".join(str_obj))
                return
            if L < n:
                str_obj.append("(")
                paren_helper(str_obj, L+1, R)
                str_obj.pop()
            if R < L:
                str_obj.append(")")
                paren_helper(str_obj, L, R+1)
                str_obj.pop()
            return result

        # Main
        return paren_helper([], 0, 0)

n = 1
print(Solution().generateParenthesis(n))
