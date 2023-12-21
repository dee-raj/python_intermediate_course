"""
itertools:
   Functional tools for creating and using iterators.
"""
from itertools import permutations
'''
permutations:
   Return successive r-length permutations of elements in the iterable.
'''

num = [1, 2, 3]
perm = permutations(num, 2)
print(tuple(perm))

greet = ['hello', 'hi', 'hey there!', 'namaste']
name = permutations(greet, 2)
print(list(name))