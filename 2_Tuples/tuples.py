# Tuples: ordered, immutable, allows duplication elements

mytuple = ('math', 98, 'bsc')
print(mytuple)

#get index value
fist_item = mytuple[0]
print("at 0",fist_item)
last_item = mytuple[-1]
print("at -1", last_item)

# check immutable
# mytuple[3] = "new data" #TypeError: 'tuple' object does not support item assignment


"""
# note for one element
axy = (23)
print(type(axy), axy)

xy = (45,)
print(type(xy), xy)
"""