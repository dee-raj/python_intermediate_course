'''
Collections :
   This module implements specialized container datatypes providing alternatives to Python's 
   general purpose built-in containers, dict, list, set, and tuple.
'''
from collections import defaultdict

# normal dict 
my_dict = {}
my_dict['add'] = 32
print(my_dict['add'])
# print(my_dict['ad']) #KeyError: 'ad'


# ================================XXXXXXXXXXXXXXXXXXXXXXXX==================XXXXXXXXXXXXXXXXX==========================
my_dict = defaultdict()
'it will have a default key as None and value as {}'
print(my_dict)

# default type is int
d_int = defaultdict(int)
d_int['a'] = 213
d_int['b'] = 67
for value in d_int.keys():
   print("check: ",d_int[value])

# lets try a key that not exist in our dict
check = d_int['not a key']
'checked that it will not give KeyError'
print("default value: ", check)


print()

#default type is float
dict_float = defaultdict(float)
dict_float['xy'] = 8767
print("default value for known key: ",dict_float['xy']) 
print("default value for unknown key: ",dict_float['xyz']) 