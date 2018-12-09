# Python Doesn't Support Multiple Constructors like in C# or Java
# But can be acheived using @classmethod
class Person:
    '''
        Person Class with Name and Age as Properties
        and Total as a Static Property
    '''
    total = 0 # Static Variable

    def __init__(self, _name, _age, _job, _isEmployed):
        type(self).total += 1 
        self.name = _name
        self.age = _age
        self.job = _job
        self.isEmployed = _isEmployed
    
    @classmethod
    def fromName(c, _name):
        return c(_name, '', '', False)

    @classmethod
    def fromNameAndJob(c, _name, _job):
        return c(_name, '', _job, True)

    def __str__(self):
        return ", ".join(map(lambda t: t[0].capitalize() + ' - ' + str(t[1])
        , self.__dict__.items()))     

p1 = Person('John', 27, 'Manager', True)
print(p1)
print()
p2 = Person.fromName('Mary')
print(p2)
print()
p3 = Person.fromNameAndJob('Carlos', 'CEO')
print(p3)
