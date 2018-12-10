# Used to Create Libraries

# Normal Import
import Modules

# Renaming the Module
import Modules as M

# Importing Specific
from Modules import persons as ps

Modules.greeting('Without Aliasing')
M.greeting('With Aliasing')

print(ps)
