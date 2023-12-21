try:
  f = open("log.txt")
  print(f.readline())
except FileNotFoundError as not_found:
  print("File not found")
else: 
  print("This will execute when there is no error...\n Everthing is fine")
  f = open('new_log.txt','r')

