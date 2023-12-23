import copy

class Person:
   def __init__(self, name:str, age:int):
      """
      Returns information about a person provided that a name and age

      initalize the name and age of a person
      """
      self.name = name
      self.age = age

   def info(self):
      return f"{self.name} is {self.age} years old."

p1 = Person('Dee-raj', 21)

print('shallow copy:')
#shallow copy
p2 = copy.copy(p1)
p2.name = 'Ram'

print(p1.info())
print(p2.info())





class College:
   def __init__(self, teacher, student):
      self.teacher = teacher
      self.student = student

   def who(self):
      'Returns who is teacher and student'
      return f"{self.teacher.name} teach {self.student.name}."

   def get_age(self):
      'Returns name and age of a person'
      return f"\nTeacher: {self.teacher.name} is {self.teacher.age} years old.\nStudent: {self.student.name} is {self.student.age} years old."

Pt1 = Person('Krishna', 46)
st1 =Person('Radha', 23)
clz = College(Pt1, st1)

print('\n\n\nDeep Copy:')
clz_clone = copy.deepcopy(clz)
clz_clone.teacher.age = 47
clz_clone.student.age = 24

print(clz.who())
print(clz.get_age())
print(clz_clone.get_age())
