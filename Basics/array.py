
# Python does not have built-in support for Arrays, but Python Lists can be used instead.

# An array is a special variable, which can hold more than one value at a time.

# create array
cars = ["Ford", "Volvo", "BMW"]

# access the array
print(cars[0])  # Ford
print(cars[1])  # Volvo     


# length of the array 
x = len(cars)

print(x)  # 3

# looping the array
for x in cars:
    print(x)


# adding the array
cars.append("Honda")
print(cars)  # ['Ford', 'Volvo', 'BMW', 'Honda']

# removing the array
cars.pop(1)
print(cars)  # ['Ford', 'BMW', 'Honda']

# ---- or ---
# cars.remove("Volvo")


# methods of array

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# copy the array
cars2 = cars.copy() 
print(cars2)  # ['Ford', 'BMW', 'Honda']

# count the number of elements in the array
x = cars.count("Ford")  
print(x)  # 1


# extend the array
cars.extend(["Toyota", "Nissan"])
print(cars)  # ['Ford', 'BMW', 'Honda', 'Toyota', 'Nissan']

# get index of the element
x = cars.index("Honda")
print(x)  # 2

# insert the element at the specified position
cars.insert(1, "Chevrolet")
print(cars)  # ['Ford', 'Chevrolet', 'BMW', 'Honda', 'Toyota', 'Nissan']

# reverse the array
cars.reverse()
print(cars)  # ['Nissan', 'Toyota', 'Honda', 'BMW', 'Chevrolet', 'Ford']


# sort the array
cars.sort()
print(cars)  # ['BMW', 'Chevrolet', 'Ford', 'Honda', 'Nissan', 'Toyota']

# delete the all elements of the array
cars.clear()
print(cars)  # []