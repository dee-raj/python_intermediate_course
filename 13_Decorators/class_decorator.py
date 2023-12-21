class CountCalls:
   'Used to maintain or update states'
   def __init__(self, func):
      self.func = func
      self.num_calls = 0

   def __call__(self, *args, **kwargs):
      self.num_calls += 1
      print(f'This is executed {self.num_calls} times')
      return self.func(*args, **kwargs)

@CountCalls
def say_hi():
   print('hi..\n')

for _ in range(4):
   say_hi()