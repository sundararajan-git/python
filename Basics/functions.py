
# function decclaration
def my_function():
  print("Hello from a function")

# function call
my_function()


# function with parameters
def my_function_with_args(first_name, last_name):
  print("Hello " + first_name + " " + last_name)

# function call with arguments
my_function_with_args("John", "Doe")

# arguments vs parameters

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# arbitrary arguments
def my_function_with_arbitrary_args(*args):
  print("The first argument is: " + args[0])
  print("The second argument is: " + args[1])
  print("The third argument is: " + args[2])

my_function_with_arbitrary_args("John", "Doe", "Smith")


# keword arguments
def my_function_with_keyword_args(first_name, last_name):
  print("Hello " + first_name + " " + last_name)

my_function_with_keyword_args(last_name="Doe", first_name="John")


# arbitrary keyword arguments
def my_function_with_arbitrary_keyword_args(**kwargs):
  print("The first keyword argument is: " + kwargs["first_name"])
  print("The second keyword argument is: " + kwargs["last_name"])

my_function_with_arbitrary_keyword_args(first_name="John", last_name="Doe")


# default parameters values
def my_function_with_default_args(first_name, last_name="Doe"):
  print("Hello " + first_name + " " + last_name)

my_function_with_default_args("John")


# passing a list as an argument
def my_function_with_list_args(fruits):
  for fruit in fruits:
    print("I like " + fruit)

my_function_with_list_args(["apple", "banana", "cherry"])

# return values

def my_function_with_return_value():
  return "Hello from a function with a return value"

my_function_return_value = my_function_with_return_value()
print(my_function_return_value)


# the pass statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def my_function_with_pass():
  pass

my_function_with_pass()

# keyword only arguments
def my_function_with_keyword_only_args(*, first_name, last_name):
  print("Hello " + first_name + " " + last_name)

my_function_with_keyword_only_args(first_name="John", last_name="Doe")


# positional only arguments
def my_function_with_positional_only_args(first_name, last_name, /):
  print("Hello " + first_name + " " + last_name)

my_function_with_positional_only_args("John", "Doe")

# combining positional, keyword, arbitrary, and default arguments
def my_function_with_all_args(first_name, last_name, /, *args, **kwargs):
  print("Hello " + first_name + " " + last_name)
  print("The arbitrary arguments are: " + str(args))
  print("The keyword arguments are: " + str(kwargs))

my_function_with_all_args("John", "Doe", "apple", "banana", first_name="Jane", last_name="Smith")


# recursion
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  
print(factorial(5))  # Output: 120



# lambda functions
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# It is often used for short, throwaway functions that are not going to be reused elsewhere in the code.

# syntax: 
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# why use lambda functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.