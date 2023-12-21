import functools

def start_end_decorator(func):
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
      print("Starting...")
      func(*args, **kwargs)
      print("Ending...")
   return wrapper

@start_end_decorator
def print_sum(a, b):
   print('Sum of {} & {}: {}'.format(a, b, a+b))

print_sum(56, 9)
print()
print("Help...\n",help(print_sum))
print("func name...\n",print_sum.__name__)