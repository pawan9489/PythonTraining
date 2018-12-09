# Inheriting Implementations from Multiple Parents

class Parent1:
    def Method_fromParent1(self):
        print("Method_fromParent1() is called")

    def common(self):
        print("Common() from Parent1")
    
class Parent2:
    def Method_fromParent2(self):
        print("Method_fromParent2() is called")

    def common(self):
        print("Common() from Parent2")

# Applied from Left to Right
class Child(Parent1, Parent2):
    pass

c = Child()
c.Method_fromParent1()
c.Method_fromParent2()
c.common()

# Method Resolution Order
print(Parent1.__mro__)
print(Parent2.__mro__)
print(Child.__mro__)
