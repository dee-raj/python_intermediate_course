from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
   f = open(filename, 'w')
   try:
      yield f
   finally:
      f.close()

with open_managed_file('context_notes.txt') as file:
   file.write('please refere generator and decorator topics to get clear knowledge of this code')
