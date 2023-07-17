class mixin:
    def attribute(self):
        attributes = ", ".join([f"{attr}: {value}" for attr, value in self.__dict__.items()])
        return attributes


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Student(Person, mixin):
    def __init__(self, name, surname, age, University):
        super().__init__(name, surname, age)
        self.University = University


student1 = Student("alex", "mebonia", 23, "dssda University")
student2 = Student("giorgi", "basiladze", 20, "sadasd University")

print(student1.attribute())
print(student2.attribute())
