# Can Contain Any type
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
x = 1, 2, 3
print(type(x))
print(x)

print()
# Common Syntax
t = (1, 2, 3)
print(type(t))
print(t)

print()
# empty tuple
e = ()
print(type(e))
print(e)

print()
# One Element tuple
o = (1,)
print(type(o))
print(o)

print()
# No Updations since immutable
# TypeError: 'tuple' object does not support item assignment
print("t = {0}".format(t))
# t[1] = 22
print("t[1] = 22 =>  {0}".format(t))

# No deleting items

print()
# Concatenation of 2 Tuples
print("t = {0}".format(t))
print("t + t = {0}".format(t + t))

# Indexing, Slicing, len, membership and repetition same as Lists

print()
#  Looping
for i in t:
    print(i)
