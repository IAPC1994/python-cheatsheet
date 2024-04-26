# Dictionary

"""
List: ordered, changeable and allow duplicate.
Tuple: ordered, unchangeable and allow duplicate.
Set: unordered, unchangeable, unindexed and NO allow duplicate.
**Dictionary: ordered, changeable, NO duplicate. (Like MAP)
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

# Access to items
print(thisdict["brand"])
print(thisdict.get("model"))

# Access to keys
x = thisdict.keys()
print(x)

# Access to values
x = thisdict.values()
print(x)

#Lenght
print(len(thisdict))

# Change a value
thisdict["year"] = 2020
thisdict.update({"year": 1964})
print(thisdict)

# Add new value
thisdict["color"] = "white"
print(thisdict)

# Get items
print(thisdict.items())

# Check if key exist
if "model" in thisdict:
    print("Yes, model exist in the dictionary")

# Removing items specified
thisdict.pop("color")
print(thisdict)

# Removing the last item
thisdict.popitem()
print(thisdict)

# Clear
thisdict2 = { "car": "Chevrolet", "model": "Corsa" }
thisdict2.clear()
print(thisdict2)

# For keys
for x in thisdict: 
    print(x)
# or
for x in thisdict.keys():
    print(x)



# For values
for x in thisdict:
    print(thisdict[x])
# or 
for x in thisdict.values():
    print(x)

# For key:value
for x,y in thisdict.items():
    print(x, y)

# Copy
thisdictcopy = thisdict.copy();

# Nested dictionaries
myFamily = {
    "mother": {
        "name": "Jessy",
        "year": 1963
    },
    "sister": {
        "name": "Ashley",
        "year": 1990
    }
}

print(myFamily["sister"]["name"])