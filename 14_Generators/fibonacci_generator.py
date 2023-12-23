def fibonacci(limit):
   # 0, 1, 1, 2, 3, 5, 8, 13 ...
   a = 0
   b = 1
   for _ in range(limit):
      print(a, end=', ')
      c = a + b
      a = b
      b = c
print("fibonacci: ")
fibonacci(6)


def fibonacci_generator(limit):
   a, b = 0, 1
   while a < limit:
      yield a
      a, b = b, a+b

fibo_gen = fibonacci_generator(40)
print("\n\nfibonacci_generator:")
for num in fibo_gen:
   print(num, end=', ')
