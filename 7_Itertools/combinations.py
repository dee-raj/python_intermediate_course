"""
itertools:
   Functional tools for creating and using iterators.
"""

# combinations with out repeatation
from itertools import combinations
''''
combinations:
   Return successive r-length combinations of elements in the iterable.
'''
origin = [-1, 0, 1]
print("origin: ", origin)
combi = combinations(origin, 2)
print("without repeatation: ", tuple(combi))


# combinations with out repeatation
from itertools import combinations_with_replacement
'''
combinations_with_replacement:
   Return successive r-length combinations of elements in the iterable allowing individual elements to have successive repeats.
'''
cobmi_wr = combinations_with_replacement(origin, 2)
print("with repeatation: ", list(cobmi_wr))
