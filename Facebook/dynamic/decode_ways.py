class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge Case(s)
        if s[0] == str(0): return 0

        # Prime
        # Build table with primed singletons
        #   and eval pairs in arrears
        table = [0] * (len(s) + 1)
        table[0], table[1] = 1, 1

        # Logic
        # Iterate straight through eval'ing single/pair
        for idx in range(2, len(table)):
            right = int(s[idx - 1])
            left = int(s[idx - 2])
            if right > 0:
                table[idx] = table[idx - 1]
            # Up to 19 or 26
            if (left == 1) or (left == 2 and right < 7):
                table[idx] += table[idx - 2]

        return table[-1]


if __name__ == "__main__":
    s = "217405"
    obj = Solution()
    print(obj.numDecodings(s))
    s = "21626"
    obj = Solution()
    print(obj.numDecodings(s))
