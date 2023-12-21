num_list = [2, 5, 75, 0, -13, -43]
print("original list: ", num_list)

new_list = sorted(num_list)
print("\ncheck original list: ", num_list)
#here you can see the orifginal list does not replaced....

print("new sorted list: ", new_list)

# sort method replace elements to make new list from the existed one
print("\ncheck original list: ", num_list)
num_list.sort()
print("after sort: ",num_list)