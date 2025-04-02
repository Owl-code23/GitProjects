fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

#break
for x in fruits:
    print(x)
    if x == "banana":
        break
for x in fruits:
    if x == "banana":
        break
    print(x)

#continue
for x in fruits:
    if x == "banana":
        continue
    print(x)

#range()
for x in range(6): # 0 - 5
    print(x)
for x in range(2, 6): # 2 - 5
    print(x)
for x in range(2, 30, 3): # 2 - 30 increment of 3
    print(x)

#else
for x in range(6):
    print(x)
else:
    print("finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("finished!")

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#pass
for x in [0, 1, 2]:
    pass