file = open('my_file.txt', 'r')
try:
   msg  = file.read()
   print(msg)
except Exception as e:
   print("Some error to write or read file.",e)

finally:
   file.close()
   print('clean up...')


# this will open and close the file & do the same work as above
with open('my_file.txt','r+') as f:
   first_line = f.readline()
   print(first_line)