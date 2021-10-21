class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def cns(string):
            res = ''
            string += '#'
            c = 1
            for i in range(len(string) - 1):
                if string[i] == string[i+1]:
                    c += 1
                    continue
                else:
                    res += str(c) + string[i]
                    c = 1
            return res

        # Start of logic
        start = '1'
        for i in range(n-1):
            start = cns(start)
        return start


print(Solution().countAndSay(5)) #111221
