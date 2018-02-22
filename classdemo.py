class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name of student is ' + self.name)
        print('Age of student is '+ str(self.age))

    #this is equivalent to toString() method of java class.
    def __str__(self):
        return "Student class is created by{}".format('himanshu')
    
    def __del__(self):
        return "this is distructor method"
    
student = Student("Himanshu", 30)
student.display()
print(student)


#Attributes

print(getattr(student,"name"))

print(hasattr(student, "grade"))

setattr(student, "grade", "10th")

print(getattr(student, "grade"))

print(hasattr(student,"grade"))