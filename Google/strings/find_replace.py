from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # EC
        if not s: return s

        # Prime
        new_string = s
        offset = 0
        cache = {}
        for i,e in enumerate(indices):
            cache[e] = {"source": sources[i], "target": targets[i]}

        # Logic
        for key in sorted(cache.keys()):
            start_idx = key + offset
            length = len(cache[key]["source"])
            if cache[key]["source"] == new_string[start_idx:start_idx+length]:
                new_string = new_string[:start_idx] + cache[key]["target"] + new_string[start_idx+length:]
                offset += len(cache[key]["target"])-len(cache[key]["source"])

        return new_string


if __name__ == "__main__":
    s = "abcd"
    s = "abcd"
    i = [0, 2]
    so = ["ab", "cd"]
    t = ["foo", "bar"]
    obj = Solution()
    print(obj.findReplaceString(s,i,so,t))

    s = "vmokgggqzp"
    i = [3,5,1]
    so = ["kg","ggq","mo"]
    t = ["s","so","bfr"]
    obj = Solution()
    print(obj.findReplaceString(s,i,so,t))
    # i = [1,3,5]
    # "vbfrssozp"
