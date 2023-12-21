laptop = dict(ram = "8 GB", storage="512 GB", graphics="nvidia 8gb rtx 3050", requirement=['programming', 'gaming', 'graphics'])
print(laptop)

if 'graphics' in laptop:
   print(f"Graphics: {laptop['graphics']}")
else:
   print("not there")

try:
   print(laptop['price'])
except:
   print("price not defined")