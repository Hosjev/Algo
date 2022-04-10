class Solution:

    def nextClosestTime(self, time: str) -> str:
        # EC
        if len(set(time)) == 1: return None

        # Lots of rules
        # start from mins, go to hr, or wrap
        avail = [i for i in time if i != ":"] # strings
        minutes = time[-2:]
        for i in range(int(minutes)+1, 60):
            str_int = str(format(i, '02d'))
            if str_int[0] in avail and str_int[1] in avail:
                return time[:3] + str_int

        # Got here, bummer
        hour = time[:2]
        for i in range(int(hour)+1, 24):
            str_int = str(format(i, '02d'))
            if str_int[0] in avail and str_int[1] in avail:
                t_hr = str_int
                min_1, min_2 = min(avail), min(avail)
                return t_hr + ":" + min_1 + min_2

        # final else
        min_num = min(avail)
        return min_num+min_num + ":" + min_num+min_num


if __name__ == "__main__":
    time = "23:43"
    obj = Solution()
    print(obj.nextClosestTime(time))
    time = "18:42"
    obj = Solution()
    print(obj.nextClosestTime(time))
    time = "13:55"
    obj = Solution()
    print(obj.nextClosestTime(time))
    time = "12:01"
    obj = Solution()
    print(obj.nextClosestTime(time))
    time = "12:59"
    obj = Solution()
    print(obj.nextClosestTime(time))
    time = "00:59"
    obj = Solution()
    print(obj.nextClosestTime(time))
    time = "23:59"
    obj = Solution()
    print(obj.nextClosestTime(time))
