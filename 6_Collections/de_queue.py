'''
Collections :
   This module implements specialized container datatypes providing alternatives to Python's 
   general purpose built-in containers, dict, list, set, and tuple.
'''
from collections import deque

queue =deque()
'open queue... can be inserted or deleted from both side'
#appending to right side
queue.append(1)
queue.append(3)
queue.append(5)
print(f"original queue: {queue}")

#appending to left side
queue.appendleft(9)
print(f"appended 9 from left: {queue}")

#poping from right
item = queue.pop()
print(f"poped item: {item}")
print(f"after poping from right: {queue}")


#poping from left
element = queue.popleft()
print(f"poped item: {element}")
print(f"after poping from left: {queue}")

#extending means appending more than one items from right side
queue.extend([2,4,6])
print(f"queue extended from right: {queue}")

#extending more than one items from left side
queue.extendleft([-2,-1,0])
'in this case the last element of list will be fist element of queue'
print(f"queue extended from left: {queue}")

# rotate (displace items) from right
queue.rotate(2)
print(f"rotated from right by 2: {queue}")

# rotate (displace items) from left
queue.rotate(-1)
print(f"rotated from left by 1: {queue}")

# to remove a element
queue.remove(0)
'here 0 is present in the queue if not it will give ValueError'
print(f"removed 0: {queue}")

# to clear the queue
queue.clear()
print(f"cleared queue: {queue}")
