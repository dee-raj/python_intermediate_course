import functools
def calculator(func):
   @functools.wraps(func)
   def wrapper_for_calculate(*args, **kwargs):
      print("Start...")
      result = func(*args, **kwargs)
      print("End...")
      return result
   return wrapper_for_calculate

def debug(func):
   @functools.wraps(func)
   def wapping_to_debug(*args, **kwargs):
      args_repr = [repr(a) for a in args]
      kwargs_repr = [f"{k} = {v!r}" for k,v in kwargs.items()]
      signature = ", ".join(args_repr + kwargs_repr)
      print(f"Calling... {func.__name__}({signature})")

      result = func(*args, **kwargs)
      print(f"{func.__name__!r} returned {result!r}")
      return result
   return wapping_to_debug


@debug
@calculator
def calculate(a:int, b=0, op='*'):
   print(f"Your inputs: a={a}, b={b}, op: {op}")
   if op =='+':
      return a + b
   elif op =='-':
      return a - b
   elif op =='*':
      return a * b
   elif op =='/':
      if b!=0:
         return a/b
      else:
         return "Exception: / by 0"
   else:
      return f'Error to do calculation with op: {op}'


print("Plus")
calculate(4, 9, '+')

print("\nMultiply")
calculate(8, 5, '*')

print("\nDivide")
calculate(35, 3, '/')

print("\nSubtract")
calculate(64, 80, '-')


print("\nError...")
calculate(85, 0, '/')

print("\nError...")
calculate(54, 8, '6')
