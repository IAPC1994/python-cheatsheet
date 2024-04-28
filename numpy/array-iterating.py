import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
    
# **Using nditer()
      
for x in np.nditer(arr):
  print(f'Using nditer: {x}')

# ** Different data types**
  
arr0 = np.array([1,2,3])
for x in np.nditer(arr0, flags=["buffered"], op_dtypes=['S']):
 print(x)

#** Iterating with diffeent step size**
 
 for x in np.nditer(arr[:, ::2]):
   print(x)

#**Enumerated**

for idx, x in np.ndenumerate(arr0):
  print(idx, x)

for idx, x in np.ndenumerate(arr):
  print(idx, x)