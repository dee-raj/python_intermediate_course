def foo(a, *args, **kwds):
   print("Positional argument: ", a)

   print()
   for arg in args:
      print("Variable argument: ", arg)

   print()
   for k, v in kwds.items():
      print(f"key= {k}, value={v}")

foo(7)
foo(2, ['one', 'two'], {1:"first", 2:"second"}, new_key = 'new value', my_key='my value', k76='23')

"Note -to know more about this please check function 18_Function_Arguments"
