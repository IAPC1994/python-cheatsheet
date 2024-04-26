
try:
    print(x)
except:
    print("An exception occurred")

try:
    print(x)
except NameError:
    print("Variable x is not defined!")
except:
    print("Something else went wrong")

try:
    print("Hello World")
except NameError:
    print("Variable x is not defined!")
else:
    print("Nothing went wrong")

try:
    print(y)
except:
    print("Variable x is not defined!")
finally:
    print("The 'try except' is finished")

# Raise an exception  
    if 1<0:
        raise Exception("Sorry, no numbers below zero")
    
    if not type("str") is int:
        raise TypeError("Only integers are allowed")