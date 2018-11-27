# Generator - A Function with a Yield statement

"""
    Normal Function
        Return output using "return" Statement
        Once value is returned the Function is Finished
        Receive input through Function Argument

    Generators (are also Functions but) 
        Return output using "yield" Statement
        They can yield multiple values
        Receive input with each yield

    Generator is One type of Iterator
    # C# Yield Return

"""
# One Directional Generation
def my_generator():
    print('Yielding a')
    yield 'a'
    print('Yielding b')
    yield 'b'
    print('Yielding c')
    yield 'c'

for char in my_generator():
    print(char)

print()
# Dont use Membership Operator when using generators
# Because Lazy Evaluation - Whole purpose of Generators
print('d' in my_generator())

print()
# Genertor is after all an Iterator
g = my_generator() # Same as Iterator Object
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # StopIteration Error

# Bi Directional - Co Routines

import random as r

sentences = [
    'Hi, How are you?',
    'Fine, thank you!',
    'Nothing much',
    "Let's Party"
]

def random_conversations():

    receive = yield 'Hi'
    while receive != 'Bye!':
        receive = yield r.choice(sentences)
    # Don't have to explicitly throw StopIteration, End of function will automatically throw

g = random_conversations()
# To get first Item or To start a Geneartor, we need to send "None"
print(g.send(None))
while True:
    try:
        reply = g.send(input())
    except StopIteration:
        break
    print('>> ', reply)

print('Conversation Over!!')
