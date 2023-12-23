from multiprocessing import Process, Value, Lock
import time

def add10(x, lock):
   for i in range(10):
      time.sleep(0.01)

      lock.acquire()
      x.value += 1
      lock.release()


if __name__ == "__main__":
   lock = Lock()
   shared_number = Value('i', 9)
   print(f"Number at beginning is: {shared_number.value}")

   p1 = Process(target=add10, args=(shared_number, lock))
   p2 = Process(target=add10, args=(shared_number, lock))

   p1.start()
   p2.start()

   p1.join()
   p2.join()
   print(f"Number at end is: {shared_number.value}")
