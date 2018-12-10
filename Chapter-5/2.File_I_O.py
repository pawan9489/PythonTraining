f = open('file.txt', 'r')
print ("Name of the file: ", f.name)
print ("Closed or not : ", f.closed)
print ("Opening mode : ", f.mode)
# Reading the Entire file at once
data = f.read() 
print(type(data))
print('------')
print(data)
print('------')
f.close()
print ("Closed or not : ", f.closed)

# Read line by line
print('-- Line By Line --')
f = open('file.txt', 'r')
for line in f:
    print(line.strip())
print('-- Line By Line --')
f.close()

# Syntax like using() {} in C#
# Closes the file at the end
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Writing to a File
# with open('file.txt', 'w') as f:
#     f.write('Last Line') # Overrides the Entire Text

# Appends to a File
# with open('file.txt', 'a') as f:
#     f.write("\nLast Line") # Adds this line to the End of File