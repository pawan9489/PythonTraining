'''
  OR    |   Union
  AND   &   Intersection
  NOT   -   Difference
  XOR   ^   Symmetric Difference
'''
s1 = {1,2,3,4}
s2 = {5,6,3,4}

print("Union: s1 | s2 = {0}".format(s1 | s2))
print()
print("Intersection: s1 & s2 = {0}".format(s1 & s2))
print()
print("Difference: s1 - s2 = {0}".format(s1 - s2))
print()
print("Difference: s2 - s1 = {0}".format(s2 - s1))
print()
print("Symmetric Difference: s1 ^ s2 = {0}".format(s1 ^ s2))