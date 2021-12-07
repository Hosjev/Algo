class MyClass:
    def __init__(self):
        self.attr = "obj class"

    def method(self):
        return f'instance method called {self} and here is proof: {self.attr}'

    @classmethod
    def classmethod(cls):
        try:
            foo = cls.attr
        except AttributeError:
            foo = "ain't no CLS attrs"
        return f'class method called {cls}, results of cls: {foo}'

    @staticmethod
    def staticmethod():
        try:
            foo = self.attr
        except NameError:
            foo = "no SELF"
        return f'static method called, results of self: {foo}'


class Pizza:
    def __init__(self, ingreds):
        self.ingreds = ingreds

    def __repr__(self):
        return f'{self.__class__.__name__}({self.ingreds!r})'

    # Factory function example
    # If class name changes, cls doesn't care
    @classmethod
    def marg(cls):
        return cls(['mozz', 'tomatoes'])


if __name__ == "__main__":
    obj = MyClass()
    print(obj.method())
    print(obj.classmethod())
    print(obj.staticmethod())
    print(Pizza.marg())
