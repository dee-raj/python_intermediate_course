from threading import Lock
lock = Lock()

# for locking and unlocking
lock.acquire()
...
lock.release()


#this will both func of acquire() and release()
with lock:
   ...

