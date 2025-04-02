#Set is unordered, unchangeable, unindexed and no duplicate

#Create
thisset = {"apple", "banana", "cherry"}
print(thisset)

#No duplicates
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
thisset = {False, True, 0}
print(thisset)

#len()
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"abc", 34, True, 40, "male"}
print(set1)
print(type(set1))

#set()
thisset = set(("apple", "banana", "cherry"))
print(thisset)

#Acces items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("banana" in thisset)
print("banana" not in thisset)

#add()
thisset.add("orange")
print(thisset)

#Add Sets update()
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove() if the item does not exist -> error
thisset.remove("banana")
print(thisset)

#discard() if the item does not exist -> no error
thisset.discard("apple")
print(thisset)

#Remove a random item pop()
x = thisset.pop()
print(x)
print(thisset)

#clear()
thisset.clear()
print(thisset)

#del
del thisset

#Loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#Join
#union() or |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set3 = set1 | set2
print(set3)

set3 = {"John", "Elena"}
set4 = {"apple", "banana", "Cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
myset = set1 | set2 | set3 | set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#intersection or & will return a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
set3 = set1 & set2
print(set3)

#intersection_update() will change the original set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#differene() or -
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
set3 = set1 - set2
print(set3)

#difference_update()
set1.difference_update(set2)
print(set1)

#symmetric_difference() or ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
set3 = set1 ^ set2
print(set3)

#symmetrich_difference_update()
set1.symmetric_difference_update(set2)
print(set1)