class Solution:
    def _upper(self, s):
        temp = "".join(s.split("-"))
        temp = list(temp)
        for i, char in enumerate(temp):
            if char.islower():
                temp[i] = char.upper()
        return temp

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Step 1 - sanitize string (rem dashes)
        # Step 2 - group from the rear
        sanitize = "".join(self._upper(s))
        idx = len(sanitize)-1
        result = str()
        while idx >= 0:
            # (7-4) : 7 => 4:8
            start = (idx-k+1)
            if start < 0: start = 0
            grouping = sanitize[start:idx+1]
            result = grouping + "-" + result
            idx = idx - k
        return result.rstrip("-")


if __name__ == "__main__":
    l = "5F3Z-2e-9-w"
    k = 4
    obj = Solution()
    print(obj.licenseKeyFormatting(l, k))

