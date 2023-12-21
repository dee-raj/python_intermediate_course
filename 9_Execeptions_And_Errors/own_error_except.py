class ValueToHighError(Exception):
   pass

def test_value(x=0):
   if x > 100:
      raise ValueToHighError('Value is too high')

try:
   check = test_value(103)
   print("Is too high: ", check)

except ValueToHighError as high:
   print("Error msg: ", high)
finally:
   print("clean up...")




class ValueToLowError(Exception):
   def __init__(self,message, value):
      self.msg = message
      self.value = value

def test_age(x):
   if x<0:
      raise ValueToLowError("Age can't be less than 0", x)
try:
   age = test_age(-13)
except ValueToLowError as e:
   print(f"Error msg: {e.msg} \t due to value: {e.value}")