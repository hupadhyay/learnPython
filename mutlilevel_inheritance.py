class Parent:
    def __init__(self):
        print("first level parent class")

    def level1Func(self):
        print("function of level one class")

class Parent2(Parent):
    def __init__(self):
        print("second level parent class")

    def level2Func(self):
        print("Function of level 2 class")

class Child(Parent2):
    def __init__(self):
        print("Child class")

    def childFunc(self):
        print("Child class function")

child = Child()
child.childFunc()
child.level2Func()
child.level1Func()