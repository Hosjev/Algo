"""
A positive integer is considered uniform if all of its digits are equal. For example, 222222 is uniform, while 223223 is not.
Given two positive integers AA and BB, determine the number of uniform integers between AA and BB, inclusive.
"""

class Uniform:
    def getUniformIntegerCountInInterval(self, A: int, B: int) -> int:
        # A => starting num
        # B => ending num (both incl)
        # Prime section
        num = A
        decimal = len(str(num))
        result = int()

        while not num >= B+1:
            if set(str(num)[0]) == set(str(num)):
                result += 1
                num += int(decimal * "1")
            else:
                if len(str(num)) > decimal: # Update
                    decimal = len(str(num))
                    num = int(decimal * "1")
                else:
                    num += 1

        return result


if __name__ == "__main__":
    print(Uniform().getUniformIntegerCountInInterval(75,3333333))
    print(Uniform().getUniformIntegerCountInInterval(1,9))
    print(Uniform().getUniformIntegerCountInInterval(9,9))
