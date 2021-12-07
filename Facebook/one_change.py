class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == "" and t == "": return False
        if abs(len(s) - len(t)) >= 2: return False
        # Prime
        s_sort = sorted(s)
        t_sort = sorted(t)
        diff, si, ti = 0, 0, 0
        # Handle equal length
        if len(s) == len(t):
            for i in range(len(s)):
                if s_sort[i] != t_sort[i]:
                    diff += 1
        # Handle s < t
        if len(s) < len(t):
            if not s: return True
            while not si == len(s):
                if s_sort[si] != t_sort[ti]:
                    diff += 1
                    ti += 1
                else:
                    si += 1
                    ti += 1
            if diff == 0: diff += 1
        # Handle s < t
        if len(s) > len(t):
            if not t: return True
            while not ti == len(t):
                if s_sort[si] != t_sort[ti]:
                    diff += 1
                    si += 1
                else:
                    si += 1
                    ti += 1
        
        print(diff)
        return diff <= 1


if __name__ == "__main__":
    s = "ab"
    t = "acb"
    s = "ab"
    t = "a"
    print(Solution().isOneEditDistance(s, t))
