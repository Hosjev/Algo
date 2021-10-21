class Solution(object):
    def largestRectangleArea(self, height):
        # Artifically enhance building list
        #   with absolute zero size
        # Because we're evaling shortest in arrears
        height.append(0)
        stack = [-1]
        area = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area, h * w)
            stack.append(i)
        height.pop()
        return area


A = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(A))
