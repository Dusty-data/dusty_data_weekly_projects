class School:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}

    def add_new_student(self, student_name, class_name):
        self.students.append((student_name, class_name))

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch

    def view_student_list(self):
        print("List of students enrolled in", self.name)
        for student_name, class_name in self.students:
            print("Student:", student_name, "I Class", class_name)

    def view_teacher_list(self):
        print("List of teachers working at", self.name)
        for teacher_name, branch in self.teachers.items():
            print("Teacher:", teacher_name, "I Branch:", branch)

# Example usage:
school = School("XYZ School", 1990)

# Adding students
school.add_new_student("Alice", "Grade 5")
school.add_new_student("Bob", "Grade 6")

# Adding teachers
school.add_new_teacher("Mr. Smith", "Mathematics")
school.add_new_teacher("Ms. Johnson", "Science")

# Viewing student list
school.view_student_list()

# Viewing teacher list
school.view_teacher_list()


