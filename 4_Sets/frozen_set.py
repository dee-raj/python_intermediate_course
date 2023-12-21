"""
frozenset() -> empty frozenset object 
frozenset(iterable) -> frozenset object Build an immutable unordered collection of unique elements.
"""
my_set = frozenset([1,3,5,7])
print(my_set)

'''
what we can not do with frozen set:
   add, update, remove...
'''
# my_set.add(54) #AttributeError: 'frozenset' object has no attribute 'add'
# my_set.remove(23) #AttributeError: 'frozenset' object has no attribute 'remove'

'''
what we can do with frozen set:
   copy, union, intersection, difference...'''
your_set = my_set.copy()
print(your_set)
