square = {1:1, 3:9, 8:64, 10:100, 13:169, 15:225}
print(square)
for item in square.values():
   print("i=",item)

value = square[10] #idx is not valid, here 10 is a key
print("value of key: ", value)

#valid
tuple_key = (6, 9)
square[tuple_key] = (36, 81)
print(f"dict: {square}\n\n")

# invalid
new_key = [6,9]
square[new_key] = [36, 81] # TypeError: unhashable type: 'list'
