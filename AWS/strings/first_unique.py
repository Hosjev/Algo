class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        
        from collections import Counter
        cache = Counter(s)
        result = None
        
        for k,v in cache.items():
            if v == 1:
                result = k
                break

        return s.index(result) if result else -1


if __name__ == "__main__":
    s = 'leetcode'
    obj = Solution()
    print(obj.firstUniqChar(s))
