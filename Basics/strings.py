
# print string
name="Arun Kumar"
print(name)


# quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# assign to variable 

# 1.single line
a="hello"
print(a)

# 2. multiple line

# double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# single quates
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)


# strings are array 
a = "Hello World"
print(a[0])



# looping ata string
a="kill"
for chunk in a:
   print(chunk)


# string length 
print(len(a))


# check string in paragraph
txt = "The best things in life are free!"
print("free" in txt)

# in cond
if "free"  in txt:
   print("Yes the 'free' word is there")

# out cond 
if "expensive" not in txt:
   print("Yes the 'expensive' word is not there")

# slicing string

#  start to end 
b = "Hello, World!"
print(b[2:5])

#  auto to end
print(b[:5])

# start to auto
print(b[7:])

# negative indexing
print(b[-5:-2])



# modify strings 

# uppercase 
a="Hello World ! "
print(a.upper())

# lowercase 
print(a.lower())

# remove whitespace
print(a.strip())

# replace string
print(a.replace("H","R"))

# split string
print(a.split(" "))


# concatenate strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# format strings 

# error 
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# f strings 
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


# escape characters

# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value


txt = "We are the so-called \nVikings\nfrom the north."
# txt = 'We are the so-called "Vikings" from the north.'
print(txt)


#  string methods

"""
1.capitalize()	Converts the first character to upper case
2.casefold()	Converts string into lower case
3.center()	Returns a centered string
4.count()	Returns the number of times a specified value occurs in a string
5.encode()	Returns an encoded version of the string
6.endswith()	Returns true if the string ends with the specified value
7.expandtabs()	Sets the tab size of the string
8.find()	Searches the string for a specified value and returns the position of where it was found
9.format()	Formats specified values in a string
10.format_map()	Formats specified values in a string
11.index()	Searches the string for a specified value and returns the position of where it was found
12.isalnum()	Returns True if all characters in the string are alphanumeric
13.isalpha()	Returns True if all characters in the string are in the alphabet
14.isascii()	Returns True if all characters in the string are ascii characters
15.isdecimal()	Returns True if all characters in the string are decimals
16.isdigit()	Returns True if all characters in the string are digits
17.isidentifier()	Returns True if the string is an identifier
18.islower()	Returns True if all characters in the string are lower case
19.isnumeric()	Returns True if all characters in the string are numeric
20.isprintable()	Returns True if all characters in the string are printable
21.isspace()	Returns True if all characters in the string are whitespaces
22.istitle()	Returns True if the string follows the rules of a title
23.isupper()	Returns True if all characters in the string are upper case
24.join()	Joins the elements of an iterable to the end of the string
25.ljust()	Returns a left justified version of the string
26.lower()	Converts a string into lower case
27.lstrip()	Returns a left trim version of the string
28.maketrans()	Returns a translation table to be used in translations
29.partition()	Returns a tuple where the string is parted into three parts
30.replace()	Returns a string where a specified value is replaced with a specified value
31.rfind()	Searches the string for a specified value and returns the last position of where it was found
32.rindex()	Searches the string for a specified value and returns the last position of where it was found
33.rjust()	Returns a right justified version of the string
34.rpartition()	Returns a tuple where the string is parted into three parts
35.rsplit()	Splits the string at the specified separator, and returns a list
36.rstrip()	Returns a right trim version of the string
37.split()	Splits the string at the specified separator, and returns a list
38.splitlines()	Splits the string at line breaks and returns a list
39.startswith()	Returns true if the string starts with the specified value
40.strip()	Returns a trimmed version of the string
41.swapcase()	Swaps cases, lower case becomes upper case and vice versa
42.title()	Converts the first character of each word to upper case
43.translate()	Returns a translated string
44.upper()	Converts a string into upper case
45.zfill()	Fills the string with a specified number of 0 values at the beginning
"""