my_str = "Management"

""" 
slicing
[start_idx : end_idx : steps]
if start_idx is not given
   it will start to idx =0
if end_idx not given 
   it will go upto len(str)-1
here steps is optional args... it contine after each step...defaut step =1
"""
start_idx = my_str[4:]
print("starting: ",start_idx)

end_idx = my_str[:5]
print("ending: ",end_idx)

neg_idx = my_str[-6:-1]
print("negative: ",neg_idx)

step_idx = my_str[0:9:2]
print("Step = 2: ",step_idx)

no_idx = my_str[::]
print("no idx: ",no_idx)

reverse = my_str[::-1]
print("step = -1 to reverse:", reverse)