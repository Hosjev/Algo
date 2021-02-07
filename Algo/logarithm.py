"""
Logarithm time complexity LOG(N) *log of N
The reason this TC is better than linear is its ability to increase N by double
but only increase the TC by 1 so:
2 exp 1 = 2
2 exp 2 = 4
2 exp 3 = 8
2 exp 4 = 16
2 exp 5 = 32
2 exp 6 = 64
2 exp 7 = 128

*As the input increases (by half) the operations only grow by one.
*Are my graph operations on binary trees falling into log of N?
*Am I eliminating half the input on any given operation in a func/method?
"""

def log_sum_func(n):
    return n * n


for x in range(5):
    print(log_sum_func(x))
