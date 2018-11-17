# String Indexing
x = 'Python Programming'
print("x[10] - {0}".format(x[10]))
# IndexError: string index out of range
# print("x[100] - {0}".format(x[100]))

print()
# String Slicing
# [start : exclusive_end]
# [start : exclusive_end : step_with_direction]
# [start : exclusive_end] = [start : exclusive_end : 1]
print("x[2:5] - {0}".format(x[2:5]))

start = 3
end = 7
print(x[start:end]) # start -> end-1
print(x[start:])    # start -> rest of the array
print(x[:end])      # beginning -> end-1
print(x[:])         # a copy of the whole array
print(x[:-100])     # No Idea, Why no Error

print()
step = 2
print(x[start:end:step])
print(x[::-1])    # all items in the array, reversed
print(x[1::-1])   # the first two items, reversed
print(x[:-3:-1])  # the last two items, reversed
print(x[-3::-1])  # everything except the last two items, reversed
print(x[::])      # a copy of the whole array
print(x[::-100])  # No Error, if step is more than the elements