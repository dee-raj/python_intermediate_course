def starts_ends_decorator(func):
   def wrapper(*args):
      print('Starting...')
      maxi = func(*args)
      print(maxi)
      print('ending...')
   return wrapper

@starts_ends_decorator
def greater(x:int, y:int) -> int:
   print("The greater number is: ", end='')
   return x if x > y else y

greater(2, 4)
print()
greater(32, 14)
