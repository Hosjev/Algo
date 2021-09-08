import time
import sys
sys.path.append("/home/wendiw/Xenial/PythonPlay/IO")
from Utilities import custlogging



#logging.write_to_log("/home/wendiw/Documents/PythonPlay/errLog.log", "First test of log function")

def greet(*names):
    print(type(names))
    for i in names:
        print("Sup", i)


greet("Boo", "Hey", "Fuck")

[print(i) for i in (2, 3, 4)]

# RECURSION
def calcF(argInt):
    if argInt == 1:
        print("    we reached 1")
        return 1;
    else:
        print("Inside else", argInt)
        return (argInt * calcF(argInt-1))


print("Result", calcF(4))


'''Print into file'''

with open("./openFileTest.txt", 'a', encoding="utf-8") as f:
    f.write("\n" + time.asctime() + "\n")
    f.write("First line of text\n")
    f.write("Second line of text\n")
    f.write("Third line of text\n")
