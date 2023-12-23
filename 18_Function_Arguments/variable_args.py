def foo(a, b, *args, **kwargs):
   print(f"a={a}, b={b}")

   # args is a tuple so you have to loop through it to access
   for para in args:
      print("args: ",para)

   # kwargs is a dictionary so you will get a key-pair value
   for key in kwargs:
      print(f"kwargs: key = {key} & value = {kwargs[key]}")


#only required arguments
print("only required arguments")
foo('Python', 'Java')

# reqquired arguments with variable arguments
print("\nreqquired arguments with variable arguments")
foo(['hi', 'hello'], {1:'one', 2:'two'}, 464, -958)

# reqquired arguments with variable arguments and keyword arguments
print("\nreqquired arguments with variable arguments and keyword arguments")
foo(2, 76, 'error', [1, 2, 3], one=1, marks=89)

# skipping variable arguments
print("\nskipping variable arguments")
foo( b='new value', a=['one', 'two'], study='Bsc. Cs', grade='A+')


"""Note 
   - Positional argument cannot appear after keyword arguments
   - You can skip variable arguments and only give keyword arguments
   - You have to be careful while providing required args (refer default_args note)
"""


def example(a, *para, b, c):
   ' After a * there is always keywords agruments '
   print("\n\n\n",a, b, c)
   for p in para:
      print(p)
example(2,7,b=42,c=53)