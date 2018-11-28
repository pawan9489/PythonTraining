# collections.namedTuple
# Tuples with Names
from collections import namedtuple
# namedtuple(TypeName, fields)
# Functional Data Constructors
Pn = namedtuple('Person', ['name', 'age']) # Class - Person
p = Pn(name = "Python", age = 28)
print(p) # Person(name='Python', age=28) # ToString()
print(p[0], p.name)
print(p[1], p.age)

# collections.orderedDict
# Python 3.6 order of insertion is preserved in Dictionary
from collections import OrderedDict
d = OrderedDict([
    ('Apple', 'Red'),
    ('Banana', 'Yellow'),
    ('Cherry', 'Black')
])

d1 = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Cherry': 'Black'
}

print()
for fruit, color in d.items():
    print("{0} is {1}".format(fruit, color))
print()
for fruit, color in d1.items():
    print("{0} is {1}".format(fruit, color))

# collections.deafultdict
# Returns a default value for non-existing keys, rather than KeyError
from collections import defaultdict

fav_programming_languages = {
    'John': 'Haskell',
    'Jake': 'Scala',
    'Clarie': 'JavaScript'
}
print()
# print(fav_programming_languages['Mark'])
d = defaultdict(lambda: 'Python')
d.update(fav_programming_languages)
print(d['Mark'])
print(d['Jake'])
print(d)

