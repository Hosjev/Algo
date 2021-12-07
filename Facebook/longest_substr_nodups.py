class Solution:

    def longest_nodups(self, string):
        if len(string) == 1:
            return 1
        inds = [1] * len(string)
        for i in range(1, len(string)):
            # Start at inds[] i - 1 stored length say 1 need start of 2index i - num
            start = i - inds[i - 1]
            local_slice = string[start:i]
            while string[i] in local_slice:
                start += 1
                local_slice = string[start:i]
            if len(local_slice) > 0:
                inds[i] = (i - start) + 1
            print(i, start, local_slice, inds)

        return max(inds)


if __name__ == "__main__":
    print(Solution().longest_nodups("bbbb"))
    print(Solution().longest_nodups("abcabcbb"))
    #rint(Solution().longest_nodups("01234567"))
    print(Solution().longest_nodups("abcdefge"))
    print(Solution().longest_nodups("pwwkew"))
