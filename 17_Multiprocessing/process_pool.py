from multiprocessing import Pool

def check_even_odd(number:int):
   if number % 2 == 0:
      return f'{number} is even'
   else:
      return f'{number} is odd'

if __name__ == "__main__":
   numbers = [x for x in range(11)]
   pool = Pool()
   '''Returns a process pool object'''

   #map
   result = pool.map(check_even_odd, numbers)
   pool.close()
   pool.join()
   print(result)

   # apply
   # print(numbers, numbers[4])
   # one_num = pool.apply(check_even_odd, numbers[5])
   # pool.close()
   # pool.join()
   # print(one_num)


