from typing import List


class Solution:
    def _recurse(self, board, word, w_idx, visited, R, C):
        """Return True if any True or None"""
        if w_idx >= len(word): return True
        # Logic
        up = down = left = right = None
        if R-1 >= 0 and board[R-1][C] == word[w_idx] and (R-1, C) not in visited:
            up = self._recurse(board, word, w_idx+1, visited + [(R-1, C)], R-1, C)
        if R+1 < len(board) and board[R+1][C] == word[w_idx] and (R+1, C) not in visited:
            down = self._recurse(board, word, w_idx+1, visited + [(R+1, C)], R+1, C)
        if C-1 >= 0 and board[R][C-1] == word[w_idx] and (R, C-1) not in visited:
            left = self._recurse(board, word, w_idx+1, visited + [(R, C-1)], R, C-1)
        if C+1 < len(board[R]) and board[R][C+1] == word[w_idx] and (R, C+1) not in visited:
            right = self._recurse(board, word, w_idx+1, visited + [(R, C+1)], R, C+1)
        if up or down or left or right: return True

    def exist(self, board: List[List[str]], word: str) -> bool:
        # EC
        if not bool(board): return False

        # Logic
        for R in range(len(board)):
            for C in range(len(board[R])):
                if board[R][C] == word[0]:
                    ans = self._recurse(board, word, 1, [(R, C)], R, C)
                    if ans: return True
        return False



if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print(Solution().exist(board, word))
    board = [ ["a", "a"] ]
    word = "aaa"
    print(Solution().exist(board, word))
    board = [
            ["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]]
    word = "ABCESEEEFS"
    print(Solution().exist(board, word))
