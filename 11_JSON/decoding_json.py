import json
from custom_obj import User
from encoding_json import UserEncoder

def decode_user(dict):
   if User.__name__ in dict:
      return User(name=dict['name'], age=dict['age'])
   return dict

user3 = User("Kali", 19)
user3JSON = UserEncoder().encode(user3)
print(user3JSON)

user = json.loads(user3JSON, object_hook=decode_user)
print(type(user), user.name)