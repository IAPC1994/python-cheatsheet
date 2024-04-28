import numpy as np
from math import log

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

# print(z)

# Create a ufunc (frompyfunc)
# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.

def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)
# print(myadd([1,2,3,4],[5,6,7,8]))
# print(type(np.add))

# Subtraction
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
# print(newarr)

# Multiply
newarr0 = np.multiply(arr1, arr2)
# print(newarr0)

# Division
newarr1 = np.divide(arr1, arr2)
# print(newarr1)

# Power
newarr2 = np.power(arr1, arr2)
# print(newarr2)

# Remainder
# newarr3 = np.mod(arr1,arr2)
newarr3 = np.remainder(arr1,arr2)
# print(newarr3)

# Quotient and Mod
newarr4 = np.divmod(arr1,arr2)
# print(newarr4)

# Absolute
arr3 = np.array([-1, -2, 1, 2, 3, -4])
newarr5 = np.abs(arr3)
# print(newarr5)


# Truncation & Fix
arr = np.trunc([-3.1666, 3.6667])
# print(arr)

arr0 = np.fix([-3.1666, 3.6667])
# print(arr0)

# Rounding
arr3 = np.around(3.1666, 2)
# print(arr3)

# Floor
arr4 = np.floor([-3.1666, 3.6667])
# print(arr4)

# Ceil
arr5 = np.ceil([-3.1666, 3.6667])
# print(arr5)

# Log at base 2
arr6 = np.arange(1, 10)
# print(np.log2(arr6))

# Log at base 2
arr7 = np.arange(1, 10)
# print(np.log10(arr7))

# Natural Log, or log at base e
arr8 = np.arange(1, 10)
# print(np.log(arr8))

# Log at any base
nplog = np.frompyfunc(log, 2, 1)
# print(nplog(100, 15))

# Summations
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
# print(newarr)

# Summation over an axis
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
# print(newarr)

# Cummulative sum
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
# print(newarr)

# Products
arr = np.array([1, 2, 3, 4]) # 1*2*3*4
x = np.prod(arr)
# print(x)

# Product over an axis
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
# print(newarr)

# Cummulative product
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)