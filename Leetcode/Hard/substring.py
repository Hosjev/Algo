class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        def substring_helper(match, subarray, i_chunk):
            if not match and not subarray:
                return True

            local_match = match[0:i_chunk]
            if local_match in subarray:
                instance = subarray.index(local_match)
                local_subarray = subarray[:instance] + subarray[instance+1:]
                return substring_helper(match[i_chunk:], local_subarray, i_chunk)
            else:
                return False


        # Priming
        results = list()
        starters = [x[0] for x in words]
        i_chunk = len(words[0])
        t_chunk = i_chunk * len(words)

        for idx, character in enumerate(s):
            if len(s) - idx < t_chunk:
                break
            if character in starters:
                if substring_helper(s[idx:idx+t_chunk], words, i_chunk):
                    results.append(idx)
                

        return results

# Write recursive/backtrack solution
# -if in starters still relevant
# -but aa aa breaks so idx+1
# -and with aa aa, we know that last 3 of s is OUT
w = ["foo", "bar"]
s = "foofoobarmandoofoobarfoo" # -3
a = Solution()
print(a.findSubstring(s, w))

w = ["word", "best", "good", "word"]
s = "wordgoodgoodgoodbestwordbestgoodbestgood"

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
w = ["fooo","barr","wing","ding","wing"] # 13
a = Solution()
print(a.findSubstring(s, w))

s = "aaaaaaaaaaaaaa"
w = ["aa","aa"] # 0-10
a = Solution()
print(a.findSubstring(s, w))

s = "abababab"
w = ["ab", "ba"]
a = Solution()
print(a.findSubstring(s, w))
