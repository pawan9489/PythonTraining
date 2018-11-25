# Local and Global Scope
# Global variable - Variables declared outside of Every Function
# Local variable - Variables declared inside of a Function

g = 0 # Global Variable
def func():
    i = 30 # Local Variable
    print("From Inside Func() - i = ", i)
    print("From Inside Func() - g = ", g)
print('---- Global Variables ---')
func()
# print(i) # NameError: name 'i' is not defined
print("From Outside Func() - g = ", g)
print()

# Modify Global Variables
g = 0
def func1():
    g = 10
    print("From Inside Func1() - g = ", g)

print('---- Modify Global Variables ---')
func1()
print("From Outside Func1() - g = ", g)
print()

g = 0
def func2():
    global g
    g = 10
    print("From Inside Func2() - g = ", g)

print('---- Modify Global Variables ---')
func2()
print("From Outside Func2() - g = ", g)
print()

# g = 0
# def outer():
#     o = 2
#     def inner():
#         i = 10
#         print("Inner - g", g, id(g))
#         print("Inner - i", i, id(i))
#         print("Inner - o", o, id(o))
#         # Below Code Creates new 'o' variable
#         # o = 20 # will loose the outer 'o'
#         # print("Inner - o", o, id(o))
#     print("Outer - g", g, id(g))
#     print("Outer - o", o, id(o))
#     inner()
#     print("Outer - o", o, id(o))
#     print(x)

# # Comment x and see failure
# x = 'Python'
# outer()
# # x = 'Python'


