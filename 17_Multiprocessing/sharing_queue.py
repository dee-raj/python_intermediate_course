from multiprocessing import Process, Queue

def negative(numbers, queue):
   for i in numbers:
      queue.put(f'negative of {i}: {-i}')

def cube(nums, queue):
   for i in nums:
      queue.put(f'cube of {i} is {i*i*i}')


if __name__ == "__main__":
   queue = Queue()
   num = range(1,11)

   #create process
   p1 = Process(target=negative, args=(num, queue))
   p2 = Process(target=cube, args=(num, queue))

   #start process
   p1.start()
   p2.start()

   #join process
   p1.join()
   p2.join()

   #close process
   p1.close()
   p2.close()

   #print queue value
   while not queue.empty():
      print(queue.get())
