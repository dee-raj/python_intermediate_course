org = 5
cpy = org
cpy += 8
print("original: ",org)
print("modified copy: ",cpy)

"""
   int is immutable so you dont have to worry
   but in case of mutable objects you need to be careful in copying by = operator
"""
org_list = [2, 4, 5, 6]
cpy_list = org_list
print("\noriginal list: ",org_list)
print("copy list: ",cpy_list)

cpy_list[2] = -90 # changing 5 to 10
print("\noriginal list: ",org_list)
print("copy list: ",cpy_list)

"here by changing copied list it also change original one... because both have same memory location"
