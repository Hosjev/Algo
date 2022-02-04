from typing import List



class Solution:

    def _build_prefix_trie(self, words):
        trie = dict()
        for word in words:
            obj = trie
            for c in word:
                if c not in obj:
                    obj[c] = dict()
                obj = obj[c]
            obj["*"] = {True}
        return trie

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Edge Case(s)
        if not s: return False

        # Prime
        trie = self._build_prefix_trie(wordDict)

        # Logic
        # TODO: due to single char possibilities,
        #       this requires a DFS approach
        #       BUT keep trie
        obj = trie
        for idx, char in enumerate(s):
            if char in obj:
                obj = obj[char]
                if "*" in obj and idx != len(s) - 1:
                    print(idx, obj)
                    obj = trie
            else: return False

        return True if "*" in obj else False


if __name__ == "__main__":
    words = ["cat", "dog", "cot"]
    s = "catsdog"
    s = "catdog"
    obj = Solution()
    #print(obj.wordBreak(s, words))
    s = "aaaaaaa"
    print(len(s))
    words = ["aaaa","aaa"]
    obj = Solution()
    print(obj.wordBreak(s, words))
