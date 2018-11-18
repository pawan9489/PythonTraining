# Truthiness and Falsiness
# "None" -> like "null" in Java, C#
'''
    Type   ->  False Value
    =====================
    int    ->   0
    float  ->   0.0
    string -> '' or ""
    list   ->   []
    tuple  ->   ()
    set    ->   {}
    dict   ->   {}
'''
print("bool(0) = {0}".format(bool(0)))
print("bool(0.0) = {0}".format(bool(0.0)))
print("bool('') = {0}".format(bool('')))
print("bool([]) = {0}".format(bool([])))
print("bool(()) = {0}".format(bool(())))
r = r"bool({})"
print("{1} = {0}".format(bool({}), r))
print("bool(None) = {0}".format(bool(None)))
