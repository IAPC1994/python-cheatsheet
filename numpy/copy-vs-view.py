import numpy as np

# **Copy**
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# **View**

arr1 = np.array([1, 2, 3, 4, 5])
y = arr1.view()
arr1[0] = 42

print(arr1)
print(y)


## **Check if array owns its data**

x = arr.copy()
y = arr.view()

print(x.base) # None because it's doesnt owns the data
print(y.base)