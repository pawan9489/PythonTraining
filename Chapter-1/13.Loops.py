'''
2 Primitive Loops
    while
    for

while  condition :
    Code

for  item  in  Sequence:
    Code

'''

i = 1
while i < 6:
    print(i)
    i += 1

print()

# Ranges - range(5) => 0 to 4
# range(stop)
# range(start, stop)
# range(start, stop, step)
print("range(5) = {0}".format(range(5)))
print("range(0, 5) = {0}".format(range(0, 5)))
print("range(0, 5, 2) = {0}".format(range(0, 5, 2)))

print()
for i in range(9, 2, -2):
    print(i)

print()
for character in 'Python':
    print(character)

# Loop Control Statements
# Break, Continue
# Interesting Keyword - pass (Null Operation)
print('------- Break -------')
for character in 'Python':
    if character == 't' : break
    print(character)

print('------- Continue -------')
for character in 'Python':
    if character == 't' : continue
    print(character)

print('------- pass -------')
for character in 'Python':
    if character == 't' : pass
    print(character)

if 3 > 2: pass