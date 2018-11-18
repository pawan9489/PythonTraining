'''
Syntax: 
    def  function_name(input_parameters) :
        Code With or Without return
'''

# Defining a function
def func():
    print('Python')

# Calling a function
func()

print()
# Passing parameters
def fun_params(lang):
    """ 
    Documentation of Function. 
  
    Parameters: 
    arg1 (string): Description of arg1 
  
    Returns: 
    string: Description of return value 
    """
    # Body of Function
    return lang + ' Language'

print(fun_params('Python'))
print('------- help(fun_params) -------')
help(fun_params)
print('------ fun_params.__doc__ ------')
print(fun_params.__doc__)

print('------- Default Arguments -------')
# Default Arguments
def printDetails(name, age = 7):
    "(string, int) => void"
    print("Name: ", name)
    print("Age: ", age)
    # return Not mandatory
printDetails("Python", 28)
printDetails("Elixir")

print('------- Keyword Arguments -------')
# Keyword Arguments -> Order of passing arguments doesn't matter
def printDetails2(name, age = 7):
    "(string, int) => void"
    print("Name: ", name)
    print("Age: ", age)
    # return Not mandatory
printDetails2(age = 28, name = "Python")
printDetails2(name = "Elixir")

print('------- Variable Length Arguments -------')
# Variable Length Arguments - Should be last parameter in function declaration
def sum(*numbers):
    "Tuple<int> => int"
    print(type(numbers))
    s = 0
    for i in numbers:
        s += i
    return s
print("sum()  = {0}".format(sum()))
print("sum(1)  = {0}".format(sum(1)))
print("sum(1,2)  = {0}".format(sum(1,2)))
print("sum(1,2,3,4,5)  = {0}".format(sum(1,2,3,4,5)))

print('------- Variable Length KeyWord Arguments -------')
# Variable Length Arguments - Should be last parameter in function declaration
def sumAmount(**persons):
    "dictionary<name, money> => int"
    print(type(persons))
    s = 0
    for name, money in persons.items():
        print("{0} contributed {1}".format(name, money))
        s += money
    return s

print("sum()  = {0}".format(sumAmount()))
print("sumAmount(Jhon = 300,Jake = 500)  = {0}".format(sumAmount(Jhon = 300,Jake = 500)))

'''
Generic Function Declaration to take any kind of Inputs
    def  func(*args, **kwargs): 
        Body of Function
'''

print('------- Pass By Reference -------')
# Pass By Reference # Same as Object passing in C# but not with ref
# All arguments in the Python are passed by reference
def modifyList(list):
    "List<int> => void"
    list[2] = 333
l = [1,2,3,4]
print("Before Updating List = {0}".format(l))
modifyList(l)
print("After Updating List = {0}".format(l))

print()
def reassign(list):
    "List<int> => void"
    list = True # Changes are Local
l = [1,2,3,4]
print("Before reassign List = {0}".format(l))
reassign(l)
print("After reassign List = {0}".format(l))
