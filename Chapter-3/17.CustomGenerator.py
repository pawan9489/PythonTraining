def my_generator():
    print('Yielding a')
    yield 'a' # Direct Yield
    print('Yielding b')
    yield 'b' # Direct Yield
    print('Yielding c')
    yield 'c' # Direct Yield

for char in my_generator():
    print(char)

def gen1():
    state = 0
    def helper():
        nonlocal state
        if state == 0:
            state = 1
            return 'a'
        elif state == 1:
            state = 2
            return 'b'
        elif state == 2:
            state = 3
            return 'c'
        else:
            raise StopIteration
    return helper

print()
f = gen1()
print(f())
print(f())
print(f())
# print(f())

def gen2():
    return_values = ['a', 'b', 'c']
    state = 0
    def helper():
        nonlocal state
        while state < len(return_values):
            state += 1
            return return_values[state - 1]
        raise StopIteration
    return helper

print()
g = gen2()
print(g())
print(g())
print(g())
# print(g())

def lazy_fibonacci():
    yield 1 # Direct Yield
    yield 1 # Direct Yield
    l = [1, 1]
    while True:
        l = [ l[-1], sum(l[-2:]) ]
        yield l[-1]

def fibo():
    return_values = [1, 1] # Direct Yields
    state = 0
    def helper():
        nonlocal state, return_values
        while True: # Infinite Stream of Values
            state += 1
            if state > 1 : # Non Direct Yields
                s = sum(return_values[-2:])
                return_values = [return_values[-1], s]
            return return_values[-1]
        raise StopIteration
    return helper

print()
f = fibo()
for _ in range(10):
    print(f())
