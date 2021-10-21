class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def paren_helper(N):
            if N == 0: return ['']
            result = []
            for i in range(N):
                for L in paren_helper(i):
                    for R in paren_helper(N-1-i):
                        result.append(f'({L}){R}')
            return result
        return paren_helper(n)


s = Solution()
print(s.generateParenthesis(3))
