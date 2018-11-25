# Functions as First Class Citizens
# Why Lambdas?
add = lambda a, b: a + b
print(add(1,3))

print()

def add1(a, b):
    return a + b
print(add1(1,3))

# Why Closures?
# Closures are functions that refer to independent (free) variables. In other words, the function defined in the closure ‘remembers’ the environment in which it was created.
#       Free variables are variables that are neither locally declared nor passed as parameter.

#   Performance - Close Over the State (free Variables)
#   Asynchronous