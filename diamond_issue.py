class Parent1:
    def __init__(self):
        print('Parent1 class initialized')

    def myfunction(self):
        print('Parent1 class function')


class Parent2:
    def __init__(self):
        print('Parent2 class initialized')

    def myfunction(self):
        print('Parent2 class function')


class Child(Parent1, Parent2):
    def __init__(self):
        print('child class initalized')

    def myfunction(self):
        super(Child, self).myfunction();
        print('child class function')


child = Child()
child.myfunction();
