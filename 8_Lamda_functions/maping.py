num = [1, 2, 4, 6, 3, 5]
print(f"Number list: {num}")

x3 = map(lambda x: x*x*x, num)
print("Square list:", list(x3))

# same thing from list comprihencing
cube = [x**3 for x in num]
print("sqr list:",cube)