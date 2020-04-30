# class Courses():
# 	name
# 	duration
# 	faculty
# 	fees

# completionRate()
# studentEnrolledForCourse()


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

print(python_course)

print(python_course.name)
python_course.completionRate(30)
java_course = Courses('Java', 5, 'Sam', 15000)

print(java_course.name)
java_course.completionRate(50)


# class Students()
# 	name
# 	age
# 	education
# 	contact
# 	email
# 	ID

# courseEnrolledFor()
# feesPaid()
# study()
# givenExam()


class students:
    def __init__(self, name, age, educations, contact, email, ID):
        self.name = name
        self.age = age
        self.educations = educations
        self.contact = contact
        self.email = email
        self.ID = ID

    def courseEnrolledFor(self, cource_name):
        print('Enrolled for ' + str(cource_name))

    def feesPaid(self, check_fees_paid):
        if check_fees_paid == 'paid':
            print('fees  paid')
        else:
            print('fees not paid')

    def study(self, complete_syllabus_percent):
        print('The syllabus is completed {} %'.format(complete_syllabus_percent))

    def givenExam(self, check_exam):
        if check_exam == 'yes':
            print('The exam is given')
        else:
            print('The exam is not given')


john_student = students('john', 20, 'IT enginerring', 96000000, 'john@gmail.com', 1)
print(john_student.ID)
john_student.courseEnrolledFor('Engineering')
john_student.feesPaid('paid')
john_student.study(90)
john_student.givenExam('yes')


# class Faculty():
# 	name
# 	expertise
# 	education
# 	contact
# 	email

# teachCourse()
# paid()
# completedCourse()

class Faculty:
    def __init__(self, name, expertise, education, contact, email):
        self.name = name
        self.expertise = expertise
        self.education = education
        self.contact = contact
        self.email = email

    def teachCource(self,Name_of_cource):
        print('course name is '+str(Name_of_cource))

    def check_paid(self,check_course_paid):
        if check_course_paid=='paid':
            print('the course is paid')

        else:
            print('the course is not paid')

    def completed_course(self, check_course_complete):
        if check_course_complete=='yes':
            print('the course is completed')
        else:
            print('the course is not completed')

rajguru_Faculty=Faculty('Rajguru','Data science','MTech',62000000,'rajguru@gmail.com')
print(rajguru_Faculty.expertise)
rajguru_Faculty.teachCource('Data Housing')
rajguru_Faculty.check_paid('paid')
rajguru_Faculty.completed_course('yes')

