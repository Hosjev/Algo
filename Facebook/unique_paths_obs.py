class Solution:

    def traverse(self, grid, square, ans):
        # Bottom right of grid => end
        if square == [len(grid)-1, len(grid[0])-1]:
            ans[0] += 1
            return ans[0]
        # Out-of-bounds
        elif square[0] > len(grid)-1 or square[1] > len(grid[0])-1:
            return
        # Obstacle
        elif grid[square[0]][square[1]] == 1:
            return

        self.traverse(grid, [square[0], square[1]+1], ans)
        self.traverse(grid, [square[0]+1, square[1]], ans)

        return ans[0]

    def unique_shit(self, g):
        # Edge Case(s)
        # => 1st square obstacle
        if g[0][0] == 1: return 0
        # => last square obstacle
        if g[-1][-1] == 1: return 0

        # TC O(n*m) SC O(SQ+1)
        return self.traverse(g, [0,0], [0])


[0, 0] # HrWc
g = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]
g = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]
#g = [[1]] # 0
#g = [[0]] # 1
#g = [[0, 1]] # 0
#g = [[0]] # 1
#g = [[0, 0]]
a = Solution()
print(a.unique_shit(g))
# O(m*n)
