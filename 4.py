class Student:
    university = 'university'

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f'Name : {self.name}, Age: {self.age}, Grade: {self.grade}'

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, new_grade):
        self.grade += new_grade


st1 = Student('alex', 90, 17)
print(st1)
print(st1.is_passing)
st1.grade = 50
print(st1.is_passing)
st1.increase_grade(60)
print(st1.grade)
