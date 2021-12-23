class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # EC
        if len(s) * k == 0: return 0

        # Sliding window approach
        left, right = 0, 0
        max_length = float("-inf")
        while not right == len(s):
            local_set = s[left:right+1]
            if len(set(local_set)) <= k:
                max_length = max(max_length, len(local_set))
                right += 1
            else:
                left += 1

        return max_length


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstringKDistinct("ecebax", 2))
    print(Solution().lengthOfLongestSubstringKDistinct("eceeeebax", 2))
    print(Solution().lengthOfLongestSubstringKDistinct("ecebaaax", 2))
    print(Solution().lengthOfLongestSubstringKDistinct("ecebaaax", 1))
