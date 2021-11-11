class Solution:
    def strStr(self, A, B) -> int:
        # Edge Case(s)
        if len(A) == 0 or len(B) == 0:
            return -1

        # Prime
        string = A
        pattern = B
        iterations = (len(string) - len(pattern)) + 1

        for idx in range(iterations):
            if string[idx:idx+len(pattern)] == pattern:
                return idx
        return -1


A = "hellloooo"
B = "lll"
print(Solution().strStr(A, B))
