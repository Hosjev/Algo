class StairsPuzzle:
    """ O(S * 3) """
    def _ways(self, steps, cache, count):
        count[0] += 1
        if steps < 0:
            return 0
        if steps == 0:
            return 1
        if steps in cache:
            return cache[steps]
        cache[steps] = (self._ways(steps - 1, cache, count) + \
                        self._ways(steps - 2, cache, count) + \
                        self._ways(steps - 3, cache, count))
        return cache[steps]

    def solve(self, steps):
        count = [0]
        result = self._ways(steps, {}, count)
        print(count)
        return result


if __name__ == "__main__":
    # This is: the number of ways to reach s(1)
    #                                      s(2)
    #                                      s(3)
    #                                      s(4)
    #                                      s(5)
    #   etc... and accumulating
    #   The cache or memo-izing table merely
    #   improves performance/speed as you climb
    #   back up the stack.
    print(StairsPuzzle().solve(10))
