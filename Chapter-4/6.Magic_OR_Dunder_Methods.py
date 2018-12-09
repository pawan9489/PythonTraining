# Magic or Dunder Methods - __Method__
# Enrich your classes by providing some implementation
# Accomplishes a Contract => like Interfaces in C# or Java
#       Initialization of new objects (__init__)
#       Object representation (__repr__, __str__)
#       Enable iteration (__len__, __getitem__, __reversed__)
#       Operator overloading (comparison) (__eq__, __lt__)
#       Operator overloading (addition) (__add__)
#       Method invocation (__call__)
#       Context manager support (with statement) (__enter__, __exit__)

#   https://www.python-course.eu/python3_magic_methods.php
#   https://docs.python.org/3/reference/datamodel.html

'''
    AIM : Create a Rational Class with below Requirements
        Rational(18, 16) # 3 / 2
        Rational(13, 1) => Rational(13)
        Should not be able to Create Rational(5, 0)
        Have a ToString() with Numerator/Denominator form
        Should be able to do Arithmetic Operators on Rationals 
            r1 + r2
            r1 - r2
            r1 / r2 
            r1 * r2
        Should be able to do Comparision Operators on Rationals 
            r1 > r2
            r1 < r2
            r1 >= r2 
            r1 <= r2    
            r1 == r2
            r2 != r2
        Sort List of Rationals
'''

class Rational:
    def __init__(self, p, q):
        p, q = self.__normalize(p, q)
        self.numerator = p
        self.denominator = q
    
    @property
    def numerator(self):
        return self._numer

    @numerator.setter
    def numerator(self, value):
        if type(value) is int or type(value) is float:
            self._numer = value
        else: 
            raise TypeError("Expected only Numeric Values in the Numerator")
        
    @property
    def denominator(self):
        return self._denom

    @denominator.setter
    def denominator(self, value):
        if type(value) is int or type(value) is float:
            if value == 0:
                raise ValueError("Denominator Cannot be Zero.")
            else:
                self._denom = value
        else: 
            raise TypeError("Expected only Numeric Values in the Denominator")

    # Some may dont want to create rational Numbers as 13 / 1 but just Rational(13)
    @classmethod # Static and Public
    def create(cls, numer):
        return cls(numer, 1)
    
    @classmethod # Static and Private
    def __gcd(cls, a, b):
        return a if (b == 0) else cls.__gcd(b, a % b)

    @classmethod # Static and Private
    def __normalize(cls, p, q):
        gcd = cls.__gcd(p, q)
        return (p / gcd, q / gcd)

    def __str__(self): # Used in Print == .toString(), Pretty Print an Object
        return "Rational({0})".format(self.numerator) if self.denominator == 1 else "Rational({0} / {1})".format(self.numerator, self.denominator)

    def __repr__(self): # String Representation of an Object ex: Rational(2 / 3)
        return "Rational({0})".format(self.numerator) if self.denominator == 1 else "Rational({0} / {1})".format(self.numerator, self.denominator)
    
    # r1 + r2
    def __add__(self, r):
        if isinstance(r, Rational):
            return Rational(self.numerator * r.denominator 
                    + self.denominator * r.numerator, 
                    self.denominator * r.denominator)
        elif type(r) is int or type(r) is float:
            return Rational(self.numerator + self.denominator * r , self.denominator)
        else:     
            raise TypeError("A Rational can only be added to a Number or other Rational")

    # r1 - r2 == __sub__
    # r1 * r2 == __mul__
    # r1 / r2 == __truediv__
    # r1 // r2 == __floordiv__
    
    # r1 == r2
    def __eq__(self, r):
        if isinstance(r, Rational):
            return self.numerator == r.numerator and \
                    self.denominator == r.denominator
        elif type(r) is int or type(r) is float:
            return self.numerator == r and \
                    self.denominator == 1
        else:     
            raise TypeError("A Rational can only be Compared to a Number or other Rational")

    # r1 < r2  == __lt__ # Enables sort for List<Rational>
    def __lt__(self, r):
        if isinstance(r, Rational):
            return self.numerator * r.denominator < \
                    self.denominator * r.numerator
        elif type(r) is int or type(r) is float:
            return self.numerator < \
                    self.denominator * r
        else:     
            raise TypeError("A Rational can only be Compared to a Number or other Rational")

    # r1 <= r2 == __le__
    # r1 != r2 == __ne__
    # r1 > r2  == __gt__
    # r1 >= r2 == __ge__

r1 = Rational(7 , 9)
print("r1", r1)
print(Rational(13 , 1))

# r2 = Rational(12)
r2 = Rational.create(12)
print("r2", r2)

# Python Interactive Shell 
# python -i file_name.py
rationals = [Rational(3,4), Rational.create(2), Rational(1, 2)]
print(sorted(rationals))