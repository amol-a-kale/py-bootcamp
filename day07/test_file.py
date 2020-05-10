class Courses:
    def __init__(self, name, duration, faculty, fees):
        self.name = name
        self.duration = duration
        self.faculty = faculty
        self.fees = fees

    def completionRate(self, complete_percent):
        print('The course is completed {} %'.format(complete_percent))

    def studentEnrolledForCourse(self, list_of_students):
        for student in list_of_students:
            print(student)


python_course = Courses('Python', 3, 'Jenny', 15000)

print(dir(python_course))

print(python_course.name)
