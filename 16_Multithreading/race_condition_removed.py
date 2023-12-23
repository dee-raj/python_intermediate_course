from threading import Thread, Lock
import time

database_value = 0
def increase():
   global database_value

   #Lock the transiction
   lock.acquire()

   # copy the database value locally
   local_copy = database_value

   #processing to local copy
   local_copy += 1
   time.sleep(2) # takes some time to processing

   # rewrite the updated value to database
   database_value = local_copy

   #remove the locking
   lock.release()


if __name__ == "__main__":
   print(f"Start value: {database_value}")

   lock = Lock() #lock obj

   # create threads
   thread_one = Thread(target=increase)
   thread_two = Thread(target=increase)

   # start threads
   thread_one.start()
   thread_two.start()

   # join : wait till threads gets complitated
   thread_one.join()
   thread_two.join()

   print(f"end value: {database_value}")


"""Note:
   'with lock:
      ...
   '
   the above done the same work as:
   'lock.acquire()
   ...
   lock.release()
   '
   because it is always recomended to release the lock after acquiring it.
   and you can take it as optional by doing the fist method
"""
