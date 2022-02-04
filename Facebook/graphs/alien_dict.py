from collections import defaultdict, Counter
from queue import Queue


class Solution:
    def alienOrder(self, words) -> str:
        # Edge Case(s)
        if not bool(words): return ""

        # Prime
        dependents = defaultdict(set)
        degrees = Counter( {char: 0 for word in words for char in word} )
        result = list()

        # Logic
        for i in range(len(words) - 1):
            # Prefix check
            len_1, len_2 = len(words[i]), len(words[i + 1])
            if len_1 > len_2 and words[i][:len_2] == words[i + 1]:
                return ""
            for char, follow in zip(words[i], words[i + 1]):
                if char != follow:
                    if follow not in dependents[char]:
                        dependents[char].add(follow)
                        degrees[follow] += 1
                        print(char, follow)
                    break

        print(dependents)
        # Iterate backward through dependents and degrees
        q = Queue() # FIFO
        [q.put(char) for char in degrees if degrees[char] == 0]
        while not q.empty():
            char = q.get()
            result.append(char)
            for adjacent in dependents[char]:
                degrees[adjacent] -= 1
                # Whittle down the degrees of dependence
                if degrees[adjacent] == 0:
                    q.put(adjacent)

        # Check for loops
        print(result)
        if len(result) < len(degrees): return ""
        
        # Finally, return string
        return "".join(result)


if __name__ == "__main__":
    words = ["wrt","wrf","er","ett","rftt"]
    words = ["fool","foo","er","ett","rftt"]
    #words = ["z","x","a","zb","zx"]
    words = ["wrt","wrf","er","ett","rftt","te"]
    print(Solution().alienOrder(words))

