# Used to Create Libraries

# Normal Import
import Modules

# Renaming the Module
import Modules as M

# Importing Specific
from Modules import persons as ps
# from Modules import * # Import Everything

Modules.greeting('Without Aliasing')
M.greeting('With Aliasing')

print(ps)
print()

# Import from other Folders
import sys
print(sys.path)
sys.path.append('../Chapter-4')
import CustomIterators as ci
print(list(ci.it))
