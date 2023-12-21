# declaring an empty list
my_list = list()
#appending diff types of elements eg- byte, int, bool, float, dict...
my_list.append([b'two', 22, False, 54.23, {'key':'value', 1:'one'}])
my_list.append(793)
print(my_list)

# iteration through your list
for i in my_list:
   print("Item => ", i)
   pass

# reverse list 
my_list.reverse()
print(my_list)

my_list.pop(1) # delete list from the list to use sort... because it sorts same element types only
my_list.append(23)
my_list.append(54)

#sort list... it will change original list by replacing items to sort
my_list.sort()
print("sorted list:", my_list)

