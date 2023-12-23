odd_tuple = (1, 3, 5, 7, 9)
neg_set = {-2, -4, -1,  -3}
even_list = [0, 2, 4, 6, 8, 10]

number_list = [*odd_tuple, *even_list, *neg_set]
print("Number list: ", number_list)


# to merzing dictionary
a_dict = dict(one=1, two=2, three=3)
b_dict = {'four':4, 'five':5, 'six':6, 'zero':0}

new_dict = {**a_dict, **b_dict}
print(new_dict)