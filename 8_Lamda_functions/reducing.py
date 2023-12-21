from functools import reduce
my_num = [3, 65, 8, -7]
sum_all = reduce(lambda x,y: x+y, my_num)
print(sum_all)