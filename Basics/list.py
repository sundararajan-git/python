
# pyhon Arrays
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# LIST
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

#  print list 
mylist = ["apple", "banana", "cherry"]

print(mylist)


# allow duplicates 
mylist = ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist)


# list length
print(len(mylist))


# data types in list 
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1 , list2 , list3)


# diffent data types in single list
list1 = ["abc", 34, True, 40, "male"]
print(list1)


# type
print(type(list1))


# to make list using constructor
theList = list(("apple","orange","banana"))
print(theList)


# access list items 

thislist = ["apple", "banana", "cherry"]

# using index
print(thislist[0])

# using negative index
print(thislist[-1])

# using range of index
print(thislist[0:2])

# check if item exists
if "apple" in thislist:
    print("Yes Apple is present")

# chnage the list itmes

# using index
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# using range
thislist[0:2] = ["mango"]
print(thislist)


# insert items
thislist.insert(3,"mango")
print(thislist)

# add items in list

# append items
thislist.append("graps")
print(thislist)

# extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# remove items in list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# using index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# using del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# delete the list 
thislist = ["apple", "banana", "cherry"]
# del thislist
print(thislist)


# clear the list 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# loop the list 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# using  index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# using while loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#  or other way 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# sort list

# string
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# numeric
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sort decenting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# custom sort function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# case sentive sort 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# reverse order 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy list

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# using list method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# using slice operator 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# join list 

# two list join
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# using append method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# using extend method 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# list methods 
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
