"""
itertools:
   Functional tools for creating and using iterators.
"""
from itertools import count, cycle, repeat
"""
Infinite iterators: 
   count(start=0, step=1) --> start, start+step, start+2*step, ...
   cycle(p) --> p0, p1, ... plast, p0, p1, ... 
   repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times
"""

# count
'Return a count object whose .__next__() method returns consecutive values.'
for i in count(23):
   print("count: ", i)


for i in count(23):
   print("count: ", i)
   if i == 24:
      break

# cycle
'Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.'
num = [-1, 0, 1]
for i in cycle(num):
   print(i)
   pass

# repeat
'''
repeat(object [,times]) -> create an iterator which returns the object for the specified number of times. 
If not specified, returns the object endlessly.
'''
for i in repeat(0):
   print(i)
   pass

#with stop args
for i in repeat(1, 7):
   print(i)