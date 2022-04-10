from typing import List
from collections import defaultdict
from queue import Queue


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # EC
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)
        cache = defaultdict(list)
        for word in wordList:
            for i in range(L):
                cache[word[:i] + "*" + word[i+1:]].append(word)

        # Queue for BFS
        q = Queue()
        q.put((beginWord, 1))
        visited = {beginWord: True}
        while not q.empty():
            word, level = q.get()
            for i in range(L):
                inter_word = word[:i] + "*" + word[i+1:]
                for match in cache[inter_word]:
                    if match == endWord:
                        return level + 1
                    if match not in visited:
                        visited[match] = True
                        q.put((match, level + 1))
                cache[inter_word] = []
        return 0


if __name__ == "__main__":
    w = ["dot", "dog", "log", "cog"]
    print(Solution().ladderLength("hot", "cog", w))
