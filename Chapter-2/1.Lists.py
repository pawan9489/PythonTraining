# Basic Data Type of Sequence
# Can Contain Any type but prefer same type
# List is a collection which is ordered and changeable. Allows duplicate members.

l1 = [1,2,3,4,5]
l2 = [1, 'apple', True, -45.612]

print(l1, l2)

print()
# Length of List
print("len(l1) = {0}, len(l2) = {1}".format(len(l1), len(l2)))

print()
# Concatenating Lists
print("l1 + l2 = {0}".format(l1 + l2))

print()
# Repetition Lists
print("l2 * 2 = {0}".format(l2 * 2))
print("2 * l2 = {0}".format(2 * l2))

print()
# Indexing and Slicing same as discussed in the Strings section
print("l2[0] = {0}".format(l2[1]))
print("l2[:2:-1] = {0}".format(l2[:2:-1]))

print()
# Updating List
print("Before Updating - ", l2)
l2[1] = 'banana'
print("l2[1] = 'banana' => {0}".format(l2))
l2[1:3] = ['cherry', False, 33, -21]
print("l2[1:3] = ['cherry', False, 33, -21] => {0}".format(l2))

print()
# Delete List elements
print("Before Deleting - ", l2)
del l2[3]
print("del l2[3] => {0}".format(l2))
del l2[2:3]
print("del l2[2:3] => {0}".format(l2))
