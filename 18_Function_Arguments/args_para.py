def check_positivity(number: int) -> str:
   'Returns x => +ve, if number is positive else x => -ve'
   return f'{number} => +ve' if number > 0.0 else f'{number} => -ve'

num = check_positivity(9)
print("The number is: ", num)

# Note here
   # '9 is args and number:int was parameter'
   # args is always given when calling a funtion
   # but parametr is defined when defining a function
