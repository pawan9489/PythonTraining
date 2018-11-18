# String Indexing
x = 'Python Programming'
print("x[10] - {0}".format(x[10]))
print("x[-8] - {0}".format(x[-8]))
# IndexError: string index out of range
# print("x[100] - {0}".format(x[100]))

print()
# String Slicing
# [start : stop]
# [start : stop : step_with_direction]
# [start : stop] = [start : stop : 1]
print("x[2:5] - {0}".format(x[2:5]))

start = 3
stop = 10
print(x[start:stop]) # start -> stop
print(x[start:])    # start -> rest of the array
print(x[:stop])      # beginning -> stop
print(x[:])         # a copy of the whole array
print(x[:-100])     # No Idea, Why no Error

print()
step = 2
print(x[start:stop:step])
print(x[::-1])    # all items in the array, reversed
print(x[1::-1])   # the first two items, reversed
print(x[:-3:-1])  # the last two items, reversed
print(x[-3::-1])  # everything except the last two items, reversed
print(x[::])      # a copy of the whole array
print(x[::-100])  # No Error, if step is more than the elements