'''This is a test of class/super/sub/etc'''


class SuperFuck:
    '''Returns super class of FUCK'''
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def area(self):
        return self.arg1 * self.arg2

    def perimeter(self):
        return 2 * self.arg1 + 2 * self.arg2


class LowFuck(SuperFuck):
    def __init__(self, arg1):
        super().__init__(arg1, arg1)


class RealLowFuck(SuperFuck):
    def __init__(self, arg1):
        super().__init__(arg1, arg1)


#CALL
aSFobj = SuperFuck(4,5)

print(aSFobj.__doc__)
print(aSFobj.area())

aLFobj = LowFuck(5)

print(aLFobj.area())
