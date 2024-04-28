import numpy as np  

arr = np.array([[1,2,3,4],[5,6,7,8]])

print(arr.shape)

arr1 = np.array([1,2,3,4], ndmin=5)

print(arr1)
print(f'shape of array {arr.shape}')

# **Reshaping 1D to 2D**

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# 1st parameter: number of dimensions
# 2nd parameter: number of elements in the dimension
newarr = arr2.reshape(4, 3)

print(newarr)

# **Reshaping 1D to 3D**
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# 1st parameter: number of arrays
# 2nd parameter: number of arrays contained
# 3rd parameter: number of lements in the dimension
newarr1 = arr3.reshape(2, 3, 2)

print(f'3D: {newarr1}')
print(f'Copy or view?: {newarr1.base}') # View

# Unknown dimension
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr2 = arr3.reshape(2, 2, -1)

print(newarr2)

# **Flattening the array: Back from Multidimensional to 1D**
arr4= np.array([[1,2,3],[4,5,6]])
newarr = arr.reshape(-1)
print(newarr)