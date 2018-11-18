# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Looks like JSON
person = {
    'name': 'John',
    'job': 'Reporter',
    'age': 34
}
print(person)

print()
# Dictionary Constructor
# dict() - empty dictionary
# dict(key - value pairs)
# dict(iterable of Tuple with 2 elements)
# Looks like a Object creation in C#
p = dict(
    name = 'John', 
    job = 'Reporter', 
    age = 34
)
print(p)

print()
p = dict([
    ('name','John'), ('job', 'Reporter'), ('age', 34)
])
print(p)

print()
# fromkeys - Dictionary with Keys and No Values
# fromkeys(iterable)
# fromkeys(iterable, value)
print("dict.fromkeys([1,2,3,4]) = {0}".format(dict.fromkeys([1,2,3,4])))
print("dict.fromkeys([1,2,3,4], 0) = {0}".format(dict.fromkeys([1,2,3,4], 0)))

print()
# Adding new Key-Value Pairs
print("Before Adding - {0}".format(p))
p['phone'] = 123355
print("After Adding - {0}".format(p))

print()
# Accessing Items
print("p['name'] = {0}".format(p['name']))

print()
# Update Values
print("Before Updating - p['name'] = {0}".format(p['name']))
p['name'] = 'Jake'
print("p['name'] = {0}".format(p['name']))

print()
# Check If Key Exists
if "age" in p:
    print("Dictionary Contains 'age' key.")

print()
# Length of Dictionary = No. of Key value pairs
print("len(p) = {0}".format(len(p)))

print()
print('----- Keys -----')
# Looping
# Loop through Keys
# for key in p.keys
for key in p:
    print(key)

print()
print('----- Values -----')
# Loop through Values
# for value in p.values
for key in p:
    print(p[key])

print()
print('----- Key-Value -----')
# Loop through Key-Value
for key, value in p.items():
    print(key,value,sep=' -> ')

print()
# Removing Items
# pop(key) - removes the item and return the value back
# Raises KeyError if no key
# pop(key, default_value_to_return_back_if_no_key)
# del p[key] - removes the item
print("Before pop - {0}".format(p))
print("p.pop('phone') - {0}".format(p.pop('phone')))
print("After pop - {0}".format(p))

print()
print("Before del - {0}".format(p))
# Raises KeyError if no key
del p['job']
print("After del - {0}".format(p))

print()
# Clear all Key Value Pairs
print("Before clear - {0}".format(p))
p.clear()
print("After clear - {0}".format(p))