'''
Collections :
   This module implements specialized container datatypes providing alternatives to Python's 
   general purpose built-in containers, dict, list, set, and tuple.
'''
from collections import Counter
'''
Counter:
   Dict subclass for counting hashable items. Sometimes called a bag or multiset. 
   Elements are stored as dictionary keys and their counts are stored as dictionary values.
'''

string = "she sells see shells on the sea shore"
my_counter = Counter(string)
print("Counter: ", my_counter)

# like normal dict
print("\nCounter items: \t", my_counter.items())
print("Counter keys: \t", my_counter.keys())
print("Counter values: ", my_counter.values())

commom4 = my_counter.most_common(4)
'List the n most common elements and their counts from the most common to the least. If n is None, then list all element counts.'
print("most common 4 items: ",commom4)

most_common_tuple = my_counter.most_common(1)[0]
print("This is the most common element: ", most_common_tuple)

most_common_element = my_counter.most_common(1)[0][0]
print("This is the most common element: ", most_common_element)

list_elements = list(my_counter.elements())
print("list of elements: ",list_elements)

unique = sorted(my_counter)
print("unique elements of my_counter in sorted order as a list: ",unique)

total_elements = sum(my_counter.values())
print("total elements: ",total_elements)


# ===================XXXXXXXXXXXXXXXXXX++++++++++++++++++++++XXXXXXXXXXXXXX====================++++++++++++++============XXXXXXXXXXXX+=======
new_Count = Counter('aabcdbabbddacf')
print("\nNew Counter: ",new_Count)

for char in 'account':
   new_Count[char] += 1
print("adding: ",new_Count)

del new_Count['f']
print("delete: ", new_Count)

random_counter = Counter('aabbbssbsaaccas')
new_Count.update(random_counter)
print("updated and a=: ", new_Count['a'])

print("before clear: ",random_counter)
random_counter.clear()
'Note: If a count is set to zero or reduced to zero, it will remain in the counter until the entry is deleted or the counter is cleared:'
print("after clear: ",random_counter)

print("\nbefore reduce d by 2: ", new_Count)
new_Count['d'] -= 2
print("after reduce d by 2: ", new_Count)