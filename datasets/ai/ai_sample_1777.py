class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)


SE_course = Course('Software Engineering', 'Allen Jones')
SE_course.add_topic('Design Patterns')
SE_course.add_topic('Testing Strategies')
SE_course.add_topic('Project Management')

print('Course:', SE_course.course_name)
print('Instructor:', SE_course.instructor)
print('Topics:')
for topic in SE_course.topics:
    print('- ', topic)