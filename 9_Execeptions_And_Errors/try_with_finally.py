try:
  a= 892 / 20
  print("working?",a)
except ZeroDivisionError as e:
  print('Error...',e)
finally:
  print("I'm finally executing..")


print()
try:
  f = open('new_log.txt', 'r')

except FileExistsError as e:
  print("Error.... ", e)

except FileNotFoundError as file:
  print("Error.... ", file)

finally:
  msg = f.readline()
  'this will execute even if there is error OR not there'
  print(msg)
  f.close()
  print("closing....")

