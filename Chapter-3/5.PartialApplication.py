
# Why Partial Application?
def nth_power(n):
    return lambda a : a ** n

square = nth_power(2)
cube = nth_power(3)

print(square(3))
print(cube(3))

def increment_by_n(n):
    return lambda x: x + n

add2 = increment_by_n(2)

print(add2(45))