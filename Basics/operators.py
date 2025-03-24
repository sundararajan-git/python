
# operatores

"""
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""


# arithmetic operators 

#  +	Addition
#  -	Subtraction	
#  *	Multiplication		
#  /	Division	
#  %	Modulus		
#  **	Exponentiation	
#  // Floor division


# addition
print(5+5)

# subtraction
print(5-3)

# multiplication
print(3*3)

# division
print(10/2)

# modulus
print(3%2) 

# exponentiation
print(3**2)

# floor division
print(5//3)



# assignment operators

#  =	x = 5		
#  +=	x += 3	         x = x + 3	
#  -=	x -= 3	         x = x - 3	
#  *=	x *= 3	         x = x * 3	
#  /=	x /= 3	         x = x / 3	
#  %=	x %= 3	         x = x % 3	
#  //=	x //= 3	         x = x // 3	
#  **=	x **= 3	         x = x ** 3	
#  &=	x &= 3	         x = x & 3	
#  |=	x |= 3	         x = x | 3	
#  ^=	x ^= 3	         x = x ^ 3	
#  >>=	x >>= 3	         x = x >> 3	
#  <<=	x <<= 3	         x = x << 3	
#  :=	print(x := 3)	 x = 3


# assingment operator
x=5
print(x)

# increment operators
x +=3
print(x)

#  decrement operator
x -=3
print(x)

# multiplication operators
x *=3
print(x) 

# division operators
x /=3
print(x)

# modules operators
x %=3
print(x) 

# exponentiation operators
x **=3
print(x)

# floor division operators
x //=3
print(x)

# & operators 
x=34
x &=3
print(x)

# | operators
x=5
x |=5
print(x)

#  ^ operators
x =3
x ^=3
print(x)

# >>= operators
x=3
x >>=3
print(x)

#  <<= operators
x=3
x <<=3
print(x)

# := operators
print(x := 3)




# comparison operators 

# ==	Equal	x == y	
""" !=	Not equal	x != y """	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y



#  equal operators 
x=5
y=5
print(x==y)

# not equal operators 
print( x!= y) 

# greater than operators 
print( x > y)

# less than operators
print(x < y)

# greater than or equal to operators 
print( x >= y) 

# less than or equal to operators
print( x <= y )


# logical operators 

"""
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""

x=5

# and operators
print(x>6 and x<10)

#  or operators 
print(x>4 or x<10)

#  not operators
print(not(x>10))


# identity operators

"""
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
"""


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# memebership operatores


x = ["apple", "banana"]

print("banana" in x)
print("banana" not  in x)

# returns True because a sequence with the value "banana" is in the list​


# bitwise operators

"""
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""

x=4
y=2

# AND operartors
print(x & y)

# OR operators
print(x | y)

# XOR operators
print(x ^ y)

# NOT operators
print(~ x)

# left shift operators
print(x << 2)

# right shift operators
print(x >> 2)


# operator precedence

print((6 + 3) - (4 + 2))


# precedence operatores order 

"""
1. ()	Parentheses	
2. **	Exponentiation	
3. +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
4. *  /  //  %	Multiplication, division, floor division, and modulus	
5. +  -	Addition and subtraction	
6. <<  >>	Bitwise left and right shifts	
7. &	Bitwise AND	
8. ^	Bitwise XOR	
9. |	Bitwise OR	
10. ( == , != , >  , >=  , < , <= , is , is not , in , not in ) Comparisons, identity, and membership operators	
11. not	Logical NOT	
12. and	AND	
13. or	OR
"""