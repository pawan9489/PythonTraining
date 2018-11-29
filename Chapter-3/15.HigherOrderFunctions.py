# Higher Order Functions
# Functions that can Take Functions or Return Functions or Both

# Helpful Higher Order Functions
# Map
# map(transformer, *Iterables) -> Iterable
print('_______MAP_______')
_10_times = lambda a : a * 10
lst = [-12, 3, 55, 26, 19]
lst1 = [10, 17, -53]
print(map(_10_times, lst))
for i in map(_10_times, lst): # ()
    print(i)

print()

# map(transformer with N_params, *N_Iterables)
# Stops when shortest one ends
def x(a, b):
    print(a, b)
[i for i in map(x, lst, lst1)]
print()
[print(i) for i in map(min, lst, lst1)]

print()
print('_______FILTER_______')
# Filter
# filter(filtering_function, Iterable)
lst = [-12, 3, 55, 26, 19]
print(filter(lambda i: not i % 2, lst))
for i in filter(lambda i: not i % 2, lst):
    print(i)

print()
print('_______REDUCE_______')
# Reduce
# reduce(function_2_params, Iterable)
# reduce(function_2_params, Iterable, seed_value)
lst = [-12, 3, 55, 26, 19]
from functools import reduce
print(reduce(lambda x, y: x + y, lst))
print(reduce(lambda x, y: x + y, lst, 10))

print()
print('_______ZIP_______')
# Zip
# zip(*iterables) # Stops when shortest one ends
fruits = 'apple', 'banana', 'cherry'
colors = 'red', 'yellow', 'black'
cost = 50, 5, 2
for f, c, cs in zip(fruits, colors, cost):
    print(f, c, cs)

print()
print('_______ENUMERATE_______')
# Enumerate
# Get Indices along with the Iterator
# enumerate(Iterator, counting_variable_start = 0)
for i, fruit in enumerate(fruits):
    print(i, fruit)

print()
for i, fruit in enumerate(fruits, 2):
    print(i, fruit)

print()
print('_______ANY_______')
# Any
# any(Iterable)
# returns True if any bool(x) is True
none_true = [0, 0, 0]
some_true = [0, 1, 0]
all_true  = [1, 2, 3]
print("any(none_true) = {0}".format(any(none_true)))
print("any(some_true) = {0}".format(any(some_true)))
print("any(all_true) = {0}".format(any(all_true)))
print("any([]) = {0}".format(any([])))

print()
print('_______ALL_______')
# All
# all(Iterable)
# returns True if all bool(x) are True
print("all(none_true) = {0}".format(all(none_true)))
print("all(some_true) = {0}".format(all(some_true)))
print("all(all_true) = {0}".format(all(all_true)))
print("all([]) = {0}".format(all([])))
