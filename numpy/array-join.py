import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# **Join two 2D arrays**

arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])

arr0 = np.concatenate((arr3, arr4), axis=1)

print(arr0)

#**Stacking arrays**

arr5 = np.array([1,2,3])
arr6 = np.array([4,5,6])
# arr7 = np.stack((arr5, arr6), axis=1)
arr7 = np.hstack((arr5, arr6))
print(f'HSTACK: {arr7}')

arr8 = np.vstack((arr5, arr6))
print(f'VSTACK: {arr8}')

arr9 = np.dstack((arr5,arr6))
print(f'DSTACK: { arr9 }')