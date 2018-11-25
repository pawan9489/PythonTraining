import pprint

pp = pprint.PrettyPrinter(indent=4)

g = 10
def func():
    l = 50
    print("Globals")
    pp.pprint(globals())    
    print()
    print("Locals")
    pp.pprint(locals())

func()

print('--------------------------')
a, b, x, y, z = 13, 5, 2, 8, 16
def m1(x, y):
    global a
    a = 35
    x, y = y, x
    b = 14
    b = 3
    c = 97
    print(a, b, x, y, z)
print()
m1(12, 7) # 
print(a, b, x, y, z) # 