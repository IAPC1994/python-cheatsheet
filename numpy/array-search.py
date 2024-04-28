import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)


# ** Search Sorted**
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
y = np.searchsorted(arr, 7, side='right')

print(x)
print(y)

# **Search multiple values**
arr = np.array([1,3,5,7])
z = np.searchsorted(arr, [2, 4, 6])
print(z)