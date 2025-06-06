import json

#Parse JSON
# JSON:
x = '{"name":"John", "age":30, "city":"New York"}'
# parse x with loads():
y = json.loads(x)
print(y["age"])

#Convert from Python to JSON
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5},
             {"model": "Ford Edge", "mpg": 24.1}]
}

print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(".",  " = ")))
print(json.dumps(x, indent=4, sort_keys=True))
