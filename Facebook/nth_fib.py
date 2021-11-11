class Fibonacci:

    def nth_recur(self, last, current, count, nth):
        if nth == count:
            return current
        return self.nth_recur(current, (last + current), count + 1, nth)

    def nth_iter(self, nth):
        last, current = 0, 1
        count = nth - 1
        while count:
            last, current = current, last + current
            count -= 1
        return current
 
    def nth_dyn(self, n):
        # Make hash of positions and return last one
        cache = {}
        return self._dyn(n, cache)

    def _dyn(self, n, cache):
        if n == 0 or n == 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self._dyn((n-1), cache) + self._dyn((n-2), cache)
        return cache[n]

    def evaluate(self, n):
        return self.nth_dyn(n)
        #return self.nth_iter(n)
        #return self.nth_recur(0, 1, 1, n)


def main():
    print(Fibonacci().evaluate(8))


main()
