# data types
#Data Types are used to define the type of a variable. It defines what type of data we are going to store in a variable.The data stored in memory can be of many types.
var1 = 1       # int data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type
a= 10
b=20
c= 34.5
d= 5+4j
e= 2+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d+e))
# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string
#list data type
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists
#tuple data type
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

#Arithmetic Operators:Used for basic mathematical operations.
a = 10
b = 5

# Addition
print(a + b)  # Output: 15

# Subtraction
print(a - b)  # Output: 5

# Multiplication
print(a * b)  # Output: 50

# Division
print(a / b)  # Output: 2.0

# Modulus (remainder)
print(a % b)  # Output: 0

# Exponentiation
print(a ** b) # Output: 100000

#Comparison Operators: Used to compare values.
x = 10
y = 5

# Equal to
print(x == y)  # Output: False

# Not equal to
print(x != y)  # Output: True

# Greater than
print(x > y)   # Output: True

# Less than
print(x < y)   # Output: False

# Greater than or equal to
print(x >= y)  # Output: True

# Less than or equal to
print(x <= y)  # Output: False
#Logical Operators: Used to combine conditional statements.
p = True
q = False

# Logical AND
print(p and q)  # Output: False

# Logical OR
print(p or q)   # Output: True

# Logical NOT
print(not p)    # Output: False

#Assignment Operators: Used to assign values to variables.
a = 10

# Add AND
a += 5  # Equivalent to: a = a + 5
print(a)  # Output: 15

# Subtract AND
a -= 3  # Equivalent to: a = a - 3
print(a)  # Output: 12

# Multiply AND
a *= 2  # Equivalent to: a = a * 2
print(a)  # Output: 24

# Divide AND
a /= 4  # Equivalent to: a = a / 4
print(a)  # Output: 6.0
#Bitwise Operators: Used to perform operations on individual bits of integers.
x = 10  # Binary: 1010
y = 4   # Binary: 0100

# Bitwise AND
print(x & y)  # Output: 0 (Binary: 0000)

# Bitwise OR
print(x | y)  # Output: 14 (Binary: 1110)

# Bitwise XOR
print(x ^ y)  # Output: 14 (Binary: 1110)

# Bitwise NOT
print(~x)    # Output: -11 (Binary: 11111111111111111111111111110101)

# Left shift
print(x << 1) # Output: 20 (Binary: 10100)

# Right shift
print(x >> 1) # Output: 5 (Binary: 101)
