from typing import List
from collections import defaultdict, Counter, deque


class Solution:

    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
            
        for first_word, second_word in zip(words, words[1:]):
            for char, follow in zip(first_word, second_word):
                if char != follow:
                    if follow not in adj_list[char]:
                        adj_list[char].add(follow)
                        in_degree[follow] += 1
                    break
                else: # Check that second word isn't a prefix of first word.
                    if len(second_word) < len(first_word): return ""
    
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        print(adj_list, in_degree, queue)
        while queue:
            char = queue.popleft() # Fifo treatment
            output.append(char)
            for adj in adj_list[char]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
                
        if len(output) < len(in_degree):
            return ""
        return "".join(output)

if __name__ == "__main__":
    words = ["wrt","wrf","er","ett","rftt"]
    print(Solution().alienOrder(words))

