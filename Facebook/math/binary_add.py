class Solution:
    def _bin_to_dec(self, binary):
        # We whittle away at binary by way of base 10
        #   -count the levels
        #   -refactor binary level with pow
        decimal, level, binary = int(), int(), int(binary)
        while binary:
            remaining = binary % 10
            decimal = decimal + (remaining * pow(2, level))
            level += 1
            binary = binary // 10
        return decimal

    def _dec_to_bin(self, decimal):
        return bin(decimal).lstrip('0b')

    def addBinary(self, a: str, b: str) -> str:
        # Edge Case(s)
        if int(a) == 0: return b
        if int(b) == 0: return a

        # Logic
        a_dec, b_dec = self._bin_to_dec(a), self._bin_to_dec(b)
        return self._dec_to_bin(a_dec + b_dec)


if __name__ == "__main__":
    obj = Solution()
    print(obj.addBinary("1000", "1010"))
    print(obj.addBinary("0", "0"))
