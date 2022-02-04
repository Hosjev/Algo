class Solution:
    def validPalindrome(self, s: str) -> bool:
        def _recurse(L, R):
            if L >= R:
                return True
            if s[L] != s[R]:
                return False
            return _recurse(L + 1, R - 1)

        # Edge Case(s)
        if not s: return True

        # Prime
        L, R = 0, len(s) - 1
        mismatch = int()

        # Logic
        while L <= R:
            if mismatch > 1: return False
            if s[L] == s[R]:
                L += 1
                R -= 1
            else: # break on 1st mismatch
                mismatch += 1
                break

        # Since we're 1 off, this works
        if mismatch:
            left = _recurse(L + 1, R)
            right = _recurse(L, R - 1)
            return left or right

        return True


if __name__ == "__main__":
    s = "abcxdba"
    #s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    #s = "ebcbbececabbacecbbcbe"
    obj = Solution()
    print(obj.validPalindrome(s))
