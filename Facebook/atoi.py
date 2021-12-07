class Solution:

    def myAtoi(self, s):
        # 1. leading whitespace? ignore, move idx
        # 2. look for - or +, neg pos respective answer (move pointer)
        # 3. if idx at digit, process idx until no more .isdigit
        idx = 0
        answer = ""
        bottom = pow(-2, 31)
        top = pow(2, 31) - 1
        while not idx >= len(s):
            # 1
            while s[idx].isspace():
                idx += 1
            # 2
            if s[idx] == "-":
                negative = True
                idx += 1
            if s[idx] == "+":
                negative = False
                idx += 1
            # 3
            if s[idx].isdigit():
                while s[idx].isdigit():
                    answer = answer + s[idx]
                    idx += 1
                break
            else: return 0

        if negative and (int(-answer) < bottom):
            answer = bottom
        elif negative and (int(-answer) > bottom):
            answer = -answer
        if not negative and (answer > top):
            answer = top
        return answer
