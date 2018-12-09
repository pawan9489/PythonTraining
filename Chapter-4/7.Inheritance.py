# Inheritance - Parent Child Relationship
# Syntax - class Class_Name(parent1, parent2, ...):
class Parent(object):
    def __init__(self, _p1, _p2):
        print('Parent Constructor Called')
        self.p1 = _p1
        self.p2 = _p2

    def printObject(self):
        return "Parent({0}, {1})".format(self.p1, self.p2)
    
    def parentMethod(self):
        return 1

class Child1(Parent):
    'Wanted to add 2 Numbers that the parent object hold'
    # If no Constructor then the Parent Constructor is Called
    # Used when we want to add extra Functions to Some existing class without Modifying it
    def add(self):
        return "In Child1 Adding {0} , {1} = {2}".format(
            self.p1, self.p2, self.p1 + self.p2 
        )

print('>> Creating Parent Object')
parent = Parent(1, 2)
print("parent.parentM1()", parent.printObject())
print()
print('>> Creating Child1 Object')
child1 = Child1(2, 3)
print("child1.add()", child1.add())
print("child1.parentM1()", child1.printObject())

class Child2(Parent):
    def __init__(self, _c1, _c2):
        print('Child2 Constructor Called')
        self.c1 = _c1
        self.c2 = _c2
        # Not Manadatory to Invoke Parent Constructor unlike Other Languages like C# or Java
        # Can Invoke Parent Constructors and Include their 
        super().__init__(1, 2)

    # Overloading the Parent Method
    def printObject(self):
        return "Child2({0}, {1}) with Parent({2}, {3})".format(
            self.c1, self.c2, self.p1, self.p2)

print()
print('>> Creating Child1 Object')
child2 = Child2(4, 5)
print("child2.c1", child2.c1)
print("child2.c2", child2.c2)
print("child2.p1", child2.p1)
print("child2.p2", child2.p2)
print("child2.parentM1()", child2.printObject())
print(dir(child2))
print(dir(Child2))