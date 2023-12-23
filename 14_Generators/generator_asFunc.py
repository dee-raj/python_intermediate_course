def numbers():
   yield 5
   yield 1
   yield 3
   yield 7

n = numbers()
# to sort 
print("Sorted list: ", sorted(n))

# to sum
# print("sum = ",sum(n))