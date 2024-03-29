class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return round(sum(self.grades) / len(self.grades), 2)

    def __repr__(self):
        students_as_string = ", ".join(self.students)
        grade = self.get_average_grade()
        return f"The students in {self.name}: {students_as_string}. Average grade: {grade:.2f}"
        # return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"


# Test code
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
