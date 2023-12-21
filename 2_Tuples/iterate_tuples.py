result = tuple((["max", 24],["john", 21],["Eva", 26], ['Alice', 29]))
print(result)

for student in result:
   print(student)

   names = [name for name in student]
   # print("Name:",names[0])

   if names[1] > 28:
      print('1st',names[0])

print("length/ no. of. items:",len(result))