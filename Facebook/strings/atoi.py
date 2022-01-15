class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. scrub whitespace
        # 2. check "-" or "+"
        # 3. read non-digit/if before, False
        # 4. convert leading zeros
        # 5. convert 
        # 6. return int

        # Prime
        MAX, MIN = pow(2, 31) - 1, pow(-2, 31)
        negative = False # assume
        positive_exp = False
        pointer = 0
        result = str()

        while pointer != len(s):
            if s[pointer].isspace():
                pass
            elif s[pointer] == "-":
                negative = True
            elif s[pointer] == "0" and not result:
                pass
            elif s[pointer].isalpha() and not result:
                return 0
            elif s[pointer].isdigit() or s[pointer] == ".":
                result += s[pointer]
            elif s[pointer] == "+": positive_exp = True
            pointer += 1

        
        if positive_exp and negative or \
            not result:
                return 0
        result = -int(float(result)) if negative else int(float(result))
        if result < MIN:
            return MIN
        if result > MAX:
            return MAX
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.myAtoi('42'))
    print(obj.myAtoi('  -42'))
    print(obj.myAtoi(' 42 foo bar'))
    print(obj.myAtoi('2147483648'))
    print(obj.myAtoi('3.45211'))
    print(obj.myAtoi('.1'))
    print(obj.myAtoi('+-12'))
    print(obj.myAtoi('+'))
