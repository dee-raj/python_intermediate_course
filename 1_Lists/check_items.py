mylist = [{1:'wait', 2:'wait', 1:'leave', 2:'leave'}, [1,0,1,1], 'Data', 'items', None, 123.456]

if 'data' in mylist:
   print('this is ture')
else:
   print('that is false')
   for i in mylist:
      print(i, end='\t')

# print length of the list by using len() function
print(f"\nNumber of items in the list: {len(mylist)}")
