from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Edge Cases
        if len(p) > len(s): return []
        if s == p: return [i for i in range(len(s))] # free return

        # Use sliding window sized at length of pattern
        idx, window = int(), len(p)
        pattern = Counter(p)
        result = []

        while idx <= (len(s) - window):
            match = s[idx:idx+window]
            print(idx, match)
            if pattern == Counter(match):
                result.append(idx)
            idx += 1

        return result


if __name__ == "__main__":
    s = "cabedacbafg"
    p = "abc"
    print(Solution().findAnagrams(s, p))
