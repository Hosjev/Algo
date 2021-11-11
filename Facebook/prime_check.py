import math


class PrimeNumber:

    def evaluate(self, num):
        if num == 2 or num == 3: return True
        for n in range(2, num):
            zero = (num % n) == 0
            if zero: return False
        return True

    def evaluate_notSuck(self, num):
        for n in range(2, int(math.sqrt(num)+1)):
            zero = (num % n) == 0
            if zero: return False
        return True


print(PrimeNumber().evaluate_notSuck(89))
