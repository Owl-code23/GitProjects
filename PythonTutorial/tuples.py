#Tuple is ordered, unchangeable and allows duplicates
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))

#One item Tuple
thistuple = ("apple",)
print(type(thistuple))
#Not a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Access Tuple Items
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:2])

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

#Change Tuple Values workaround
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange")
y.remove("apple")
x = tuple(y)
print(x)

#Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#unpacking
(red, yellow, darkred, orange) = thistuple
print(red)
print(yellow, darkred, orange)

#unpacking with asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#Loop Tuples
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

i = 0

while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

#Join two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)