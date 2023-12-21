# Lists: ordered, mutable, allows duplicate elements, allows different data types

myList = [['Banana',232], 'cherry', b'apple']
print(myList)


item = myList[0] # firt item of list
last_item = item[-1]
print("last item",last_item)

#list with same elements
ones = [1] * 5 # here 5 is number of items in it
print(ones)

# adding lists
new_list = myList + ones # + does same work as append but with list only
print("new added list:", new_list)


