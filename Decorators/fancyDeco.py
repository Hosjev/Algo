"""Examples of the fancier/more complex decorators"""
import sys
sys.path.append("/home/wendiw/Xenial/PythonPlay")
from Utilities.decorators import *
from functools import lru_cache



class WasteTime:
    """if num_times == 5:
    do below 5 times with no output
    from number 0 to 10k, do an exponent of 2 (number times itself)
    then add each number"""
    @debug
    def __init__(self, max_t):
        self.max_t = max_t

    @timer
    def exp_waster(self):
        for _ in range(self.max_t):
             sum([i**2 for i in range(10000)])

@debug
@slow_down(rate=1)
def countdown(from_number):
    """Note that to make use of the slow down decorator
    the function or method needs to call itself."""
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

@singleton
class ClPass:
    pass

#@CountCalls
# This wrapper caches results on calls below it,
# tracking the function and arguments, which must be hashable.
# Here we have 1 arg, which is fine. The maxsize determines
# the number of cached calls. (this replaces your dict/tabling/memoization)
@lru_cache(maxsize=20)
@cache
def fibonacci(num):
    print(f"...calling fibon... {num}")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

#@debug
#@repeat(num_times=2)
def say_some():
    print("I'm saying something.")


###
print(f"\nNEW tests... countdown")
countdown(1)


###
print("\nNEW tests... WasteTime")
wt = WasteTime(1)
wt.exp_waster()


###
print("\nNEW tests... ClassInst")
one = ClPass()
two = ClPass()
print(id(one))
print(id(two))

###
print("\nNEW tests... fibonacci")
f = fibonacci(13)
# Notice how "f" is a natural sum of all Fib returns
print(f)
print(fibonacci.cache_info())
