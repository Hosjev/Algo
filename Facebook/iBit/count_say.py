class Solution:
    """
    Input: int
    Output: str
    """
    def countAndSay(self, num: int) -> str:
        def accumulator(base):
            temp = base + "*"
            count = 1
            result = ""
            for i in range(len(temp) - 1):
                if temp[i] == temp[i+1]:
                    count += 1 # accumulator
                else: # resolution
                    result += str(count) + temp[i]
                    count = 1 # reset count of accu things
            return result

        # Main
        # Edge Case(s)
        if num <= 0: return 0

        base = "1"
        # generator
        for i in range(num-1):
            base = accumulator(base)

        return base

print(Solution().countAndSay(5))
