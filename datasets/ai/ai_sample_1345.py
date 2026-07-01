class StudentRecord:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
 
    def get_student_records(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'course': self.course
        }
 
    def set_student_records(self, updates):
        self.student_id = updates.get('student_id', self.student_id)
        self.name = updates.get('name', self.name)
        self.age = updates.get('age', self.age)
        self.course = updates.get('course', self.course)