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