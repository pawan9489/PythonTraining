class Person:
    '''
        Person Class with Name and Age as Properties
        and Total as a Static Property
    '''
    total = 0 # Static Variable

    def __init__(self, _name, _age):
        # type(self).total += 1 # Static Variable
        Person.total += 1 # Static Variable
        self.name = _name # Instance Variable
        self.age = _age # Instance Variable
    
    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    @staticmethod
    def getTotal():
        return Person.total

    # Implicitly Pass the Type (Class Name) as the First argument
    @classmethod
    def totalPlusN(c, n):
        # print(c) # <class '__main__.Person'>
        return c.total + n

    def __str__(self):
        return "Name - {0}, Age - {1}".format(self.name, self.age)

p1 = Person('John', 25)
p2 = Person('Mary', 35)

print()
print("p1.getAge()", p1.getAge())
print()
print("Static Varaible -> Person.total", Person.total)
print()
print("Static Method -> Person.getTotal()", Person.getTotal())
print()
print("Static Method as Instance Method -> p1.getTotal()", p1.getTotal())
print()
print("Static Variable as Instance Variable -> p1.total", p1.total)
print()
print("Static Method -> Person.totalPlusN(10)", Person.totalPlusN(10))
print()
print("Instance Method as Static Method -> Person.getAge(p1)", Person.getAge(p1))

print('----')
for key in dir(p1):
    print("{0:20} - {1}".format(key, getattr(p1, key)))
print('----')