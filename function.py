
def myFirstFunction(name="John"):
    print("Hello " + name)

myFirstFunction("Ivan")
myFirstFunction(name="Melisa")
myFirstFunction()

# More arguments that a function accept

def moreArgument(*arg):
    print("Hello " + arg[1])

moreArgument("Ivan", "Meli", "Camilo")

# Arbitrary Keyword Arguments **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")


# Return values
def number_sum(number):
    return number + 1

print(number_sum(4))

# Positional-Only argument
def my_function_2(x, /):
    print(x)
my_function_2(3)
# my_function_2(x = 3) Raise an error


# Keyword-Only arguemnts
def my_function_3(*, x):
    print(x)
my_function_3(x = 3)
# my_function_3(3) Raise an error


# Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion( k - 1 )
        print("Recursion: ", result)
    else:
        result = 0
    return result

tri_recursion(6)