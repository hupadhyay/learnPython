class Parent:
    def __init__(self):
        print("Parent class constructor")

    def myfunction(self):
        print("This function declared in the Parent class")


class Child(Parent):
    def __init__(self):
        print('Child class constructor')

    def myfunction(self):
        print('This function declared in child class')
        super(Child, self).myfunction();

child = Child()

child.myfunction()