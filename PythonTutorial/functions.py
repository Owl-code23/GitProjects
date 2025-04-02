#def
def my_function():
    print("Hello from a function")

my_function()

#Arguments or args
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")

#Arbitrary Arguments *args
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus", "Test")

#Keyword Arguments or kwargs
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitray Keyword Arguments, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function()

#Passing a List
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return values
def my_function(x):
    return 5 * x

print(my_function(3))

#Pass
def myfunction():
    pass

#Positional-Only Arguments
def my_function(x, /):
    print(x)

my_function(3)

#Keyword-Only Arguments
def my_function(*, x):
    print(x)

my_function(x = 3)

#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("Recursion example results:")
tri_recursion(6)