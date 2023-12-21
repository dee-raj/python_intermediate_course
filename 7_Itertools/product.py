"""
itertools:
   Functional tools for creating and using iterators.
"""

from itertools import product
"""
product: 
   Cartesian product of input iterables. Equivalent to nested for-loops.
"""

odd_num = [1, 3, 5]
even_num = [4, 6, 8]
prod = product(odd_num, even_num)
# print("Product: ", list(prod))


a =[0, 1]
b = ['hi']
h = product(a, b, repeat=2)
print(list(h))

