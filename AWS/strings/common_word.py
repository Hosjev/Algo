from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Case Insensitive algorithm
        import string
        sanitized_para = ""
        for i in paragraph:
            if i in punctuation and i not "'":
                sanitized_para += i + " "
            else: sanitized_para += i
        array = [i.strip(string.punctuation).lower() for i in sanitized_para.split()]
        result = []
        for i in set(array):
            if i not in banned:
                result.append([i, array.count(i)])
        return sorted(result, key=lambda x: x[1], reverse=True)[0]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Regex 
        import re
        pattern = re.compile(r'([a-zA-Z0-9\']+)[\s,.!?]+')
        word_pattern = re.compile(r'[\w\']+')

        # Scrub / concatenate
        string = paragraph.lstrip() + " "
        from collections import defaultdict
        cache = defaultdict(int)

        for word in pattern.findall(string):
            s_word = word_pattern.match(word).group()
            if s_word.lower() not in banned:
                cache[s_word.lower()] += 1
        
        return sorted(cache.items(), key=lambda x: x[1], reverse=True)[0]



if __name__ == "__main__":
    p = "Bob hit a ball, the hit BALL flew far after it was hit."
    obj = Solution()
    print(obj.mostCommonWord(p, ["hit"]))
    p = 'a.'
    obj = Solution()
    print(obj.mostCommonWord(p, [""]))
    p = "a, a, a, a, b,b,b.c, c"
    print(Solution().mostCommonWord(p, ["a"]))
