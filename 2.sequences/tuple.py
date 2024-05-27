student = ("Jane Doe", 20, "CS101")
print(student) # ('Jane Doe', 20, 'CS101')

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'course'])
student = Student("John Doe", 22, "CS102")
print(student.name) # John Doe