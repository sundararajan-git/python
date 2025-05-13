
# class and objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# create a class
class MyClass:
    x = 5

# create an object
p1 = MyClass()
print(p1.x)  # 5


# The __init__() function is called automatically every time the class is being used to create a new object.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
p2 = Person("Mary", 28)

print(p1.name)  # John
print(p1.age)  # 36
print(p2.age)  # 28
print(p2.name)  # Mary


# The __str__() function controls what should be returned when the class object is represented as a string.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    

p1 = Person("John", 36)

print(p1)  # John is 36 years old

# object methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()  # Hello my name is John


# Self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class: 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()  # Hello my name is John


# modify object properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old")

p1 = Person("John", 36)
p1.myfunc()
p1.age = 40
print(p1.age)  # 40


# delete object properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old")            

p1 = Person("John", 36)
p1.myfunc()
del p1.age
# print(p1.age)  # AttributeError: 'Person' object has no attribute 'age'

# delete the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old")            

p1 = Person("John", 36)
del p1
# p1.myfunc()  # NameError: name 'p1' is not defined


# pass statement
class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement
