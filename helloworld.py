import sys
import random

print('Hello World');
print('Python Version ' + sys.version);

# Variables
x = 5

# Short comment
"""Large comment"""

# Casting
x = str(3) #String
y = int(3) #Number
z = float(3) #Decimal

# Type function
print(type(x))

# Many values to multiple variables
x, y, z = "Playstation", "XBOX", "Nintendo 64"
print(x, y, z)

# One value to multiple variables
x = y = z = "Same value"

# Unpack a collection
fruits = ["Hello","awesome","!"]
x,y,z = fruits
print(y)

# Functions
def myFunc():
    global x_global 
    x_global = "Amazing"
    print("Python is " + x_global)

myFunc()

print(x_global)

# Data types (str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType)

#Random number
print(random.randrange(1,10))

# Multiline string
multiline_string = """ Helloooo, this is
a multiple line string.
Awesome!"""

print(multiline_string[11])

# For
for x in x_global:
    print(x)
    print(len(multiline_string))
    print("Awesome" in multiline_string)

if("this" in multiline_string):
    print('YES!')

if("lines" not in multiline_string):
    print("NOT IN")

print(x_global[2:5])
print(x_global[:5])
print(x_global[2:])

# Uppercase, lowercase, strip(trim), replace, split --> Strings
print(x_global.upper())
print(x_global.lower())

# F-Strings (Combine String + number)
age = 30
txt = f"I'm {age} years old"
txt2 = f"I'm {age:.2f} years old"
print(txt)
print(txt2.capitalize())

"""
    **Arithmetic Operators**

    Addition = x+y
    Subtraction = x-y
    Multiplication = x*y
    Division = x/y
    Modulus = x%y
    Exponentiation = x**y
    Floor division = x//y

    **Assignment Operators**

    x = 5
    x += 5
    x -= 5
    x *= 3
    x /= 3
    x %= 3
    x //= 3
    x **= 3
    x &= 3
    x |= 3
    x ^= 3
    x >>= 3
    x <<= 3

    **Comparision Operators**

    Equal ==
    Not Equal !=
    Greater than >
    Less than <
    Greater than or equal to >=
    Less than or equal to <=

    **Logical Operators**
    and -> ex. x<5 and x<10
    or -> ex. x>5 or x<10
    not -> ex. not(x>5 and x<10)

    **Identity Operators** (Compare if the objects are the same object, with the same memory location)
    is -> ex. x is y
    is not -> ex. x is not y

    **Membership operators**
    in -> ex. x in y
    not in -> ex. x not in y
"""