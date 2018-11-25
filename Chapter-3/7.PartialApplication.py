# Why Partial Application?
# One Application of Currying - Reuse Existing Functionality
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

def add(a, b, c, d):
    return a + b + c + d
a = curry(add)
print()
print("a(1)(2)(3)(4) = ", a(1,2)(3,4)())