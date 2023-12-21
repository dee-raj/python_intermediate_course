from timeit import default_timer as timer
my_list = ['hey'] * 4 # make it large 
print("original: ", my_list)

# slow
start_time = timer()
my_str = ''
for item in my_list:
   my_str += item + " "
print(my_str)
stop_time = timer()
print(f"Time diff: {stop_time - start_time}")

# fast
start = timer()
my_sting = " ".join(my_list)
print('\n',my_sting)
stop = timer()
print(f"Time diff: {stop - start}")

