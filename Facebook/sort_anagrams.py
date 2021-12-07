from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0: return [[""]]
        cache = {}
        for i in strs:
            key = str(sorted(i))
            try:
                cache[key].append(i)
            except KeyError:
                cache[key] = [i]
        
        if len(cache) == 0:
            return [[""]]
        return list(cache.values())


if __name__ == "__main__":
    a = ["", "", "eat", "ate", "tan", "nat", "boo", "tea"]
    print(Solution().groupAnagrams(a))
