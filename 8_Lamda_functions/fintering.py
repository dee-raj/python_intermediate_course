numbers = [-8, -3, -2, 0, 1, 4, 5, 6, 7, 9]
print("my Numbers:  ", numbers)

even = filter(lambda x: x%2==0, numbers)
print("Even numbers:", list(even))

# same thing for odd but using list property
odd = [x for x in numbers if x%2!=0]
print("Odd numbers: ", odd)

