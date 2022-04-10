from typing import List


class Solution:
    def _recurse(self, n, L, R, placeholder, result):
        if len(placeholder) == n * 2:
            result.append("".join(placeholder))
            return
        # Go L as far as poss
        if L < n:
            placeholder.append("(")
            self._recurse(n, L+1, R, placeholder, result)
            placeholder.pop()
        # Go R
        if R < L:
            placeholder.append(")")
            self._recurse(n, L, R+1, placeholder, result)
            placeholder.pop()
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        # EC
        if not n: return []
        # Recurse on L/R
        return self._recurse(n, 0, 0, [], [])


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(1))
