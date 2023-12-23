import copy
org_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# cpy_list = list(org_list) #method 1
# cpy_list = org_list[:] #method 2
# cpy_list = org_list.copy() #method 3
cpy_list = copy.copy(org_list)  #method 4

print("original list: ",org_list)
print("copy list: ",cpy_list)

cpy_list[2] = -90 # changing 5 to 10
print("\noriginal list: ",org_list)
print("copy list: ",cpy_list)


"""Note
   -shallow copy: one level deep, only references of nested child objects
   - deep copy: full independent copy
"""