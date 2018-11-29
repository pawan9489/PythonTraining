# Custom Key Sorting
# list.sort(key=..., reverse=...) # Object Oriented Way
# sorted(list, key=..., reverse=...) # Functional Way
lst = [-12, 3, 55, 26, 19]
# Inplace Sort
print(lst.sort()) # Returns None like Void function
print(lst)
lst = [-12, 3, 55, 26, 19]
# Returns a New Iterable 
print(sorted(lst)) # Returns Iterable
print(lst)

# Key Sorting
# key = lambda a : 
print('___ Key Sorting ___')
lst = ["Output", "Apple", "Code"]
print(sorted(lst))
print(sorted(lst, key = len))
"""
    lst = ["Output", "Apple", "Code"]
    key = len # Think like map Item to some value and Compare mapped results
    temp = [6, 5, 4]
    sort via Key
    temp = [4, 5, 6]
    ["Code", "Apple", "Output"]
"""
# Reverse
# reverse = True or False(default)
print('___ Reverse ___')
print(sorted(lst, key = len, reverse = True))

print()
from collections import namedtuple

def printPersons(persons):
    [print(person) for person in persons]

Person = namedtuple('Person', ['id','name', 'age']) # Class - Person
p1 = Person(id = 1, name = "Bob", age = 32)
p2 = Person(id = 2, name = "Mark", age = 12)
p3 = Person(id = 3, name = "John", age = 70)
p4 = Person(id = 4, name = "Bob", age = 27)
p5 = Person(id = 5, name = "Watson", age = 12)

persons = p1, p2, p3, p4, p5

# Multiple Key Sorting
# like in SQL ::  column_1 asc, column_2 desc, column_3 asc

# Order By age
x = sorted(persons, key = lambda p: p.age)
print('__ Sorted Via Age Asc __')
printPersons(x)

print()
print('__ Sorted Via Age Asc and ID Desc __')
x = sorted(
        sorted(persons, key = lambda p: p.age),
        key = lambda p: p.id, 
        reverse = True
)
printPersons(x)
