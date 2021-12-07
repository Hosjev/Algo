class Solution:

    def isPalindrome(self, s: str) -> bool:
        # Main logic O(logN)
        left, right = 0, len(s) - 1
        while left <= right:
            while not left >= right and not s[left].isalnum():
                left += 1
            while not right <= left and not s[right].isalnum():
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else: return False

        return True


if __name__ == "__main__":
    s = "ra,cec ar"
    s = "a racecar"
    #s = " "
    #s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
