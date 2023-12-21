"""
itertools:
   Functional tools for creating and using iterators.
"""
from itertools import groupby
'''
make an iterator that returns consecutive keys and groups from the iterable

iterable
  Elements to divide into groups according to the key function.
key
  A function for computing the group category for each element. 
  If the key function is not specified or is None, the element itself is used for grouping.
'''

my_num = [-3, -1, 0, 4, -2, 7, 8]

def is_positive(x):
   return x > 0

positive_group = groupby(my_num, key=is_positive)
print("Return True if positive")
for key, val in positive_group:
   print(key, list(val))

negative_group = groupby(my_num, key=lambda x:x<0)
print("\nReturn True if negative")
for key, val in negative_group:
   print(key, list(val))



laptop = [
   {"Brand":"HP", "price":60},
   {"Brand":"iBall", "price":60},
   {"Brand":"Dell", "price":55},
   {"Brand":"Acer", "price":67},
   {"Brand":"MSI", "price":67}
]
group_obj = groupby(laptop, key=lambda x: x['price'])
print("\nGrouping same price laptop")
for key, value in group_obj:
   print(f"price {key}k \t {list(value)}")