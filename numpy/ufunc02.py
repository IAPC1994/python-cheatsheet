import numpy as np

# Differences

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
# print(newarr)

# n = repetitions
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
# print(newarr)

# Finding LCM (lowest common multiple)
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
# print(x)

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
# print(x)

# Finding GCD (Greatest Common Denominator)
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
# print(x)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
# print(x)

# **Trigonometric functions
x = np.sin(np.pi/2)
# print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
# print(x)

# Degrees into radians
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
# print(x)

# Radians to degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
# print(x)

# Finding Angles
x = np.arcsin(1.0)
# print(x)

# Angles of each value in arrays
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
# print(x)

# Hypotenues
base = 3
perp = 4
x = np.hypot(base, perp)
# print(x)

# **Hyperbolic functions

x = np.sinh(np.pi/2)
# print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
# print(x)

# Finding Angles
x = np.arcsinh(1.0)
# print(x)

# Angles of each value in arrays
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
# print(x)

#**Set Operations
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
# print(x)

# Finding Union
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
# print(newarr)

# Finding intersection
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
# print(newarr)

# Finding difference
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
# print(newarr)

# Symmetric difference
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)