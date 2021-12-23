import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Edge Case(s)
        # TODO: handle MIN MAX ints

        # Prime
        # Negative == 1*(n as fraction)
        negative_power = n < 0
        if negative_power:
            x = 1 / x
        iterations = math.floor(abs(n)/2)
        summed = 1
        count = 0

        # Double our answer until power of 2/half
        while not count == iterations:
            summed *= x
            count += 1

        summed *= summed
        if abs(n) % 2 != 0: # Odd
            summed *= x
        return summed.__round__(5)


if __name__ == "__main__":
    print(Solution().myPow(2.0, 10))
    print(Solution().myPow(2.1, 3))
    print(Solution().myPow(-2, 3))
    print(Solution().myPow(2, -2))
    print(Solution().myPow(-2, -3))
