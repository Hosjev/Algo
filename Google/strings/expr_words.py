from typing import List


class Solution:
    def _eval_string(self, s):
        key = 0
        source = [[s[0], 1]]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                source[key][1] += 1
            else:
                source.append([s[i], 1])
                key += 1
        return source

    def expressiveWords(self, s: str, words: List[str]) -> int:
        # EC

        # Prime
        results = 0
        pattern = self._eval_string(s)

        # Logic
        for word in words:
            good = True
            try:
                compare = self._eval_string(word)
                if len(pattern) != len(compare): raise StopIteration
                for i, e in enumerate(compare):
                    if e[0] != pattern[i][0]: raise StopIteration
                    else:
                        count, compare_count = pattern[i][1], e[1]
                        if count < 3:
                            if count != compare_count: raise StopIteration
                        else:
                            if compare_count > count: raise StopIteration
            except StopIteration:
                good = False
            if good: results += 1


        return results


if __name__ == "__main__":
    s = "heeellooo"
    w = ["hello", "hi", "helo"]
    obj = Solution()
    print(obj.expressiveWords(s, w))
    s = 'abcd'
    w = ['abc']
    obj = Solution()
    print(obj.expressiveWords(s, w))
