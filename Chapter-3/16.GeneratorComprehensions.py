# Generator Expressions
# can implement break-like behaviour

# List Comprehension - []
# Dictionary Comprehension - {}
# Generator Comprehension - ()
"""
    (map_item  Iterator)
    (map_item  Iterator  Filter_item) # Map item after filter same as SQL
"""

def fibonacci():
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]

def stop(): 
    raise StopIteration()

g = (i for i in fibonacci() if i < 10 or stop()) # Generator Object
for i in g:
    print(i)

# Nested Comprehensions
# Loops in a Loop
"""
    [map_items Outer_Iterator Filter_Outer_Iterator .... Inner_Iterators Filter_Inner_Iterators]
"""
print('------ Nested Loops ------')
grid = []
for x in range(2):
    for y in range(2):
        grid.append((x,y))
print(grid)

print([(x, y) for x in range(2) for y in range(2)])

print([(x, y) 
    for x in range(2) 
    if x >= 1 
    for y in range(2)])