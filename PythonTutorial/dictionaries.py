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