class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name of student is ' + self.name)
        print('Age of student is '+ str(self.age))


student = Student("Himanshu", 30)
student.display()

#Attributes

print(getattr(student,"name"))

print(hasattr(student, "grade"))

setattr(student, "grade", "10th")

print(getattr(student, "grade"))

print(hasattr(student,"grade"))