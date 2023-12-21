alpha = ['d', 'a', 't', 'a', ' ', 's', 'c', 'i', 'e', 'n', 'c', 'e']

#count a item in tuple
count = alpha.count('a')
print(f"No of a: {count}")

# get length
length = len(alpha)
print(f"no. of. items: {length}")

# index of element
idx = alpha.index('i')
print(f"index of i: {idx}")

# tuple to list 
new_list = list(alpha)
print(f"type:{type(new_list)}\tList: {new_list}")


# list to tuple 
new_tuple = tuple(new_list)
print(f"type:{type(new_tuple)}\tTuple: {new_tuple}")
