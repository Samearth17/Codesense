class Student:
 def __init__(self, name, student_id, courses):
 self.name = name
 self.student_id = student_id
 self.courses = courses

class Course:
 def __init__(self, title, course_id, credits):
 self.title = title
 self.course_id = course_id
 self.credits = credits

class Database:
 def __init__(self):
 self.students = []
 self.courses = []
 
 def add_student(self, student):
 self.students.append(student)
 
 def add_course(self, course):
 self.courses.append(course)