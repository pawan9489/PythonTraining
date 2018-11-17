# Arithmetic operators 
# + - * / // % ** 

# Bitwise operators # Will Boost the Execution Speed
# & | ^ ~ << >>
print("12 & 14 = {0}".format(12 & 14))
print("12 & 1 = {0}".format(12 & 1))
print("13 & 1 = {0}".format(13 & 1))
# Will be discussed Later in Sets

# Assignment operators
# +=  -=  *=  /=  //=  %= 
# **=  &=  |=  ^=  >>=  <<= 

# Comparison operators
# ==  !=  >  <  >=  <= 

print()
# Logical operators
# and (&&)  or (||)  not(!)
x = 12
print("x > 5 and x < 10 = {0}".format(x > 5 and x < 10))
print("x > 5 or x < 10 = {0}".format(x > 5 or x < 10))
print("not(x > 5 or x < 10) = {0}".format(not(x > 5 or x < 10)))

print()
# Identity operators (Compare Objects)
# Reference Comparision
a = 2
b = 1 + 1
print("a is b = {0}".format(a is b))
print("a is not b = {0}".format(a is not b))

print()
# Membership operators (Presence of Sequence in an Object)
a = "Bucket"
b = "et"
print("b in a = {0}".format(b in a))
print("a not in b = {0}".format(a not in b))
