class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.new_grades) // len(self.new_grades)

    def average_marks(self):
        return sum(self.marks) // len(self.marks)

    # using decorators: this is through the annotation: @property - the only argument accepted is 'self'
    @property
    def average_mmarks(self):
        return sum(self.marks) // len(self.marks)

# example on inheritance
class Working_Student(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) # this is initializing the parent class: Student
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.50

rolf = Working_Student('Rolf', 'MIT', 15.50)
print(rolf.salary, "Get Salary of Working_Student")
print(rolf.name, "Get Name of Working_Student")
print(rolf.school, "Get School of Working_Student")

rolf.marks.append(65)
rolf.marks.append(85)
rolf.marks.append(71)
rolf.marks.append(70)

print(rolf.marks, "Get marks of Working_Student")
aastudent = Student("Olek", "Wandiya High School")
aastudent.marks.append(65)
aastudent.marks.append(85)
aastudent.marks.append(71)
aastudent.marks.append(70)
print(aastudent.average_mmarks, "Get average marks of through the property annotation")