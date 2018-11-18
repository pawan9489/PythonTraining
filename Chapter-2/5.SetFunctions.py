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

print()
# difference Update
print("Before Difference Update - s1 = {0}".format(s1))
print("s2 = {0}".format(s2))
s1.difference_update(s2)
print("s1.difference_update(s2) = {0}".format(s1))

s1 = {1, 2, 3, 4}
print()
# Intersection Update
print("Before Intersection Update - s1 = {0}".format(s1))
print("s2 = {0}".format(s2))
s1.intersection_update(s2)
print("s1.intersection_update(s2) = {0}".format(s1))

print()
# isdisjoint - Returns whether 2 sets have intersection
print("s1.isdisjoint(s2) = {0}".format(s1.isdisjoint(s2)))
r = r"{1,2}.isdisjoint({3,4})"
print("{1} = {0}".format({1,2}.isdisjoint({3,4}), r))

print()
# issubset & issuperset
r = r"{1,2}.issubset({3,4})"
print("{1} = {0}".format({1,2}.issubset({3,4}), r))
r = r"{1,2}.issubset({1,2,3,4})"
print("{1} = {0}".format({1,2}.issubset({1,2,3,4}), r))
r = r"{1,2,3,4}.issuperset({1,2,3,4})"
print("{1} = {0}".format({1,2,3,4}.issuperset({1,2,3,4}), r))