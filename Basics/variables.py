

# creating variable

name = "Arun K"
age = 25

print(name)
print(age)


# variable casting ( convertsion one type to another type )

x = str(4)
y = int("4")
z = float(4)

print(x)
print(type(x))
print(type(y))
print(type(z))


# single or double quotes

friend1 = "John"
# is the same as
friend2 = 'Ben'

print(friend1)
print(friend2)

# case sensitive

a = 4
A = "Sally"
#A will not overwrite a

print(a)
print(A)

# variable names 

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""


# allowed 
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# not allowed 
# 2myvar = "John"
# my-var = "John"
# my var = "John"


# name cases 

# 1.camel case
myVariableName = "John"

# 2.pascal case
MyVariableName = "John"

# 3.snake case
my_variable_name = "John"

#  assigning mutltiple varaibles

x,y,z = "Orange" , "Banana" , "Apple"

print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
furits = ["apple","orange","cherry"]
x,y,z = furits

print(x)
print(y)
print(z)


# output variables

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = 5
y = 10
print(x + y)

# not allowed 
# x = 5
# y = "John"
# print(x + y)


# global varaibles

x = "awesome"

def myfunc():
  x = "fantastic"
#   local varaibles
  print("Local - Python is " + x)

myfunc()

# global varaible
print("Global - Python is " + x)



# global keyword 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Gloabl KeyWord - Python is " + x)