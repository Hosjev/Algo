class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # put/get
        from collections import deque


        # Main logic
        # Priming
        q = deque()
        q.append(-1)
        running_max = 0

        for idx, side in enumerate(s):
            if side == "(":
                q.append(idx)
            else: # a right
                try:
                    left = q.pop()
                    running_max = max(running_max, idx - q[-1])
                except IndexError:
                    # By leaving the unmatched right sides on the stack
                    # we keep track of the last valid starting point
                    q.append(idx)


        return running_max

s = ")()(()())(()(()))"
s = "()(()()))(()(()))"
a = Solution()
print(a.longestValidParentheses(s))
