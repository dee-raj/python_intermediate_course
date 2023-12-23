class ManagedFile:
   def __init__(self, filename) -> None:
      print('init')
      self.filename = filename

   def __enter__(self):
      print('enter')
      self.file = open(self.filename, 'w')
      return self.file

   def __exit__(self, exc_type, exc_value, exc_traceback):
      if self.file:
         self.file.close()
      if exc_type is not None:
         print('\tException')
         print('exc: ', exc_type, exc_value)
      print('exit')
      return True

with ManagedFile('notes.txt') as file:
   print('do some stuff...')
   file.write('email = knowsnobody698@gmail.com \npass = tycsrollno123 \nThe attacker are targeting king first; so save king')
   file.somemethod()

print('\ncontinuing')