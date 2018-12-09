# Inheritance is Like a tree, Extending parents Functionality
# A mixin is a class such that some method of the class uses a method which is not defined in the class.
# Mixin Class are not meant to be Instantiated
# Like an Interface ex: Compare Method for Sorting

# Create a Generic Methods Class that can be used multiple times to compare Objects
# Same as @functools.total_ordering
class ComparableMixin(object):
    """This class has methods which use `<=` and `==`,
    but this class does NOT implement those methods."""
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return self <= other and (self != other)
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return self == other or self > other

class Integer(ComparableMixin):
    def __init__(self, i):
        self.i = i
    def __le__(self, other):
        return self.i <= other.i
    def __eq__(self, other):
        return self.i == other.i

print(Integer(0) <  Integer(1)) 
print(Integer(0) != Integer(1))
print(Integer(1) >  Integer(0))
print(Integer(1) >= Integer(1))

# Pick the Functionalities by Combining different Base Classes

# Designing a Game 
class Person:
    def __init__(self, _name):
        self.name = _name

# Persons categoried based on Talent
class Farmer(Person):
    def farmFields(self):
        print('Farming the Fields')

class Scholar(Person):
    def study(self):
        print('I know everything')

class Soldier(Person):
    def sword(self):
        print('Can drew a sword')

class Magician(Person):
    def magic(self):
        print('^__^')

# Persons categoried based on Strength
class Weak(Person):
    def runAway(self):
        print('Running Away')

class Strong(Person):
    def fight(self):
        print('Can fight with any one')

# Composition over Inheritance
class King(Soldier, Strong):
    pass

class Minister(Scholar, Weak, Farmer, Magician):
    pass

k = King('John')
m = Minister('Steve')

print()
print('-- King --')
print('Name = ', k.name)
k.fight()
k.sword()

print()
print('-- Minister --')
print('Name = ', m.name)
m.farmFields()
m.study()
m.runAway()
m.magic()