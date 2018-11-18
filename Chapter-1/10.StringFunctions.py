# Includes - in (Membership operator)
# Item in Sequence -> Returns Bool
print("a in apple ? {0}".format('a' in "apple"))
print("A in apple ? {0}".format('A' in "apple"))
print("A not in apple ? {0}".format('A' not in "apple"))
print()
print("gram in Programming ? {0}".format('gram' in "Programming"))

print()
# Trim Extra Spaces
# strip(string) - removes from both sides of string
# lstrip(string) - removes from left side
# rstrip(string) - removes from right side
print("'Python    '.strip() = '{0}'".format('Python    '.strip()))
print('abcba'.strip('ab'))
print('abcba'.lstrip('ab'))
print('abcba'.rstrip('ab'))

print()
# Length of a String
print("len('Python') = {0}".format(len('Python')))

print()
# Convert to Lower Case
print("'Python'.lower() = {0}".format('Python'.lower()))

print()
# Convert to Upper Case
print("'Python'.upper() = {0}".format('Python'.upper()))

print()
# Replace a string with Another
print("'Python'.replace('Py', 'IronPy') = {0}".format('Python'.replace('Py', 'IronPy')))

print()
# Split the String into Substrings by using a Seperator
print("'Apple, Banana, Carrot'.split(',') = {0}".format('Apple, Banana, Carrot'.split(',')))
