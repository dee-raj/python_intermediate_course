'''
Collections :
   This module implements specialized container datatypes providing alternatives to Python's 
   general purpose built-in containers, dict, list, set, and tuple.
'''
from collections import OrderedDict
'''
OrderedDict:
   Dictionary that remembers insertion order
'''

my_ordered_dict = OrderedDict()
'It will remember the order of insertion of items in older version of python i.e before 3.6'
my_ordered_dict['laptop'] = 60
my_ordered_dict['phone'] = 32
my_ordered_dict['books'] = 5
my_ordered_dict['other'] = 6

print(my_ordered_dict)
'it works similar to normal dict'