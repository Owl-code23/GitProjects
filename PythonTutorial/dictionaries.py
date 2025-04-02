#Dictionaries is ordered, changeable and no duplicate

#Create
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])

#No duplicates
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print(len(thisdict))

#Any data type
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

#dict()
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing items
x = thisdict["age"]
print(x)

#get()
x = thisdict.get("age")
print(x)

#keys()
x = thisdict.keys()
print(x)
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) # before change
car["color"] = "white"
print(x) # after change

#values()
x = thisdict.values()
print(x)
thisdict["test1"] = "test1"
print(x)

#items()
x = thisdict.items()
print(x)
thisdict["test2"] = "test2"
print(x)

#Check if key exists
if "name" in thisdict:
    print("Yes, 'name' is one of the keys in the thisdict dictionary")

#Change Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#update()
thisdict.update({"year": 2020})
print(thisdict)

#Add items
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"doorcolor": "red"})
print(thisdict)

#Remove items pop()
thisdict.pop("doorcolor")
print(thisdict)

#Remove last item popitem()
thisdict.popitem()
print(thisdict)

#del
del thisdict["model"]
print(thisdict)

#clear()
thisdict.clear()
print(thisdict)

del thisdict

#Loop
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
#Key names
for x in thisdict:
    print(x)
for x in thisdict.keys():
    print(x)
#Values
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)

#Copy a Dictionary copy() or dict()
mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])