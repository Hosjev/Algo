class RobotMatrix:

    def _forward(self, pos, grid, ans):
        if pos == (len(grid), len(grid[0]) - 1):
            return True
        if pos[0] > len(grid) - 1 or \
           pos[1] > len(grid[0]) - 1 or \
           grid[pos[0]][pos[1]] == "x":
            return False
        ans.append(pos)
        R = self._forward((pos[0], pos[1]+1), grid, ans)
        if not R:
            D = self._forward((pos[0]+1, pos[1]), grid, ans)
            if not D:
                ans.pop()
                return False
        return ans

    def _reverse(self, grid, row, col, memo, ans):
        if row < 0 or col < 0 or grid[row][col] == "x":
            return False
        pos = (row, col)
        if pos in memo:
            return memo[pos]
        memo[pos] = (row == 0 and col == 0 or \
                     self._reverse(grid, row, col - 1, memo, ans) or \
                     self._reverse(grid, row - 1, col, memo, ans)
                    )
        if memo[pos]: ans.append(pos)
        return memo[pos]

    def move(self, grid):
        #return self._forward((0, 0), grid, [])
        ans = []
        self._reverse(grid, len(grid)-1, len(grid[0])-1, {}, ans)
        return ans


def main():
    m = [
      ["o", "o", "o", "o"],
      ["o", "o", "x", "x"],
      ["o", "o", "o", "o"],
      ["o", "x", "o", "o"],
    ]
    print(RobotMatrix().move(m))

main()
