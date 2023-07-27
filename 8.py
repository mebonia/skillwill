class GradeMixin:
    def __init__(self):
        self._grades = {}

    def add_grade(self, subject, grade):
        self._grades[subject] = grade

    def average_grade(self):
        if self._grades == {}:
            return 0
        else:
            total = sum(self._grades.values())
        return total / len(self._grades)


class Student(GradeMixin):
    def __init__(self, student_id, name):
        super().__init__()
        self._student_id = student_id
        self._name = name

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    def display_details(self):
        print(f'student ID: {self._student_id}')
        print(f'Student name {self.name}')
        print(f'Average Grade : {self.average_grade()}')


class StudentManagementSystem:
    def __init__(self):
        self._students = {}

    def add_student(self, student_id, name):
        if student_id not in self._students:
            self._students[student_id] = Student(student_id, name)
            print(f" Student '{name}' with ID '{student_id}' added successfully.")
        else:
            print('Student Id already exists. provide a unique ID')

    def show_student_details(self, student_id):
        student = self._students.get(student_id)
        if student:
            student.display_details()
        else:
            print('student not found.')

    def show_student_average_grade(self, student_id):
        student = self._students.get(student_id)
        if student:
            print(f'Student ID: {student_id}, \n Name: {student.name} \n Average Grade: {student.average_grade()}')
        else:
            print('student not found.')

    @property
    def students(self):
        return self._students


student_system = StudentManagementSystem()
student_system.add_student("12345", 'alex')
student_system.add_student("42567", "nika")
student_system.add_student("42567", "nika")

student_system.show_student_details("12345")
student_system.show_student_details("42567")

student_system.students["12345"].add_grade("Math", 100)
student_system.students["12345"].add_grade("English", 85)
student_system.students["42567"].add_grade("Math", 85)
student_system.students["42567"].add_grade("English", 80)

student_system.show_student_average_grade("12345")
student_system.show_student_average_grade("42567")
student_system.show_student_average_grade("4256sdssdasdsadasdadas7")
