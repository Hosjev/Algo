from collections import Counter


class Solution:

    def minWindow(self, s, t):
        if not t or not s or \
            len(t) > len(s):
            return ""

        # Pattern by char count
        t_c = Counter(t)
        # Sliding window cache
        s_c = {}
        # Of what unique char (count excl)
        required = len(t_c)
        L, R, formed = 0, 0, 0
        min_len, answer = float("inf"), (None, None)

        while R < len(s):
            # Move R until we have our 1st set
            character = s[R]
            s_c[character] = s_c.get(character, 0) + 1
            if character in t_c and s_c[character] == t_c[character]:
                formed += 1
            # Move L until we break
            while L <= R and formed == required:
                character = s[L]
                if R - L + 1 < min_len:
                    min_len = (R - L + 1)
                    answer = (L, R)
                s_c[character] -= 1
                if character in t_c and s_c[character] < t_c[character]:
                    formed -= 1
                L += 1    
            R += 1    

        return "" if min_len == float("inf") else s[answer[0]:answer[1]+1]


if __name__ == "__main__":
    s = "abaacbab"
    t = "aabc"
    print(Solution().minWindow(s, t))
    s = "aa"
    t = "aa"
    print(Solution().minWindow(s, t))
    s = "abc"
    t = "ac"
    print(Solution().minWindow(s, t))
