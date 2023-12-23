
def foo():
   my_local_vari = my_global_vari
   print("Printing global variable: ",my_global_vari)

   # alter local variable
   my_local_vari += 10
   print("modified local variable: ",my_local_vari)

   # alter global variable
   # my_global_vari +=20
   # 'UnboundLocalError'
   # print("modified global variable: ",my_global_vari)

my_global_vari = 23
print("before func call global variable: ",my_global_vari)
foo()
print("after func call global variable: ",my_global_vari)




print("\n\n")
'remove UnboundLocalError'
def check():
   global my_global

   #local variable
   x = 10
   print("Local variable: ",x)

   #modify global variable
   my_global += x # 5 + 10 = 15
   print(f"my_global after adding {x}: {my_global}")
   my_global += x # 15 + 10 = 25

my_global = 5
print("my_global before function call: ", my_global)
check()
print("my_global after function call: ", my_global)


"""Note:
   - variables can have 2 scope of bound
      1. local => works within a block of code only
      2. global => works in entire the program
   but if you want to access a global variable in some block of code first you need to define it as global <x>
   this is because of reducing the race contions
"""
