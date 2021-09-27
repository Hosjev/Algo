class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        answer_hash = {}
        for item in strs:
            # Our sorted string is the hash key
            key = "".join(sorted(item))
            try:
                answer_hash[key].append(item)
            except KeyError:
                answer_hash[key] = [item]

        return list(answer_hash.values())

a = ["eat", "tea", "tan", "ate", "nat", "bat"]

s = Solution()
print(s.groupAnagrams(a))
