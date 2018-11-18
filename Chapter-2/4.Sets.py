# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
fruits = {'apple', 'banana', 'apple', 'cherry'}
print(type(fruits))
print(fruits)

print()
# Set Constructor
# set() - empty set
# set(iterable) - New set initialized with iterable items
s = set([1,2,3,2,1])
print(s)

print()
# No Indexing - Since no ordering but we can Loop
for fruit in fruits:
    print(fruit)

print()
# Membership
print("'cherry' in fruits = {0}".format('cherry' in fruits))

print()
# Only appending No Updating Items - Since no Indexing
# Add items
print("Before adding = {0}".format(fruits))
fruits.add('mango')
print("fruits.add('mango') = {0}".format(fruits))

print()
# Add Multiple items
print("Before Multiple adding = {0}".format(fruits))
fruits.update(['orange', 'grapes'])
print("fruits.update(['orange', 'grapes']) = {0}".format(fruits))

print()
# Length of Set
print("len(fruits) = {0}".format(len(fruits)))

print()
# Remove Item
# remove(item) - will throw error if item dont exist
# discard(item) - will not throw error if item dont exist
print("Before removing = {0}".format(fruits))
fruits.remove('grapes')
print("fruits.remove('grapes') = {0}".format(fruits))

print()
# pop - remove some random element - Since no Indexing
# only pop(), not pop(index) - Since no Indexing
print("Before pop = {0}".format(fruits))
print("fruits.pop() = {0}".format(fruits.pop()))

print()
# clear()
print("Before clear = {0}".format(fruits))
fruits.clear()
print("fruits.clear() = {0}".format(fruits))