def countDown(num):
   print("Starting...")
   while num:
      yield num
      num -= 1
cd = countDown(4)

val = next(cd)
print(val)

val = next(cd)
print(val)

val = next(cd)
print(val)

val = next(cd)
print(val)
