"""
Dictionary is key-value pair data type
   it is unordered and mutable
   it maps key to its associated values
   it only store unique key and if there a key it will overwite it
"""

myDict = {"course":"computer", "year":"first", "lan":"python"}

# add key-value to dict
myDict["expreties"] = "intermediate"
print(myDict)

#access data from dict
value = myDict["course"]
print(f"Value of course: {value}")