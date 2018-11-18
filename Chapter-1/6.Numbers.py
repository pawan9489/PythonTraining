# 3 Numeric Types
x, y, z = 10, -4.22, 2 + 4j

print("{x} - {tx}\n{y} - {ty}\n{z} - {tz}".format(
    x = x,tx = type(x), 
    y = y,ty = type(y),
    z = z,tz = type(z)))

print()

# e - Power of 10 => xe5 = x * 10 ** 5
sx = 1.553e4 # 1E4
print(sx)

# Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
# w = int("3.4") # ValueError: invalid literal for int() with base 10: '3.4'

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'