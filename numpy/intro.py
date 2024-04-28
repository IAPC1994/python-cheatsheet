import numpy as np

arr = np.array([1,2,3,4,5])
tup = np.array((1,2,3,4,5))
print(arr)
print(tup)
print(type(arr))
print(np.__version__)


# **0-D Arrays**
arr0 = np.array(42)

print("NO-dimensional: ",arr)

# **1-D Arrays (UNI-DIMENSIONAL)**
arr1 = np.array([1,2,3,4,5])
print("UNI-dimensional: ",arr)

# **2-D Arrays (BI-DIMENSIONAL)**
arr2 = np.array([[1,2,3], [4,5,6]])
print("BI-dimensional: ",arr)

# **3-D Arrays (TRI-DIMENSIONAL)**
arr3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print("TRI-dimensional: ",arr)

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# **MULTIDIMENSIONAL 4TH is the vector, 3rd is the matrix with the vector, 2nd 3-D Array, 1st 4D array**
arr_multiple = np.array([1,2,3,4,5], ndmin=5)
print(arr_multiple)
print("number of dimensions: ", arr_multiple.ndim)