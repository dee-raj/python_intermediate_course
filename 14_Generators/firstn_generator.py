import sys
def firstn(n):
   nums = []
   num = 0 
   while num < n:
      nums.append(num)
      num += 1
   return nums

# print(sum(firstn(100)))
print("Size of firstn: ",sys.getsizeof(firstn(1000)))

def firstn_generator(n):
   num = 0
   while num < n:
      yield num
      num += 1

# print(sum(firstn_generator(100)))
print("Size of firstn_generator: ",sys.getsizeof(firstn_generator(1000)))