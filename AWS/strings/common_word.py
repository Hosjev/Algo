from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Regex 
        import re
        pattern = re.compile(r'([\S]+)\s+')
        word_pattern = re.compile(r'[\w\']+')
        # Scrub / concatenate
        string = paragraph.lstrip()
        string += " "
        from collections import defaultdict
        cache = defaultdict(int)

        for word in pattern.findall(string):
            # Scrub word
            s_word = word_pattern.match(word).group()
            if s_word.lower() not in banned:
                cache[s_word.lower()] += 1
        
        max_word = max(cache.values())
        return [x for x in cache if cache[x] == max_word][0]



if __name__ == "__main__":
    p = "Bob hit a ball, the hit BALL flew far after it was hit."
    obj = Solution()
    print(obj.mostCommonWord(p, ["hit"]))
    p = 'a.'
    obj = Solution()
    print(obj.mostCommonWord(p, [""]))
    
