def foo(a, b, c) -> None:
   print(a, b, c)

#unpacking list
my_list = [1, 2, 3]
print("\nvariable agruments with list")
foo(*my_list)

#unpacking tuple
my_tuple = (3, 7, 9)
print("\nvariable agruments with tuple")
foo(*my_tuple)

# unpacking dictionary
my_dict1 = {'one':1, 'two':2, 'three':3}
print("\nvariable agruments with dict")
foo(*my_dict1)

my_dict = {'a':'First', 'b':'Second', 'c':'Third'}
print("\nkeyword agruments with dict")
foo(**my_dict)

"""Note:
   - *args = variable agruments, **kwds = keyword agruments
   - Here you have to make the no of unpacking list, tuple, dict same length as of agruments.
   - In the case of unpacking dictionary the key should be same as parameter name.
   - list and tuple values passed as variable agruments but dictionary as keyword agruments.
      - if you pass dictionary as variable agruments it will get only the keys and not values.
      - and in this case you are free to use any key because it's not mapping them
   - len of your container must match the no of parameter
"""

# # not valid unpacking list
# my_list_not = [2, 5, 9, 3]
# foo(*my_list_not)
# foo(**my_list)

# # not valid unpacking tuple
# my_tuple_not_valid = (1, 2)
# foo(*my_tuple_not_valid)
# foo(**my_tuple_not_valid)

# # not valid unpacking dictionary
# my_dict_not_valid = {'1':'one', '2':'two', '3':'three'}
# print()
# foo(**my_dict_not_valid)

