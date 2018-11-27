# Iterator - An Object that contains multiple other objects
#   Objects that can be used in "FOR" loop
# Ordered Iterator - Elements are in Predictable Order
# UnOrdered Iterator - Elements are in UnPredictable Order

# Unpacking Tuples
fruits = 'apple', 'banana', 'cherry', 'mango'
a, b, c, d = fruits
print(a, b, c, d)

print()
# *Rest
a, *r, b = fruits
print(a, r, b)

print()
a, b, *r = fruits
print(a, b, r)

print()
# Nested Unpacking
fruits = ('apple', 'banana'), 'cherry', 'mango'
(a, b), c, d = fruits
print(a, b, c, d)


# Unpacking Dictionary
fruits = {
    'apple': 'Green',
    'banana': 'Yellow',
    'cherry': 'Red'
}

print()
(k1, v1), (k2, v2), (k3, v3) = fruits.items()
print(k1, v1)
print(k2, v2)
print(k3, v3)

# Iterator Protocol
#   - Supports "in" and "for"
# Iterators don't Necessarily have a length - DB fetch data
# Iterators don't Necessarily Support Indexing - Set or Dictionary
"""
    iter() # provides an Iterator Object
    next() # retrieves elements from the iterator object
    StopIteration # Exception raised when iterator exhasted
"""
print()
l = [10, 20, 30, 40]
i = iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) # StopIteration Error

i = iter(l)
print()
while True:
    try:
        print(next(i))
    except StopIteration:
        break

# Can implement your own Iterators using Class with __iter__() & __next__()