mydict = dict(first_name = "Thomas", last_name ="shelby", age=34, city="Birmingham")
print(f"original Dict: {mydict}")

# to delete a key-value pair without returning
del mydict["age"]
print(f"After delete age: ", mydict)

# poping with returning
last_name = mydict.pop('last_name')
print(f"Poped item: {last_name}")
print(f"After pop last name: ", mydict)


# poping with popitem to returning last inserted key-pair
last_value = mydict.popitem()
print(f"Poped item: {last_value}")
print(f"After pop last value: ", mydict)

