class Parent1(object):
    def __init__(self):
        print('Parent1 class initialized')

    def funParent1(self):
        print('Parent1 class function')


class Parent2(object):
    def __init__(self):
        print('Parent2 class initialized')

    def funParent2(self):
        print('Parent2 class function')


class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        print('child class initalized')

    def funChild(self):
        print('child class function')


child = Child()
child.funChild()
child.funParent1()
child.funParent2()
