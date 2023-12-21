'''
Collections :
   This module implements specialized container datatypes providing alternatives to Python's 
   general purpose built-in containers, dict, list, set, and tuple.
'''
from collections import namedtuple

'''
namedtuple:
Returns a new subclass of tuple with named fields.
'''

point = namedtuple('Point', 'x,y')
print("my named tuple: ",point.__doc__) #docstring for the new class

pt = point(2, -5) # instantiate with positional args or keywords
print("my point: ",pt)

print(f"\nAdd: {pt[0] + pt[1]}") #indexable like a plain tuple

print(f"multiply: {pt.x * pt.y}")  # fields also accessible by name

# _replace() is like str.replace() but targets named fields
pt = pt._replace(x=9)
print("replaced x=9: ",pt)
