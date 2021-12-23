class CompressString:
    def compress(self, s):
        # Edge Case(s)
        if (len(s) / 2) <= len(set(s)):
            return s

        # Prime
        counter = 0
        prev = sorted(s)[0]
        result = str()
        for i in sorted(s):
            if i == prev:
                counter += 1
            else:
                result += self._eval_char(prev, counter)
                prev = i
                counter = 1

        result += self._eval_char(prev, counter)
        return result

    def _eval_char(self, c, n):
        return f"{c}{n}" if n > 1 else f"{c}1"


s = "aabb"
s = "aaabbcddd"
print(CompressString().compress(s))
