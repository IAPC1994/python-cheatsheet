# Tuple

"""
List: ordered, changeable and allow duplicate.
**Tuple: ordered, unchangeable and allow duplicate.
Set: unordered, unchangeable, unindexed and NO allow duplicate.
Dictionary: ordered, changeable, NO duplicate.
"""

thistuple = ("apple","banana","cherry","orange", "kiwi", "melon", "mango")
print(thistuple)

# Access to values
print(thistuple[1])
print(thistuple[-1])

# Check if item exists
if "cherry" in thistuple:
    print("Cherry exists!")

# Change a value of the tuple transforming it to list
list1 = list(thistuple)
list1[1] = "strawberry"
thistuple = tuple(list1)
print(thistuple)

# Add items (Doing the previous proccess or adding a tuple to another tuple)
thistuple2 = ("carrot",)
thistuple += thistuple2
print(thistuple)

# Delete a tuple
del thistuple2

# Unpacking a tuple
thistuple3 = ("apple","banana","cherry")
(green, yellow, red) = thistuple3
print(green, yellow, red)

#Using asterisk
(green2, yellow2, *red2) = thistuple
print(red2)

# For in tuple
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

# While
while i < len(thistuple):
    print(thistuple[i])
    i += 1