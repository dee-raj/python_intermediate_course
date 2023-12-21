laptop = dict(ram = "8 GB", storage="512 GB", graphics="nvidia 8gb rtx 3050", requirement=['programming', 'gaming', 'graphics'])
print(f"Original Dict: {laptop}")

print('\n\n')
for value in laptop.values():
   print(f"Value = {value}")

print('\n\n')
for key in laptop.keys():
   print(f"Key = {key}")

print('\n\n')
for key, value in laptop.items():
   print(f"Key = {key}\t Value = {value}")