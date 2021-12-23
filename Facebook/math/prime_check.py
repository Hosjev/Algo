import math


class PrimeNumber:
    """ O(sqrt Num) O(N)  """
    def evaluate(self, num):
        if num == 2 or num == 3: return True
        for n in range(2, num):
            zero = (num % n) == 0
            if zero: return False
        return True

    def evaluate_notSuck(self, num):
        for n in range(2, int(math.sqrt(num)+1)):
            # If my num at any time is wholly divided
            #   (w/no remainder) by anything
            #   then it is NOT a prime
            zero = (num % n) == 0
            if zero: return False
        return True


print(PrimeNumber().evaluate_notSuck(89))
