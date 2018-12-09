'''
    Class Like Structures in Functional Style:
        Tuple
        Dictionary
        Named Tuple

    Classes
'''
d = dict(
    name = 'John',
    age = 29
)
print('- Normal Dictionary -')
print(d)

# Class Analogy
def createPerson(_name, _age):
    return dict(
        name = _name,
        age = _age
    )

print()
print('- Factory Function to Create Dictionaries -')
print(createPerson('John', 19))
print(createPerson('Mary', 45))

# What is the Difference between Dictionary or Named Tuple and a Class?

class Person:
    'Person Class with Name and Age as Properties'
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age
    
    def __str__(self):
        return "Name - {0}, Age - {1}".format(self.name, self.age)
        # return ", ".join(map(lambda t: t[0].capitalize() + ' - ' + str(t[1])
        # , self.__dict__.items())) 

print()
print('- Using Classes -')
p = Person('John', 30)
print("p - {0}".format(p))
print(p.name, p.age)
print(p.__dict__)

# To Prove the Classes are Dictionaries
print()
print('After Adding a Key')
p.job = 'Manager'
print("p - {0}".format(p))
print(p.__dict__)
del p.job
print(p.__dict__)

# Getters and Setters
print()
print(' Getters and Setters ')
print(p.age) # Getter
p.age = 99 # Setter
print(p.age)

print()
# Generic Getters and Setters
# getattr(object, property_name)
# setattr(object, property_name, value)
print(getattr(p, 'age'))
setattr(p, 'age', 70)
print(getattr(p, 'age'))

# Get all avaliable functions on an Object
print()
print(dir(p))
print('----')
for key in dir(p):
    print("{0:20} - {1}".format(key, getattr(p, key)))
print('----')