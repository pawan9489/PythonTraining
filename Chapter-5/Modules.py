# Function
def greeting(name):
    print("Hello,", name)

# Data
persons = [
    {
        'name': 'John',
        'age': 40
    },
    {
        'name': 'Mary',
        'age': 35
    }
]

# Class
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def __str__(self):
        return "Person(Name-'{0}',Age-{1})".format(self.name, self.age)

if __name__ == '__main__':
    p = Person('Kate', 47)
    print(p)
