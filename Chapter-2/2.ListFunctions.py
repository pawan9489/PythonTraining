l = [1, 'cherry', False, 33, -21, -45.612]

print()
# List Contructor
# list() - empty list
# list(iterable) - New List initialized with iterable items
# t = (1,2,3)
# print(type(t))
# lst = list(t)
lst = list((1,2,3))
print(lst)

print()
# Get Index of item
# Error if not exists -> ValueError: item is not in list
print("l.index(False) = {0}".format(l.index(False)))

print()
# Appending Lists
# append(item) # Only one item at a time appending
print("Before Appending - {0}".format(l))
l.append(True)
print("l.index('False') = {0}".format(l))

print()
# Insert at Index
print("Before Inserting - {0}".format(l))
l.insert(4, 9999)
print("l.insert(4, 9999) = {0}".format(l))

print()
# Membership
print("'apple' in l = {0}".format('apple' in l))

print()
# Remove Specific Item
# Error if not exists -> ValueError: item is not in list
print("Before Removing - {0}".format(l))
l.remove(33)
print("l.remove(33) = {0}".format(l))

print()
# Remove all elements
print("Before Clearing - {0}".format(l))
l.clear()
print("l.clear() = {0}".format(l))

l = [1, 'cherry', False, 9999, -21, -45.612, True]

print()
# pop() - removes last element and returns value
# pop(index) - removes the element at index and returns value
print("Before pop - {0}".format(l))
print("l.pop() = {0}".format(l.pop()))
print("After pop = {0}".format(l))
print("l.pop(3) = {0}".format(l.pop(3)))
print("After pop = {0}".format(l))

print()
# Copy the list - Shallow Copying
l_copy = l.copy()
print("l = {0}".format(l))
print("l.copy() = {0}".format(l_copy))

print()
# count
print("l = {0}".format(l))
print("l.count(False) = {0}".format(l.count(False)))

print()
# Reverse - In Place
print("l = {0}".format(l))
l.reverse()
print("l.reverse() = {0}".format(l))

print()
# Sort - In Place
# sort(key = None, reverse = False)
# TypeError: '<' not supported between instances of 'type1' and 'type2'
l = [12, 34, 5, 9, -14, 0, 2, 66, 17]
print("l = {0}".format(l))
l.sort()
print("l.sort() = {0}".format(l))

print()
# Looping
print("l = {0}".format(l))
for i in l:
    print(i)

print()
print("max(l) = {0}".format(max(l)))
print("min(l) = {0}".format(min(l)))

# Below are discussed after "Higher order Functions"
# filter
# Map
# flatMap
# reduce