def person_cv(name:str, course:str, age= 13):

   cv = f"""{name} is a student of {course}.
He/she is very intelligent and have deep knowledge of {course}.
he/she is {age} years old.
"""
   if 0 <= age < 18:
      cv += f"{name} is a young child and teen."
   elif age > 18:
      cv += f"{name} is a adult."
   else:
      print("please enter a valid age")
   return cv


mycv = person_cv('Dee-raj', 'JEE', 20)
print(mycv)



""""Note:
   - you can make all agrs as default argument but
   - you can't define a Non-default argument follows default argument
   - default argument must be end of your argument
   - default argument helpful to define its type with some default value
"""
