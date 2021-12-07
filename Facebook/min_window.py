class Solution:

    def _recurse(self, idx, s, pattern):
        if idx == len(pattern):
            return True
        if pattern[idx] in s:
            return self._recurse(idx + 1, s, pattern)
        else:
            return False

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return 0
        L, R = 0, 0
        min_window = float("inf")
        answer = ""
        pattern = "".join(sorted(t))
        while not R == len(s):
            local_slice = s[L:R+1]
            if self._recurse(0, set(local_slice), pattern) and \
                    not len(pattern) > len(local_slice):
                if (R-L+1) < min_window:
                    min_window = R-L+1
                    answer = s[L:R+1]
                L += 1
            else:
                R += 1
        return answer
        

if __name__ == "__main__":
    s = "abaacbab"
    t = "abc"
    print(Solution().minWindow(s, t))
    s = "aa"
    t = "aa"
    print(Solution().minWindow(s, t))
    s = "abc"
    t = "ac"
    print(Solution().minWindow(s, t))
