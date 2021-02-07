"""Example generator. The most imp thing to recall: Gens are memory efficient as when you build them they don't store all values in memory but return them when called."""
import cProfile

def my_gen():
    # the YIELDS below TURN this function into a generator.
    # YIELD itself returns a function
    # the numbers are unnecessary as yield returns nothing but the next iteration
    # for loops are generators that yield and handle "StopIteration" errs
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    # but here we can return by appending to yield a result and then storing it in a variable
    #n = "foo"
    # it should be noted here that yield executes all the code in between
    print('This is printed at last')
    yield n


# Really good use of a generator. Providing example of note above: memory efficient. If you have an object that needs to read in a ton of data, use a generator and iterate through the items one at a time. Thereby only loading one item into memory at a time. Files/database objects, images?
def file_gen(file_name):
    for line in open(file_name, "r"):
        yield line

f_gen_res = file_gen("/tmp/Xorg.crouton.1.log")
row_count = 0
print(next(f_gen_res))
print(next(f_gen_res))
print(next(f_gen_res))
print(next(f_gen_res))
for item in f_gen_res:
    row_count += 1
print(row_count)

# infinite gen
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def is_palindrome(num):
    # Skip single-digit inputs. %modulus--divides left by right and returns remainder before decimal division: possible values 1-9
    """Floor division to root out single digits (10 not incl)
    -modulus equals remainder after division
    >set the 'temp' value based on num provide
    >set a var to zero
    >the MEAT: while your num provided doesn't equal zero
        :reset rev num: 0*10 plus 12%10 -- 0+2 = 2
        :reset temp to 12//10 = 1
        :go again
        :reset rev num: 2*10 plus 1%10 -- 20+1 = 21
        :reset temp to 1//10 = 0
        break
    >return results"""
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
        print("interation")

    if num == reversed_num:
        return True
    else:
        return False

#the smallest possible integer palindrome
is_palindrome(11)

#infinite generator calls the above math mess
#eternally increment "num" for possible palindromes
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            print(f"inside IF IS: {num}")
            if i is not None:
                num = i
        print(f"outside IF IS: {num}")
        num += 1

#palgen = infinite_palindromes()

#for i in palgen:
    #digits = len(str(i))
    #palgen.send(10 ** (digits))

#for i in infinite_sequence():
    #pal = is_palindrome(i)
    #if pal:
        #print(pal)


# HOWEVER this example demostrates that list executes faster AT ONCE if the dataset is small or the execution is CPU bound
cProfile.run('sum([i*2 for i in range(10000)])')
cProfile.run('sum((i*2 for i in range(10000)))')

"""When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller. (In contrast, return stops function execution completely.) When a function is suspended, the state of that function is saved. This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling."""

# this does nothing but call the function b/c nothing is returned
#my_gen()

# this assigns a to a generator object
#a = my_gen()
#print(a) 

# this iterates thru the generator
#next(a)

# this iterates thru the generator
#next(a)

# this both iterates thru the generator and stores the yield return
#b = next(a)
#print(b)

c = my_gen()
for item in c:
    print(item)
