
# Why Currying? - Reusability

f = lambda i : i * 2

def addA(a):
    a = f(a) # Some Computation with Given params
    def addB(b):
        b = f(b)
        def addC(c):
            c = f(c)
            def addD(d):
                d = f(d)
                return a + b + c + d
            return addD
        return addC
    return addB

print(addA(1))
print(addA(1)(2))
print(addA(1)(2)(3))
print(addA(1)(2)(3)(4))

