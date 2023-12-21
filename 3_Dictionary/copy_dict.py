lecture = dict(fycs = ['DM','DS','linux'], sycs = ['LA','DS','OS'])
print(f"Orgi dict: {lecture}") 

table = lecture
print(f"Copy dict: {table}")

"""
But the above method also modify the original if we change in copied one.
   it is because of they have same address in memory location
"""
table['tycs'] = ['AI','PM','cyber']
print(f"\nOrgi dict after adding tycs: {lecture}") 
print(f"Copy dict after adding tycs: {table}")


# actual copy using bult in function
tt = lecture.copy()
print(f"Actual copy of dict : {tt}")

tt['time'] = [7.00, 9.50, 10.38]
print(f"\nOrgi dict after adding time: {lecture}") 
print(f"Actual copy dict after adding time: {tt}")