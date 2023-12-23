import copy
#shallow copy
num_list = list([[1, 2, 3, 4, 5], [6, 7, 8, 9]])
copy_num = copy.copy(num_list)
copy_num[1][2] = -11
copy_num[0][2] = -22
print("\nOriginal: ", num_list)
print("shallow copy num: ", copy_num)


#deep copy
my_num_list = list([[1, 2, 3, 4, 5], [6, 7, 8, 9]])
deep_copy_num = copy.deepcopy(my_num_list)
deep_copy_num[0][3] = -44
deep_copy_num[1][3] = -33
print("\nOriginal: ", my_num_list)
print("deep copy num: ", deep_copy_num)