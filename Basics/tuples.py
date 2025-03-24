
# tuples

# Ordered
# Unchangeable
# Allow Duplicates
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)


# tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# create tuple with one item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# data types 
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# diffrent data types in single tuples
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)


# type
print(type(tuple1))


# create tuple using tuple constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# access tuples

# using index
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# using negative index
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# using range 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# check if item exits
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# add itmes

# in list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# in tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# remove item
# in list 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# using del key word
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


# unpack tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# using  asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# tropic variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# loop tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# using index number

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# tuple mehtods 
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


