import sys

my_even_generator = (i for i in range(50) if i%2==0)
'generator comprihension and define with (x for x ...)'
for even_num in my_even_generator:
   print(even_num, end=' ')

print()
gen_list = list(my_even_generator)
print("generator to list: ",type(gen_list))
print("size of generator: ", sys.getsizeof(my_even_generator))
print()

#list comprihens
my_odd_list = [i for i in range(50) if i%2!=0]
'list comprihension and define with [x for x ...]'
for odd_num in my_odd_list:
   print(odd_num, end=' ')

print()
print("size of list: ", sys.getsizeof(my_odd_list))
