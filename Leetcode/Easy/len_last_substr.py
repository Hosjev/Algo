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



if __name__ == "__main__":
    s = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s))
