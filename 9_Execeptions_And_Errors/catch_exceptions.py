# catching exception
try:
 a = a
except:
   print("Some error...")


# excepting Exception and printing message
try:
  a = 5 / 0
except Exception as e:
  print("The error is...",e)


# excepting exception by error name
num = 4 #3
try:
  assert(num % 2 == 0), 'Not a even number'
  print("success to assert")

except AssertionError as ae:
  print("Error has occured as: ", ae)


# multiple try-except-except...
try:
  a = 76 / 2
  b = a + " k"
except ZeroDivisionError as zero:
  print("/ by 0", zero)

except TypeError as typing:
  print("There is type error: ", typing)
