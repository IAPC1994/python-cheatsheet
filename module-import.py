# import module
import platform
import module as greetingModule
from module import person1

greetingModule.greeting("Ivan")

a = greetingModule.person1["age"]
print(a)
print(person1["name"])

x = platform.system()
y = dir(platform)
print(x)
print(y)