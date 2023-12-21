"""
Union and intersection gives new set and it will not modify the original set
"""

odd = {1, 2, 3, 5, 7}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

"""
Return the union of sets as a new set.
(i.e. all elements that are in either set.)
"""
uni_oe = odd.union(even)
print(f"Union of odd & even: {uni_oe}")

uni_op = odd.union(prime)
# Union of odd & prime
print(f"uni_op", uni_op)

uni_ep = even.union(prime)
# Union of even & prime
print(f"uni_op", uni_op)

iter_oe = odd.intersection(even)
print(f"Intersection of odd & even: {iter_oe}")

print("\n\n\n")
"""
Return the difference of two or more sets as a new set.
(i.e. all elements that are in this set but not the others.)
"""
diff = uni_ep.difference(uni_op)
print(f"uni_ep - uni_op: {diff}")

diffe = uni_op.difference(uni_ep)
print(f"uni_op - uni_ep: {diffe}")



"""
Return the symmetric difference of two sets as a new set.
(i.e. all elements that are in exactly one of the sets.)
"""
symm_diff = uni_op.symmetric_difference(uni_ep)
print("symmetric difference: ",symm_diff)

# Update a set with the union of itself and others.
even.update(prime)
print("\n\nUpdated even with prime: ", even)

# Update a set with the intersection of itself and another.
odd.intersection_update(odd)
print("intersection updated odd with prime: ", odd)


# Remove all elements of another set from this set.
print("difference_update")
odd.difference_update(even)
print(odd)
even.difference_update(odd)
print(even)

# Update a set with the symmetric difference of itself and another.
print("symmetric_difference_update")
odd.symmetric_difference_update(prime)
print(odd)
even.symmetric_difference_update(odd)
print(even)
