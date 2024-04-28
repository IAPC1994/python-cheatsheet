import numpy as np

arr = np.array([1,2,3,4])
print(arr[0])

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st row: ', arr2[0, 1])
print('5th element on 2nd row: ', arr2[1, 4])

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr3[0, 1, 2])