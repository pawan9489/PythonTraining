"""
    General Idea -> Rapid Alteration (Concurrency) ~= Parallel

    Why CoRoutines?
        When dealing with Thread Concurrency
            Thread Context Switching is Costly
            Unpredictable Thread Scheduler
        
    Generator Functions can Suspend and Resume
    
    Multiple Generators can Run in Rapid Alteration. Such generators are often called CoRoutines. Hence they are called Light-Weight Threading.

    Very Efficient, Co-Operative Multi Tasking, Stable and Transparent
"""

def lazy_fibonacci():
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [ l[-1], sum(l[-2:]) ]
        yield l[-1]

def lazy_tribonacci():
    yield 0
    yield 1
    yield 1
    l = [0, 1, 1]
    while True:
        l = [ l[-2], l[-1], sum(l[-3:]) ]
        yield l[-1]

for i, (f, t) in enumerate(zip(lazy_fibonacci(), lazy_tribonacci())):
    if i == 10:
        break
    print(f, t)

# Communicating Co-Routines
import random

sentences = [
    'Hi, How are you?',
    'Fine, thank you!',
    'Nothing much',
    "Let's Party",
    'Bye!'
]

def sender():
    while True:
        yield random.choice(sentences)
    
def receiver():
    while True:
        recv = yield # There is Nothing to Give Only Receive
        print("Received - {0}".format(recv))
        if recv == 'Bye!':
            break
        print("Replied - {0}".format(random.choice(sentences)))

print('--------  Communication --------')
s = sender()
r = receiver()
r.send(None) 
# x = r.send(None)
# print("x" , x) # None 
while True:
    recv = s.send(None)
    try:
        r.send(recv)
    except StopIteration:
        break
