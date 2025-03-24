# set

# Unordered
# Unchangeable
# Duplicates Not Allowed
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.


# print set
thisset = {"apple", "banana", "cherry"}
print(thisset)


# duplicates ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


# diffrent types
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


# 0 and false are same value consider
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


# access the items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# check is present or not 
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)


# add items in set

# using add method 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# add one set to another set for ietms tasrasnfer
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)


# add any itreateable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset)


# remove items in sets

# using remove method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


# using discard method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


# using the pop mehtod random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# delete the set permanently
thisset = {"apple", "banana", "cherry"}
# del thisset
print(thisset)


# loop sets 
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#  join sets

# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# union method 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# join set and tuple

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)


# update method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
# set3 = set1 & set2
print(set3)


# diffrence
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
# set3 = set1 - set2
print(set3)

# set methods

# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
# <	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
# >	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others




