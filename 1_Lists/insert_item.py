#define list
mylist = [('python', 'list'), b'Data', 'items', None, 123.456]

#append items at last position of list 
mylist.append(len(mylist))
print("List after append: ", mylist)


# insert element at any position given index
mylist.insert(3,[1,4,9,16])
print("List after insert: ", mylist)

#pop item from list
myItem = mylist.pop()
print("poped item",myItem)


#remove item from list
removed_item = mylist.remove('items') # it returns None
# print('removed_item', removed_item)

print("List after pop: ", mylist)

# after clearing list
mylist.clear() # it returns None
print("List after clear: ", mylist)