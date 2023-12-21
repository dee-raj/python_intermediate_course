result = ("max", 24)
#unpack the exact no of elements
name , marks = result
print(f"Name: {name}")
print(f"Marks: {marks}")


course = ('computer', 'software', 'electronic', 'electrical', 'mechanical', 'chemestry')
#unpack with multiple items
c1, *c, c3 = course
print(f"first priority: {c1}.\t Last priority: {c3}.")
print(f"Other than edge value: {c}. \ttype:{type(c)}")