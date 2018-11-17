import sys

'''
Syntax: python fileName.py   arg1   arg2   .....
sys.argv = [fileName, arg1, arg2, .....]
'''

print(sys.argv)

file_name = sys.argv[0]
print(file_name)

# Input from User
# x = input()
# print("You have entered " + x)