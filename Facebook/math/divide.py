class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if not divisor: return
        MIN_INT = pow(-2, 31)
        MAX_INT = pow(2, 31) - 1
        HALF_MIN = MIN_INT // 2
        if dividend == MIN_INT and divisor == -1: # some overflow case
            return MAX_INT

        # Roundabout way of evaling neg, but saves code
        negs = 2
        if divisor > 0:
            negs -= 1
            divisor = -divisor
        if dividend > 0:
            negs -= 1
            dividend = -dividend

        quotient = 0
        while divisor >= dividend:
            powerOfTwo = 1
            value = divisor
            # Until we can't double or reach edge
            while (value >= HALF_MIN) and \
                ((value + value) > dividend):
                value += value
                powerOfTwo += powerOfTwo
            quotient += powerOfTwo
            dividend -= value

        return -quotient if negs == 1 else quotient


if __name__ == "__main__":
    print(Solution().divide(10, 2))
    print(Solution().divide(10, -2))
    print(Solution().divide(-10, -2))
