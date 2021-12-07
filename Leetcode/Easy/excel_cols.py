class Solution:

    def _convert_to_int(self, char):
        # Alpha intake
        alpha = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        return alpha.index(char.capitalize())


    def solve(self, string):
        answer = 0
        for i, char in enumerate(string):
            answer *= (i * 26)
            answer += self._convert_to_int(char)
        return answer


if __name__ == "__main__":
    print(Solution().solve("AB"))
    print(Solution().solve("ZY"))
    print(Solution().solve("fxshrxw"))

