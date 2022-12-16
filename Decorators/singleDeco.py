import sys
sys.path.append("/home/wendiw/Xenial_Backup/PythonPlay")
from Utilities.decorators import *


@debug
def waste_some_time(num_times):
    """if num_times == 5:
    do below 5 times with no output
    from number 0 to 10k, do an exponent of 2 (number times itself)
    then add each number"""
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
    return "I finished"

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

@repeat(num_times=3)
@CountCalls
def say_greet(person):
    #print(f"Greeting this person {person}")
    return f"Greeting this person {person}"
