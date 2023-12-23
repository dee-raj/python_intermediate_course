def add_3(x):
   x += 3
num=7
add_3(num)
print(num) #7

"""Note 
   - this is still printing 7 because even we pass num as argument to add_3 and 
   - it created x as new local variable and change it by +3
   - and it it noting to do with global variable num
   - because num:int 7 is not mutable
   - so we can't change it by parsing

   - This is possible in case of mutable objects like list, dict ...
   - but immutable obj within the mutable objects can be changed (see below codes)

"""


#for list
def append_10(arr:list):
   arr.append(10)
   arr[3] = 90

my_list = [0, 2, 4, 6, 8]
print("list before func call: ", my_list)
append_10(my_list)
print("list after func call: ", my_list)


#for dict
def one_11(para:dict):
   para['ones'] = [1,1]
   para['zero'] = 0.001

my_dict = {'zero':0}
print("\nmy_dict after func call: ", my_dict)
one_11(my_dict)
print("my_dict after func call: ", my_dict)




