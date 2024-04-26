"""
List: ordered, changeable and allow duplicate.
Tuple: ordered, unchangeable and allow duplicate.
Set: unordered, unchangeable, unindexed and NO allow duplicate.
Dictionary: ordered, changeable, NO duplicate.
"""

list = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]

# First position
print(list[1])
# Last position
print(list[-1])

# Range of indexes

print(list[2:5])
print(list[:4])
print(list[2:])

# Item exist
if("apple" in list):
    print("Apple exist")

# Change Item Value
list[1]="blackcurrant"
print(list)

# Change a Range of item values
list[1:3] = ["blackcurrant", "watermelon"]
print(list)

#Insert items in specific index without replace it
list.insert(2, "tuna")
print(list)

#Add items
list.append("onion")
print(list)

#Extend list
list2 = ["lettuce","carrot"]
list.extend(list2)
print(list)

#Remove item
list.remove("onion")
print(list)

#Remove specified index
list.pop(5)
print(list)

#Remove last
list.pop()
print(list)

#Delete a list
del list2

#Clear a list
#list.clear()
#print(list)

# For in list
for x in list:
    print(x)

for i in range(len(list)):
    print(list[i])

# While
while i < len(list):
    print(list[i])
    i += 1

# Comprehension
newlist = [x for x in list if "a" in x]
print(newlist)

# Sort
newlist.sort()
print(newlist)

# Sort reverse
newlist.sort(reverse=True)
print(newlist)

# Reverse the list
newlist.reverse()
print(newlist)

# Copy a list
newlist2 = list.copy();
#or
#newlist2 = list(list)

# Join two lists
list3 = newlist + list
print(list3)