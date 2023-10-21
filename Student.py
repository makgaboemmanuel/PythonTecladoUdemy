class Student:
    def __init__(self, new_name, new_grades):
        self.new_name = new_name
        self.new_grades = new_grades

    def average(self):
        return sum(self.new_grades) // len(self.new_grades)


