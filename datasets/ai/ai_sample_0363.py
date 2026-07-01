class Student:
 def __init__(self, name, grades):
  self.name = name
  self.grades = grades

 def calculate_grade(self):
  total = 0
  for grade in self.grades:
   total += grade

  return total / len(self.grades)

student1 = Student("John", [80,90,85,95])
print(student1.calculate_grade())
# Output: 88.75