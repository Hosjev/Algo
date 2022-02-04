class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Edge Case
        if len(s) == 0:
            return 0
        import re
        s = " " + s + " "
        pattern = re.compile(r'\s?([\w]+)\s+')
        print(s)
        return pattern.findall(s)
        #return len(pattern.findall(s)[-1])

    def lengthOfLastWord(self, s: str) -> int:
        # EC

        # Prime
        idx = len(s) - 1
        answer = int()
        s = s.strip()

        # Logic
        while idx > 0:
            char = s[idx]
            if char.isspace():
                return answer
            elif char.isalpha():
                answer += 1
            idx -= 1

        return answer





if __name__ == "__main__":
    s = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s))
