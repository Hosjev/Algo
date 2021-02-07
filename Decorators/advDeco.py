import sys
sys.path.append("/home/wendiw/Xenial_Backup/PythonPlay")
from Utilities.decorators import *



@simp_deco
def say_hello(name):
    return f"Hello {name}"

#@greet_bob
def be_awesome(name):
    return f"Yo {name} together we are the awesomest!"

#Self/locally decorated
def parent(num):
    def one_child():
        return "I am first child"
    def two_child():
        return "I am 2nd child"
    if num == 1:
        return one_child
    else:
        return two_child

@my_decorator
def say_whee():
    print("Whee!")

@debug
def waste_some_time(num_times):
    """if num_times == 5:
    do below 5 times with no output
    from number 0 to 10k, do an exponent of 2 (number times itself)
    then add each number"""
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

@slow_down
def countdown(from_number):
    """Note that to make use of the slow down decorator
    the function or method needs to call itself."""
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

@register
def hello_per(name):
    return f"Hello {name}"

@register
def awesome_per(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


###
print("Tests...")
#h = say_hello
#print(h)
h = say_hello("Mel")
print(h)


###
print("\nNEW tests...")
say_whee()


###
print("\nNEW tests...")
waste_some_time(15)


###
print("\nNEW tests...")
mg = make_greeting("Bill", 66)
print(mg)


###
print("\nNEW tests...")
countdown(9)
