class Student:
    def __init__(self, name, age, education, contact, ID, course_enrolled, email=None):
        self.name = name
        self.age = age
        self.education = education
        self.contact = contact
        self.email = email
        self.ID = ID
        self.course_enrolled = course_enrolled

    def courseEnrolledFor(self):
        # John has enrolled for course
        print(self.name + " has enrolled for " + self.course_enrolled)

    def feesPaid(self, paid_fees):
        print("{} has paid {} /-".format(self.name, paid_fees))
        print("{1} has paid {0} /-".format(paid_fees, self.name))
        print("{name} has paid {fees} /-".format(name=self.name, fees=paid_fees))

    def print_obj_properties(self):
        print(self.name, self.email, self.contact)


john = Student("John", 26, "B.E", 13244, "john@gmale.com", 1, "Python")
mike = Student("Mike", 27, "B.E", 34353, 2, "Java")
jenny = Student("Jenny", 23, "B.E", 758597, 3, "JavaScript", email="jenny@gmale.com")
ramu = Student("Ramu", 26, "Ph.D", 343536, "rambo@gmale.com", 4, "Python")

print(jenny.age)