class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def sayHello(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("Ivan", 29)
p1.sayHello()

#Inheritance

class Student(Person):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    # Super will make the child class inherit all the methods and properties from its parent
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year

e1 = Student("Melisa", 26, 2024)
print(e1)
e1.sayHello()