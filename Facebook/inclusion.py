from collections import defaultdict



class Solution:
    def checkInclusionHash(self, s1: str, s2: str) -> bool:
        # (timed out)
        # Edge Case(s)
        if len(s1) > len(s2): return False

        # Prime
        pattern = sorted(s1)
        cache = defaultdict(list)
        for i,c in enumerate(s2): cache[c].append(i)

        # Logic
        for char in s1:
            if not char in cache:
                return False
            for idx in cache[char]:
                match = sorted(s2[idx:idx+len(s1)])
                if match == pattern: return True
        return False

    def matches(self, occur_1, occur_2):
        for i in range(26):
            if occur_1[i] != occur_2[i]: return False
        return True # final return

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Passed with still high compute time
        # Edge Case(s)
        if len(s1) > len(s2): return False

        # Prime for approach #4
        #   offset unicode alpha chars w/first letter 'a' 
        s1_occurrence = [0] * 26 # alpha 0-25
        for i in s1: s1_occurrence[ord(i) - ord('a')] += 1
        
        # Logic
        # Iter through difference
        for i in range(len(s2) - len(s1) + 1):
            s2_occurrence = [0] * 26
            for j in range(len(s1)):
                # advance thru s2 s1 number of times
                s2_occurrence[ord(s2[i + j]) - ord('a')] += 1
            if self.matches(s1_occurrence, s2_occurrence): return True
        return False # final return



if __name__ == "__main__":
    s1 = "ab"
    s2 = "eiabvbiaoo"
    obj = Solution()
    print(obj.checkInclusion(s1, s2))
