"""
import functools
def my_decorator(func):
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
      # do... before
      result = func(*args, **kwargs)
      # do... after
      return result
   return wrapper

@my_decorator
def do_something():
   'Syntax fo a decorator'
   pass
do_something()
"""

def start_end_decorator(func):
   def wrapper():
      print("Starting...")
      func()
      print("Ending...")
   return wrapper

@start_end_decorator
def print_sum():
   print('Sum of {} & {}: {}'.format(22, 33, 55))

print_sum()
'a decorator is a function which takes another function as args & extend the behavior of this function without explicitly modifing it.'
