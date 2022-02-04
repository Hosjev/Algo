class Solution:
    # @param A : string
    # @return string

    def _expand(self, L, R, s):
        left, right = L, R
        while left >= 0 and right < len(s) and \
                s[left] == s[right]:
                    left -= 1
                    right += 1
        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        # Edge Case(s)
        if len(s) == 1 or \
          len(set(s)) == 1:
              return s

        # Prime
        start, end = 0, 0

        for idx in range(len(s) - 1):
            # Odd / Even
            odd = self._expand(idx, idx, s)
            even = self._expand(idx, idx + 1, s)
            # Eval
            local = max(odd, even)
            if local > (end - start):
                start = idx - ((local - 1) // 2)
                end = idx + (local // 2)
            # Early exit
            if end == len(s) - 1: break

        return s[start:end+1]


if __name__ == "__main__":
    A = "abede"
    print(Solution().longestPalindrome(A))
    A = "abbb"
    print(Solution().longestPalindrome(A))
    A = "abcd"
    print(Solution().longestPalindrome(A))
    A = "aabb"
    print(Solution().longestPalindrome(A))
    A = "oqycntornscygodzdctxnhoc"
    print(Solution().longestPalindrome(A))
    A = "uvsghsfqzryzfcadvkmkr"
    print(Solution().longestPalindrome(A))
    A = "qyvvfrvbdqriuhtasageryqysllgf"
    print(Solution().longestPalindrome(A))
    A = "abababababababa"
    print(Solution().longestPalindrome(A))
