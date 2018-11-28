""" 
    Eager Evaluation - If you loop through a list, all elements are created in advance. This is Ineffficient, beacause - It consumes memory Not all elements may be used. This is often called eager evaluation. ex: Python 2 Range Vs Python 3 Range

    Lazy Evaluation - (Calculate on demand)
        If you loop through an Iterator, the iterator may create each element when it is called. This is Efficient, because - Only one element is kept in memory. Unused elements are never created.
"""

# Fibonacci - [1, 1, 2, 3, 5, 8, 13, 21, ....]
def eager_fibonacci(n):
    l = [1, 1]
    for i in range(2, n):
        l.append(sum(l[-2:]))
    print(l)
    return l[-1]

print(eager_fibonacci(10))

def lazy_fibonacci():
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [ l[-1], sum(l[-2:]) ]
        yield l[-1]

# Enumerate(iterator) - index, value
for i, n  in enumerate(lazy_fibonacci()):
    if i == 10:
        break
    print(n)
