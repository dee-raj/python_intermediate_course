from multiprocessing import Process
import os, time

def square_numbers():
   for i in range(100):
      print()
      print(f"Square of {i} is {i*i}", end=' ')
      time.sleep(0.2)

processes = []
num_processess = os.cpu_count()
print("no of cpu in your machine: ",num_processess)

#create processes
for i in range(num_processess):
   p = Process(target=square_numbers)
   processes.append(p)

# start 
for p in processes:
   p.start()

#join 
for p in processes:
   p.join()

print("end main")