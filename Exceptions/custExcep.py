""" Game guess number """

import sys

sys.path.append("/home/wendiw/Documents/PythonPlay")

from Exceptions.GuessGameErrs import *

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
    try:
        u_num = input("Enter a number: ")
        u_num = int(u_num)
        if (u_num==number+1) or (u_num==number-1):
            raise ValueSoClose
        elif u_num < number:
            raise ValueTooLow
        elif u_num > number:
            raise ValueTooHigh
        break
    except ValueError:
        print("Gimme a number, and only!")
        print()
    except ValueTooLow:
        print("This value is too small, try again!")
        print()
    except ValueTooHigh:
        print("This value is too large, try again!")
        print()
    except ValueSoClose:
        print("Oooh! You are SO close! Try again.")
        print()

print("Congratulations! You guessed it correctly.")
