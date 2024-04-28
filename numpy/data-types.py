import numpy as np
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

arr = np.array([1, 2, 3, 4])
arr0 = np.array(['apple', 'banana', 'cherry'])
arr1 = np.array([1, 2, 3, 4], dtype='S')
arr2 = np.array([1, 2, 3, 4], dtype='i4')



print(arr.dtype)
print(arr0.dtype)

print(arr1)
print(arr1.dtype)

print(arr2)
print(arr2.dtype)

# **Converting data type on existing array**

arr3 = np.array([1.1, 2.1, 3.1])

# newarr = arr3.astype('i')
newarr = arr3.astype(int)

print(newarr)
print(newarr.dtype)