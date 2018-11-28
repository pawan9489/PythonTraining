# Why Currying? - Reusability
# Get specialized functions from more general functions
# Convert's N-Arity Function to N 1-Arity Functions

def add(a, b, c, d):
    return a + b + c + d
print("add(1,2,3,4) = ", add(1,2,3,4))

def addA(a):
    def addB(b):
        def addC(c):
            def addD(d):
                return a + b + c + d
            return addD
        return addC
    return addB

print()
addAll = lambda a : lambda b : lambda c : lambda d : a + b + c + d

print(addAll(1)(2)(3)(4))

addAll = lambda a : (
    lambda b : ( 
        lambda c : ( 
            lambda d : (
                a + b + c + d
            )
        )
    )
)

print(addAll(1)(2)(3)(4))

add_1_2 = addAll(1)(2)
print("add_1_2(5)(10) =", add_1_2(5)(10))

print()
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

def curry(func):
    f_args = []
    f_kwargs = {}
    def f(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            f_args += args
            f_kwargs.update(kwargs)
            return f
        else:
            return func(*f_args, *f_kwargs)
    return f

def add3(a, b, c, d):
    return a + b + c + d
a = curry(add3)
print()
print("a(1)(2)(3)(4) = ", a(1)(2)(3)(4)())
