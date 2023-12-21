import json
from custom_obj import User

from json import JSONEncoder
class UserEncoder(JSONEncoder):
   def default(self, o):
      if isinstance(o, User):
         return {'name' : o.name, 'age':o.age, o.__class__.__name__:True}
      return JSONEncoder.default(self, o)

user2 = User("John", 24)
user2JSON = json.dumps(user2, cls=UserEncoder)
print(user2JSON)

user3 = User("Kali", 19)
user3JSON = UserEncoder().encode(user3)
print(user3JSON)


print(f"type: {type(user3JSON)}\t user3: {user3JSON}")
user = json.loads(user3JSON)
print(user['age'])

