class Solution:
    def removeInvalidParentheses(self, s):
        # TODO: add memoize table for depth reached
        #       *given we need to eval min every time?

        # Prime
        self.off_by = float("inf") # force an overwrite
        self.result = set() # use outer var
        self.parens = set("()")

        def dive(depth, L, R, off_by, placeholder):
            if depth == len(s): # eval
                if L == R: # only matches
                    if off_by < self.off_by: # our 1st or winning MIN off_by
                        self.off_by = off_by
                        self.result = {placeholder}
                    elif off_by == self.off_by: # a MIN off_by reached
                        self.result.add(placeholder)
            else: # all others
                if s[depth] not in self.parens: # add and dive
                    dive(depth + 1, L, R, off_by + 1, placeholder + s[depth])
                else:
                    dive(depth + 1, L, R, off_by + 1, placeholder) # immediately dive
                    if s[depth] == "(": # Left
                        dive(depth + 1, L + 1, R, off_by, placeholder + "(")
                    elif R < L: # Right and needed
                        dive(depth + 1, L, R + 1, off_by, placeholder + ")")

        dive(0, 0, 0, 0, "")
        return list(self.result)


if __name__ == "__main__":
    obj = Solution()
    print(obj.removeInvalidParentheses("(a)())"))
