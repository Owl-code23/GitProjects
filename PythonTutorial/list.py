#List is ordered, changeable and allows duplicate
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
list1 = [1, 5, 7, 9, 3]
list2 = [True, False, False]
list3 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(type(list3))

#list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print(list1[-1])
print(list1[-2])
print(list1[2:5])
print(list1[:4])
print(list1[2:])

#Check if item exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#Change Item Value
thislist[1] = "blackcurrant"
print(thislist)

#Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print(thislist[3])

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append()
thislist.append("orange")
print(thislist)

#insert()
thislist.insert(1,"orange")
print(thislist)

#extend()
thislist = ["apple", "banana", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove()
thislist.remove("banana")
print(thislist)

#pop()
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist) # remove last item

#del
del thislist[0]
print(thislist)
del thislist

#clear()
list1.clear()
print(list1)

#Loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

[print(x) for x in thislist]

#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#newlist = [expression |for| item |in| iterable |if| condition == |True|]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#sort()
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sort(reverse = True)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#sort(key = function)
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist.sort(key = str.lower)
print(thislist)

#reverse()
thislist.reverse()
print(thislist)

#copy()
mylist = thislist.copy()
print(mylist)

#list()
mylist = list(thislist)
print(mylist)

#:(slice)
mylist = thislist[:]
print(mylist)

#Join Two List
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)