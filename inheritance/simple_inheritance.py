class Parent(object):
    def __init__(self):
        print("Parent class initialized.")

    def parentFun(self):
        print("Parent class function")


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child class initialized")

    def childFun(self):
        print("Child class function")


# Create object of child

mychild = Child();

mychild.childFun();
mychild.parentFun();
