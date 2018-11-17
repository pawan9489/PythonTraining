'''
Syntax:  Indentation is MUST

Syntax 1 
    if  condition :
        Code
    elif  condition :
        Code
    else :
        Code

Syntax 2 (Short Hand IF)
    if  condition : One Line Code

Syntax 3 (Short Hand IF...ELSE)
    Statement1 if condition else Statement2 

    More Like twisted Ternary
    Condition  ?  Statement1 : Statement2

'''

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print()

if a > b: print("a is greater than b")

print()

print("A") if a > b else print("B")
