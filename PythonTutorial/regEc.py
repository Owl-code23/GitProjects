import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! We have a match!")
else:
    print("No match")

#findall()
x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)

#search()
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

x = re.search("Portugal", txt)
print(x)

#split()
x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

#sub()
x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)

#Match Object
#span()
x = re.search(r"\bS\w+", txt)
print(x.span())

#string
print(x.string)

#group()
print(x.group())