class Base1:

    def __init__(self):
        self.attr1 = "base1"

    def method_b1(self):
        return "...from base1"


class Base2(Base1):

    def __init__(self):
        self.attr2 = "base2"
        #super().__init__() # OR
        Base1.__init__(self)

    def method_b2(self):
        return self.attr2


class MultiBase(Base2):

    def __init__(self):
        self.attr = "m_base"
        super().__init__()

    def run_test(self):
        return self.method_b1()


if __name__ == "__main__":
    obj = MultiBase()
    print(obj.run_test())
    print(MultiBase.__mro__)
    print(obj.__class__)
    print(obj.__dict__)
