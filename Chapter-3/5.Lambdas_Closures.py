# Functions as First Class Citizens
# Why Lambdas?
add = lambda a, b: a + b
print(add(1,3))

print()

def add1(a, b):
    return a + b
print(add1(1,3))

# Why Closures?
#   Performance - Close Over the State (free Variables)
#   Asynchronous