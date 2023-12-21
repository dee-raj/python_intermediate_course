def start_end(func):
   def wrapper():
      print("Starting...")
      func()
      print("Ending...")
   return wrapper

def print_sum():
   print('Sum of {} & {}: {}'.format(22, 33, 55))

summing = start_end(print_sum)  # this line is reduced by decorator
summing()
