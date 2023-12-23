from threading import Thread, Lock, current_thread
from queue import Queue
import time


def worker_func():
   while True:
      value = q.get()
      with lock:
         print(f"in {current_thread().name} got {value}")
         time.sleep(2)
      q.task_done()

if __name__=="__main__":
   q = Queue()
   lock = Lock()
   num_threads = 10

   for i in range(num_threads):
      thread = Thread(target=worker_func)
      thread.daemon = True # all other threads should die after killing main thread
      'end the execution of while true'
      thread.start()

   for i in range(1, 10):
      q.put(i)
   q.join()

   print("End main...")
