import time

fibSequence = dict()

def getNthFib(n):
    # Write your code here.
    fibIndex = 2
    fibSum = int()
	
    def	fibCalc(fibIndex, lastInt, lastRes):
        # result greater than 2
        fibSum = lastInt + lastRes
        while n != fibIndex:
            fibIndex += 1
            return fibCalc(fibIndex, lastRes, fibSum)
        else:
            return lastRes

    # If n is zero, return, else iterate
    if n == 0 or n == 1:
        fibSum = 0
    else:
        fibSum = fibCalc(fibIndex,0,1)

    return fibSum

# To iterate thru Fib numbers, try dict first

#for i in (12,8,2,3,6,1,0,4):
for i in range(20):
    try:
        if i == 0:
            fibSequence[0] = (0,0)
        elif i == 1:
            fibSequence[1] = (0,1)
        print("From Fibonacci position {}: {}".format(i,fibSequence[i]))
    except KeyError as e:
        getNthFib(int(str(e)))
        print("Added Fibonacci position {}: {}".format(i,fibSequence[i]))

