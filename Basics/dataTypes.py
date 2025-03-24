
#  Built in Data Types 

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


# get data types
x=5
print(x,type(x))


# string type
x = "Hello World"
print(x,type(x))

# inteager type
x=20
print(x,type(x))


# flaot type
x=20.5
print(x,type(x))

# complex type
x=1j
print(x,type(x))


# list type 
x = ["apple", "banana", "cherry"]
print(x,type(x))

# tuple type
x = ("apple", "banana", "cherry")
print(x,type(x))

# range type
x = range(6)
print(x,type(x))

# dict type
x = {"name" : "John", "age" : 36}
print(x,type(x))

# set type
x = {"apple", "banana", "cherry"}
print(x,type(x))

# frozenset type
x = frozenset({"apple", "banana", "cherry"})
print(x,type(x))

# bool type
x = True
print(x,type(x))

# bytes type
x = b"Hello"
print(x, type(x))

# bytearray type
x = bytearray(5)
print(x,type(x))

# memorycview type 
x = memoryview(bytes(5))
print(x,type(x))

# none type
x=None
print(x,type(x))