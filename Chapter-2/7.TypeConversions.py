# Iterconversions between data structures
l = [2, 3, 4, 5, 2]
t = ('a', 2, True, -4.5, True)
s = {False, 10, 34.5}
d = {'a': 1, 'b': 2}

print()
# List Contructor with multiple Iterables
print("list(list) = {0}".format(list(l)))
print("list(tuple) = {0}".format(list(t)))
print("list(set) = {0}".format(list(s)))
print("list(dictionary) = {0}".format(list(d)))

print()
# Tuple Contructor with multiple Iterables
print("tuple(list) = {0}".format(tuple(l)))
print("tuple(tuple) = {0}".format(tuple(t)))
print("tuple(set) = {0}".format(tuple(s)))
print("tuple(dictionary) = {0}".format(tuple(d)))

print()
# Set Contructor with multiple Iterables
print("set(list) = {0}".format(set(l)))
print("set(tuple) = {0}".format(set(t)))
print("set(set) = {0}".format(set(s)))
print("set(dictionary) = {0}".format(set(d)))

print()
# Dictionary Contructor with multiple Iterables
# print("dict(list) = {0}".format(dict(l))) # Error
# print("dict(tuple) = {0}".format(dict(t))) # Error
# print("dict(set) = {0}".format(dict(s))) # Error
print("dict(dictionary) = {0}".format(dict(d)))
print("dict(Iterable(tuple_with_2_elements)) = {0}".format(dict([(1,8), (4,9)])))

print()
# Type Checking
i = 2
f = 2.4
b = True
if type(i) is int:
    print("i is int")

if type(f) is float:
    print("f is float")

if type(b) is bool:
    print("b is bool")

if type(l) is list:
    print("l is list")

if type(t) is tuple:
    print("t is tuple")

if type(s) is set:
    print("s is set")

if type(d) is dict:
    print("d is dictionary")
