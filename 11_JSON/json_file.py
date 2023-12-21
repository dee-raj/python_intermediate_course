import json

person = {"firstName" : "dee", "lastName" : "raj", "age" : 21, "havePG" : False, "study" : ['12th', '10th', 'UG']}

personJSON = json.dumps(person, indent=3, sort_keys=True)
print(personJSON)

# with open('person.json', 'w') as f:
#    json.dump(person, f, indent=3)

p = json.loads(personJSON)
print(p)


# read from a json file
with open('person.json','r') as file:
   dee = json.load(file)
print(dee)