def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"by",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b


a = divide(10,5)
print(a)
print(type(a))
b = divide(5,0)
print(type(b))
