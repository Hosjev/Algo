class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # EC if either 0
        if (len(s) * k) == 0:
            return 0

        left, right = 0, 0
        cache = dict()
        max_length = 1

        while right < len(s):
            cache[s[right]] = right
            right += 1

            if len(cache) == k + 1:
                del_idx = min(cache.values())
                del cache[s[del_idx]]
                left = del_idx + 1

            max_length = max(max_length, right - left)

        return max_length


if __name__ == "__main__":
    # Using a cache as type of set(), 80% faster
    print(Solution().lengthOfLongestSubstringKDistinct("ecebax", 2))
