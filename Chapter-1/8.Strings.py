# Single and Double Quotes
print('Python')
print("Python")

print()
print("Python's")
print('Hey "Python"')

print()
# Escape Characters
print('Python\'s')
print("Hey \"Python\"")

print()
type = 'dynamic'
name = 'Python'
age = 28
text = "{0} is {1} years old and {2} typed Language.".format(
    name, age, type)
print(text)

print()
# String Concatenation
print(type + ' ' + name)

print()
# String Repetition
print(name * 3)
print(3 * name)

print()
# Raw Strings
raw_string = r"\asddasdas\t \n \asdf!@#$%^&*()"
print(raw_string)