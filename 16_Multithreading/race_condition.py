from threading import Thread
import time

database_value = 0
def increase():
   global database_value

   # copy the database value locally
   local_copy = database_value

   #processing to local copy
   local_copy += 1
   time.sleep(2) # takes some time to processing

   # rewrite the updated value to database
   database_value = local_copy


if __name__ == "__main__":
   print(f"Start value: {database_value}")

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


"""wait:
   the end value should be 2 but it is printing as 1 only.
   why?
   This is race condition

   when we call time.sleep(2) the thread change and 
   database_value again set to 0

   this is because both the threads wants to modify same variable at same time
   """