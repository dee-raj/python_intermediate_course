# for argument unpacking 
def find_sum(a, b):
   print(f"The sum of {a} & {b} is: {a+b}")

# unpacking list, tuple
mylist = [9, 33] # (53, 4)
find_sum(*mylist)

# unpacking dictionary
mydict = dict(a=89, b=-65)
find_sum(**mydict)

"""Note 
   - unpacking is possible only if the no of elements matches the no of parameters to your function
   - dict key name should be same as parameter name
   - please refer 18=> unpacking_args.py
"""

# to unpack list
my_list = [2, 4, 6, 8, 10]
print("\nMy num list: ", my_list)
*one_d, last = my_list
print(f"One digit nums: {one_d}\t last: {last}")

# to unpack tuple
my_tuple = (2, 4, 6, 8, 10)
print("\nmy tuple: ", my_tuple)
first, *mid, last = my_tuple
print(f"first value: {first}\t middle value: {one_d}\t last value: {last}")
print(f'type: {type(mid)}')
