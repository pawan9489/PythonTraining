class Person:
    '''
        Person Class with Name and Age as Properties
        and Total as a Static Property

        Private variables
            Job Title
            Is Employed
    '''
    total = 0 # Static Variable

    def __init__(self, _name, _age, _job, _isEmployed):
        type(self).total += 1 
        self.name = _name
        self.age = _age
        self.__job = _job
        self.__isEmployed = _isEmployed
    
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
print(p1.name)
print(p1.age)
# print(p1.__job)
# print(p1.__isEmployed)
# print(p1._Person__job)
# print(p1._Person__isEmployed)

print('----')
for key in dir(p1):
    print("{0:20} - {1}".format(key, getattr(p1, key)))
print('----')