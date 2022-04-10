from typing import List



class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def _get_key(item):
            # "a2 act car"
            # (0, "act car", "a2"), (1, )
            _id, remaining = item.split(maxsplit=1)
            return (0, remaining, _id) if remaining[0].isalpha() else (1, )
        # sorted uses merge/insertion
        return sorted(logs, key=_get_key)


if __name__ == "__main__":
    l = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    l = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    l = ["a1 9 2 3 1", "g1 act car", "c1 act car", "a1 act car", "zo4 4 7","ab1 off key dog","a8 act zoo"]
    l = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
    obj = Solution()
    print(obj.reorderLogFiles(l))
