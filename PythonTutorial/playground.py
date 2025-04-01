import sys
import random

print(sys.version)

#Indentation example
if 5 > 2:
    print("Five is greater than two")

#Python variable example
x = 5
y = "Hello, World!" #This is a comment
print(x)
print(y)

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#variable and type can be changed
x = 4
x = "Sally"
print(x)

#Casting
x = str(3)
y = int(3)
z = float(3)
print(x, y, z)

print(type(x))
print(type(y))
print(type(z))

#double quotes are the same as single quotes
x = 'John'
y = "John"
print(x)
print(y)

#Variable names are case-sensitive
a = 4
A = "Sally"
print(a, A)

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

#One Value to Multiole Variables
x = y = z = "Orange"
print(x, y, z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x + y + z)

#Global Variables
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

#Local Variables
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

#global keyword
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = 1   # int
y = 2.8 # float
z = 1j  # complex with a "j" as the imaginary part

#scientific numbers with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#int(), float(), complex()
x = float(1)
y = int(2.8)
z = complex(1)
print(x, y, z)
print(type(x))
print(type(y))
print(type(z))

#random number from 1 to 9
print(random.randrange(1,10))

x = int(2.8)
y = int("3")
print(x, y)
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x, y, z, w)
x = str("s1")
y = str(2)
z = str(3.0)
print(x, y, z)

#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print(bool(""))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x, int))

#Python Arithmetic Operations
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 % 3)
print(5 ** 3)
print(5 // 3)

#Python Assignment Operators
x = 5
x += 3
print(x)
x -= 4
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
print(x := 7)
print(x)
x //= 3
print(x)
x **= 3
print(x)

#Python Logical Operators
x = 5
print (x > 3 and x < 10)
print (x < 6 or x < 4)
print (not(x < 5 and x < 10))

#Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print (x is z) # z is the same object as x
print (x is y) # not the same object, even if they have the same content
print (x == y)

#Python Bitwise Operators
print(6 & 3) # AND
"""
6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
"""
print(6 | 3) # OR
"""
6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
"""
print(6 ^ 3) # XOR
"""
6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
"""
print(~3) # NOT
"""
 3 = 0000000000000011
-4 = 1111111111111100
"""
print(3 << 2) # 2 Shift left
"""
 3 = 0000000000000011
12 = 0000000000001100
"""
print(3 >> 1) # 1 Shift right
"""
3 = 0000000000000011
1 = 0000000000000001
"""
