list_original = ['java', 'python', 'C/C++', 'Js', 'php']
print("original: ",list_original)

#assigning same value, it will also modify the original one
list_copy = list_original

list_copy.append('Dart')
print("copied: ",list_copy)
print("original: ",list_original)

# with : operator
list_copy.append('kotline')
new_value = list_original[0::1]
print("new list:", new_value)


# with .copy method
copied_list = list_original.copy()
print(copied_list)

