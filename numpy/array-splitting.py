import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)
newarr = np.array_split(arr, 4)

print(newarr)

#**2D Arrays**
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

#**2D arrays into three 2D arrays**
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)
# or 
newarr = np.hsplit(arr, 3)

print(newarr)