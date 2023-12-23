from queue import Queue

if __name__ == "__main__":
  q = Queue(5)

  q.put(1)
  q.put(2)
  q.put(3)
  q.put(4)
  'Put an item into the queue.'

  print("check is queue empty: ", q.empty())
  'Return True if the queue is empty, False otherwise (not reliable!).'
  print("check is queue full: ", q.full())

  # rear -> 4 3 2 1 --> front
  for i in range(4):
    print(q.get())

  # q.join()
  # 'Blocks until all items in the Queue have been gotten and processed.'

  print("check is queue empty: ", q.empty())

  q.task_done()
  # 'Indicate that a formerly enqueued task is complete.'

  print("end main")