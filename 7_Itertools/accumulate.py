"""
itertools:
   Functional tools for creating and using iterators.
"""
from itertools import accumulate
'''
accumulate:
   Return series of accumulated sums (or other binary function results)
'''
print("without func args")
uses_hr = [7, 9, 8, 11, 6]
print("phone uses time in hour: ", uses_hr)
tot_acc = accumulate(uses_hr)
print("Accumulated totoal uses: ", list(tot_acc))


print("\nwith func args")
import operator
a=[3, 5, 9]
print("original : {}".format(a))
acc_mul = accumulate(a, func=operator.mul)
print(f"multiply and accucmulate: {list(acc_mul)}")

print()
result = [46, 88, 73, 91, 68, 57]
print("Result: ",result)
first = accumulate(result, max)
print("Max accumulate: ", list(first))