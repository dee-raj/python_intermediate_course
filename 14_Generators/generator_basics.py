def my_generator():
   yield 1
   yield 2
   yield 3

obj = my_generator()
print(obj)

# value can be accessed with next()
val = next(obj)
print("value with next: ",val)

#to get values inside the obj
for i in obj:
   print("value for",i)

# val = next(obj) # StopIteration because there is no other yield statement

