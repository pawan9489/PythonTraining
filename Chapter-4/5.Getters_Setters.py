'''
class Obj:
    @property
    def attribute(self): # implements the get - this name is *the* name
        return self._attribute
    
    @attribute.setter
    def attribute(self, value): # name must be the same
        self._attribute = value
    
    @attribute.deleter
    def attribute(self): # again, name must be the same
        del self._attribute
'''
class Person:
    def __init__(self, n, a):
        self.name = n # Calling the Setter Function
        self.age = a # Calling the Setter Function

    @property # Getter
    def name(self): # Even though "name" is a function, can access as a variable
        print("getter of name called")
        return self._name # Access Instance Variable

    @name.setter # Setter
    def name(self, value):
        print("setter of name called")
        self._name = value # Create Instance Variable

    @name.deleter
    def name(self):
        print("deleter of x called")
        del self._name

    @property
    def age(self):
        return self.age
    
    @age.setter
    def age(self, value):
        if value != int(value):
            raise TypeError("Age must be an integer")
        if 20 <= value <= 100:
            self._age = int(value) # Create Instance Variable
        else: # It is an Integer and out of Bounds
            raise ValueError("Age must be " +
                             "between 20 and 100 inclusive")

    def __str__(self):
        return ", ".join(map(lambda t: t[0].capitalize() + ' - ' + str(t[1])
        , self.__dict__.items())) 

p = Person('Jake', 42)
print(p.__dict__)
p.name = 'John'  # setter called
print(p.__dict__)
john = p.name    # getter called
print("p._name -> ", p._name)
print(p.__dict__)
del p.name       # deleter called
print(p.__dict__)

print()
# p.age = "40" # TypeError: Age must be an integer
# p.age = 400 # ValueError: Age must be between 0 and 100 inclusive
# ******   Make Illegal State of an Object Un-Representable   ******
# print(Person('asd', 999))

'''
    It requires Programmer Discipline to maintain Setters, 
    but in typed Languages the Type System takes this Responsibility.
    
    Python Community treats the _var to be accessed only within the class
    __var -> private , can't be accessed directly
    _var  -> convention of using internal variables
'''
p._age = 9999
print(p.__dict__)