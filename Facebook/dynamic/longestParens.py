class Solution:

    def longestValidParentheses(self, s: str) -> int:
        # Edge Case(s)
        if len(s) <= 1: return 0

        # Prime
        stack = [-1]
        current = 0
        max_len = 0

        # Logic
        while stack:
            paren = s[current]
            if paren == '(':
                stack.append(current)
            else: # right
                index = stack.pop()
                if index == -1 or s[index] == ')': # mismatch
                    stack.append(current)
                else:
                    max_len = max(max_len, (current - stack[-1]))
            current += 1
            if current == len(s): break
        return max_len
            


if __name__ == "__main__":
    p = "())((()))"
    #p = ")))((())"
    p = "()()(())"
    obj = Solution()
    print(obj.longestValidParentheses(p))
