# Non-Locals
# Assign values to a variable in an outer (but non-global) scope.

import pprint
pp = pprint.PrettyPrinter(indent=4)

g = 0
def outer():
    o = 10
    def inner1():
        i1 = 20
        def inner2():
            i2 = 30
            # global o # Error for Non-Global
            # nonlocal g # Error for Globals
            nonlocal o
            o = 50
            print("inner2 :", o)
            pp.pprint(globals())
            print()
            pp.pprint(locals())
        inner2()
    inner1()
    print("Outer :", o)

outer()
