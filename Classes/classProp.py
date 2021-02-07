class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature
    def in_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    def get_temperature(self):
        print(f"({__class__!r}) returning getting temp value")
        return self._temperature
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print(f"({__class__!r}) setting value")
        self._temperature = value
    temperature = property(get_temperature,set_temperature)


class Age:
    def __init__(self):
        self._age = 0

    def get_age(self):
        return self._age

    def set_age(self, a):
        self._age = a

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


class AgeProp:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a < 0:
            raise ValueError("You are an embryo at age (" + str(a) + "). Try again.")
        self._age = a


print("Building age object...")
w = AgeProp()
w.age = 52
print(w.age, "\n")


print("Building age object...")
a = Age()
print("...setting age")
a.age = 55
print("...retrieving age")
print(a.age)
print("\n")

print("Building object...")
t = Celsius()
print("...getting temp by property...")
print(t.temperature)
print("...getting temp by method...")
print(t.get_temperature())
t.set_temperature(25)
print(t.in_fahrenheit())
print(t.temperature)


