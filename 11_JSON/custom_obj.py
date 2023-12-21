import json
from typing import Any
class User:
   def __init__(self, name:str, age:int) -> None:
      self.name = name
      self.age = age

user1 = User("max", 32)
"the JSON object must be str, bytes or bytearray, not User"

def encode_user(obj):
   if isinstance(obj, User):
      return {'name' : obj.name, 'age':obj.age, obj.__class__.__name__:True}
   else:
      raise TypeError('Error in object type of user')

user1JSON = json.dumps(user1, default=encode_user)
print(user1JSON)
