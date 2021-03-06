x, y, z = 11, 22, 33

# Deprecated Formatting
print("Numbers %d %d %d"%(x, y, z))

# Better way
print("Numbers {0} {1} {2}".format(x, y, z))

print()
# More Readable Format
a, b, c = 3, 4, 5
print("A Rectangle with sides {Width}, {Height}, {Breadth}".format(
    Width = a, 
    Height = b, 
    Breadth = c))

print()
# Precision Formatting
# After colon "width" is mandatory and rest are optional
# {message : {width}}
# {message : {fill_character}{push_direction}{width}}
# If Floating Value
# {message : {fill_character}{push_direction}{width}.{precision}}
print("Before {0:12} After".format(33))
print("Before {0:<12} After".format(33))
print("Before {0:$>12} After".format(33))
print()
print("Push {0:>12.4} Right".format(22/7))
print("Push {0:<12.4} Left".format(22/7))
# print("Push {0:a>12.4} Right".format(22/7))
