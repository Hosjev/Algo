class Solution:

    def _ways(self, N, cache):
        if N < 0:
            return 0
        if N == 0:
            return 1
        if N in cache:
            return cache[N]
        cache[N] = (
                    self._ways(N - 1, cache) + \
                    self._ways(N - 2, cache)
                    )
        return cache[N]


    def solve(self, N):
        if not N: return 0
        return self._ways(N, {})


if __name__ == "__main__":
    print(Solution().solve(3))
    print(Solution().solve(4))
    print(Solution().solve(5))
