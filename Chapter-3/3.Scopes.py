# WHY Function inside a Function ??
#   Abstraction (Hiding) (Security)
#   Simplification (Dont see Unncessary) - Inner() is only used by Outer()
#   Currying - Get specialized functions from more general functions
#   Partial Application - Reuse Existing Functionality
g = 0
def outer():
    o = 2
    def inner():
        i = 10
        print("Inner - g", g, id(g))
        print("Inner - i", i, id(i))
        print("Inner - o", o, id(o))
        # Below Code Creates new 'o' variable
        # o = 20 # will loose the outer 'o'
        # print("Inner - o", o, id(o))
    print("Outer - g", g, id(g))
    print("Outer - o", o, id(o))
    inner()
    print("Outer - o", o, id(o))
    print(x)

# Comment x and see failure
x = 'Python'
outer()
# x = 'Python'

print()
# Simplification - Factorial Example via Tail Recursion
def fact(number, accumulation):
    if number <= 1:
        return accumulation
    else:
        return fact(number - 1, number * accumulation)
print(fact(5, 1))

def factorial(number):
    def fact(number, accumulation):
        if number <= 1:
            return accumulation
        else:
            return fact(number - 1, number * accumulation)
    return fact(number, 1)
print(factorial(5))

print()
# Abstraction
def person(name, job, age):
    # Private Variables
    ssn = age * 12 + 333

    # Private Function
    def getAge():
        return age

    def getSSN():
        return ssn

    # Public Funtion
    def printName(name):
        print("Name of Person : ", name, 
            " and person's age is", getAge(),
            "SSN -> ", getSSN())
    
    # Public API
    return dict(
        n = name,
        j = job,
        p = printName # How does this work in JS?
    )
p1 = person('John', 'Detective', 30)
p2 = person('Mary', 'Doctor', 50)

p1_name = p1['n']
p2_name = p2['n']
print(p1_name)
print(p2_name)

p1['p'](p1_name)
p2['p'](p2_name)
