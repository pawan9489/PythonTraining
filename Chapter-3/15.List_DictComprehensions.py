# List Comprehesions
# Processing a List in a single Expression
"""
    Statements - Instructions to compiler or Interpreter to do something
        ex: 'For' loop is a statement
    They don't evaluate to something

    Expressions - Anything that evaluates to something
        ex: 10 + 30
        ex: list Comprehension (Alternative to 'for' statement)

    [map_item  Iterator]
    [map_item  Iterator  Filter] # Map item after filter same as SQL
"""
from math import sqrt

print('---- Looping ----')
for i in range(5):
    print(sqrt(i))

print()
sq = [sqrt(i) for i in range(5)]
print(sq)

print('---- Filtering ----')
for i in range(5):
    if not i & 1 : print(i)

print()
sq = [i for i in range(5) if not i & 1]
print(sq)

print('-- Draw Back --')
# Can't break
def fibonacci():
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]

for i in fibonacci():
    if i > 10: 
        break
    print(i)

print()
# Filters values not Breaks => Infinite Loop
# [i for i in fibonacci() if i <= 10]

# Dictionary Comprehensions
"""
    {map_Key_Value  Iterator}
    {map_Key_Value  Iterator  Filter_Key_Value} # Map Key_Value after filter same as SQL
"""
print(' _________ Dictionary Comprehensions _________')
fruits = 'apple', 'banana', 'cherry'
colors = 'red', 'yellow', 'black'

d = dict(zip(fruits, colors))
print(d)

print()
d = {}
for f, c in zip(fruits, colors):
    d[f.capitalize()] = c.capitalize()
print(d)

print({ f.capitalize(): c.capitalize() for f, c in zip(fruits, colors)})
print({ 
    f.capitalize(): c.capitalize() 
    for f, c in zip(fruits, colors) 
    if not c == 'red'
})

"""
    C# LINQ or SQL like syntax

    select f.capitalize(), c.capitalize() 
    from zip(fruits, colors)
    where c <> 'red'
"""

