def add_10(x):
   return x + 10
print("addding 10 to add_10: ", add_10(10))

# one args
add10 = lambda x:  x+10
print("Sum of 30 and add10:", add10(30))

# multiple args
multiply = lambda x, y : x*y 
print("Multiple of 30 and 45: ", multiply(30, 45))


"""
lambda function tipically use when 
   a function is executed only once in your code.
   or as an argument to higher order function
   or you want to return one one line from your function
"""