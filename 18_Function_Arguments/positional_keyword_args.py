#positional args
def greatest(a:int, b:int, c:int) -> str:
   'Returns the greatest number of given three numbers'
   print("\nYour numbers: ",[a, b, c])
   if a > b and a > c:
      return f'a= {a}'
   elif b > a and b > c:
      return f'b= {b}'
   else:
      return f'c= {c}'

#positional arguments
num = greatest(15,2,7)
'here agrs are passing as they are defined ordered'
print(f"Greatest number: {num}")

#keyword arguments
great = greatest(93, b=54, a=65)
'passing args as their deifination names'
print(f"Greatest number: {great}")

"""Note:
   - you can use keyword agrs after positional args
      eg. greatest(34, c=87, b=65)
   - you can not use same agrs for both positional and keyword args
      eg. greatest(93, b=54, a=65) => TypeError
"""