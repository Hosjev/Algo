class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        1. Lots of O(N) but equalizing heights
        2. Calc max to left and right
        3. Eval difference at every index
        """
        # Priming
        LR_hash = {}
        for x in range(len(height)):
            LR_hash[x] = {"l": 0, "r": 0}
        water = int()

        # Determine max height to my left
        lMax = 0
        for idx in range(1, len(height)):
            lMax = max(lMax, height[idx-1])
            LR_hash[idx]["l"] = lMax

        # Determine max height to my right
        rMax = 0
        for idx in reversed(range(len(height)-1)):
            rMax = max(rMax, height[idx+1])
            LR_hash[idx]["r"] = rMax

        # Take the difference (me) from smallest wall
        for i, h in enumerate(height):
            # Mini containers
            minContain = min(LR_hash[i]["l"], LR_hash[i]["r"])
            if h < minContain:
                water += (minContain - h)

        return water


h = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
a = Solution()
print(a.trap(h))
