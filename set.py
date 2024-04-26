# Set 

"""
List: ordered, changeable and allow duplicate.
Tuple: ordered, unchangeable and allow duplicate.
**Set: unordered, unchangeable, unindexed and NO allow duplicate.
Dictionary: ordered, changeable, NO duplicate.
"""

thisset = {"apple","banana","cherry"}
print(thisset)

# Access items
for x in thisset:
    print("")

print("banana" in thisset)

# Add items
thisset.add("orange")
print(thisset)

# Add sets, list o tuples to set using update or union
thisset2 = {"pineapple","mango","papaya"}
thisset.update(thisset2)
print(thisset)

# Remove item
# Remove: if the item doesnt exist, will raise an error
thisset.remove("papaya")
print(thisset)

# Discard: if the item doesnt exist, will NOT raise an error
thisset.discard("papaya")
print(thisset)

#Clear
#thisset2.clear()
#print(thisset2)

# Delete
# del thisset2

#intersection: Keeps only the duplicates
thissetintersection = thisset.intersection(thisset2) # or thisset & thisset2
print(thissetintersection)

#difference: keeps the items from the first set that are not in the other set
thissetdifference = thisset.difference(thisset2) # or thisset - thisset2 
print("Difference", thissetdifference)

#symmetric_difference: keeps all items except the duplicates
thissetsymdifference = thisset2.symmetric_difference(thisset)
print(thissetsymdifference)