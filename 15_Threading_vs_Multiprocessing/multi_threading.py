from threading import Thread
import os, time

def cube_numbers():
   for i in range(5):
      print()
      print(f"\ncube of {i} is {i*i*i}", end=' ')
      time.sleep(2)
threads = []
num_threads = 10

#create threads 
for i in range(num_threads):
   t = Thread(target=cube_numbers)
   threads.append(t)

# start 
for t in threads:
   t.start()

# join 
for t in threads:
   t.join()

print("\nEnd main...")