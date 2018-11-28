# Why Partial Application?
# One Application of Currying - Reuse Existing Functionality

def addA(f, a):
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

print('---  Double  ---')
double = lambda i : i * 2
print(addA(double, 1))
print(addA(double, 1)(2))
print(addA(double, 1)(2)(3))
print(addA(double, 1)(2)(3)(4))
print('---  Triple  ---')
triple = lambda i : i * 3
print(addA(triple, 1))
print(addA(triple, 1)(2))
print(addA(triple, 1)(2)(3))
print(addA(triple, 1)(2)(3)(4))

