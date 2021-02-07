import sys
import time

randoList = [1, 4, "fuss", "boo"]
errLog = open("./errLog.log", 'a', encoding="utf-8")


for item in randoList:
    try:
        print("Item:", item)
        r = 1/int(item)
        print("Reciprical:", r, "\n")
        #break
    except:
        print("ERROR:", sys.exc_info()[0])
        errLog.write(time.asctime() + "\n")
        errLog.write("Item [" + item + "] in list received: " + str(sys.exc_info()[0]) + "\n")
        print("continue...\n")

