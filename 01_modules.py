"""
Modules are an extremely useful tool for organizing and reusing code.
Simply put, a module is a python file that contains code, variables, functions, classes
that you can include in another program.
Just like functions, Modules help make your code:
- reusable
- organized
- easier to maintain

DRY Principle - "Don't Repeat Yourself"

Examples of built in modules:
time, random, os, math......

eg. 
import math #Inculde the module
print(math.pi) #Using code from the imported module
"""
# import math
# Let's see the built in modules:
# help("modules")
# help(math)

# Import just one functon from a module
from random import randint
# Import a module with an alias
import math as m
print(m.pi)

print(randint(1,10))