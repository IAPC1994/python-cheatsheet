from numpy import random
import numpy as np

# Numbers
x = random.randint(100)
print(x)

# Floats
y = random.rand()
print(y)

# Integers
# 1D
i = random.randint(100, size=(5))
print(i)
#2D
ii = random.randint(100, size=(3, 5))
print(ii)


# **Choice**

# c = random.choice([3,5,7,9])
c = random.choice([3,5,7,9], size=(3,5))
print(c)

# **Probabilities**

p = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3,5))

print(f'Random: {p}')


# **Shuffling arrays** method makes changes to the original array.
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

# **Permution** method returns a re-arranged array (and leaves the original array un-changed).
arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))