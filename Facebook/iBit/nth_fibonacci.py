class Solution:
    def solve(self, A):
        # TODO: decorate tail recursion (as cPy doesn't respect it)
        def _get_modulo(last, cur):
            max_prime = pow(10, 9) + 7
            return (last + cur) % max_prime

        def fibonacci(nth, count, last_sum, c_sum):
            if nth == count:
                return c_sum

            f_sum = _get_modulo(last_sum, c_sum)
            return fibonacci(nth, count + 1, c_sum, f_sum)

        def xOR_fibonacci(nth, a, b):
            # Early edge cases, except for 2
            if nth == 0:
                return a
            if nth == 1:
                return b
            if nth == 2:
                return a ^ b

            return xOR_fibonacci(nth % 3, a, b)

        #return fibonacci(A, 1, 0, 1)
        return xOR_fibonacci(A, 1, 2)



print(Solution().solve(8))
