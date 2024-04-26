# Lambda (Anonymous function)
x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(7,8))

# Utility
def myfunc(n):
    return lambda a : a * n

myDuplicator = myfunc(2)
myTriplicator = myfunc(3)

print(myDuplicator(10))
print(myTriplicator(25))