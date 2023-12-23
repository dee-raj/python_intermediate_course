from multiprocessing import Process, Array, Lock
import time

def add100(numbers, lock):
   for i in range(100):
      time.sleep(0.01)
      for num in range(len(numbers)):
         with lock:
           numbers[num] += 1


if __name__ == "__main__":
   lock = Lock()
   shared_array = Array('d', [0.1, 10.1, 20.1])
   print(f"array at beginning is: {shared_array[:]}")

   p1 = Process(target=add100, args=(shared_array, lock))
   p2 = Process(target=add100, args=(shared_array, lock))

   p1.start()
   p2.start()

   p1.join()
   p2.join()
   print(f"array at end is: {shared_array[:]}")
