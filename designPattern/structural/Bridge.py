import abc
from abc import ABC

class ColorBox(ABC):
    @abc.abstractmethod
    def pickColor(self):
        pass
    
    @abc.abstractmethod
    def doColor(self):
        pass


class Natraj(ColorBox):
    
    def pickColor(self):
        print('Picking of Natraj Colors.') 
    
    def doColor(self):
        print('Coloring with Natraj Colors.')

  
class Camline(ColorBox):
    
    def pickColor(self):
        print('Picking of Camline Colors.') 
    
    def doColor(self):
        print('Coloring with Camline Colors.')


class Shape(ABC):

    @abc.abstractmethod
    def makeShape(self):
        pass
    
    @abc.abstractmethod
    def colorShape(self):
        pass


class Rectangle(Shape):

    def __init__(self, clrBox):
        self.colorBox = clrBox

    def makeShape(self):
        print('Drawing rectangle')
        
    def colorShape(self):
        self.colorBox.pickColor()
        self.colorBox.doColor()
    


class Circle(Shape):

    def __init__(self, clrBox):
        self.colorBox = clrBox

    def makeShape(self):
        print('Drawing Circle')
    
    def colorShape(self):
        self.colorBox.pickColor()
        self.colorBox.doColor()

def main():
    natraj = Natraj()
    circle = Circle(natraj)
    circle.makeShape()
    circle.colorShape()

    camline = Camline()
    rectangle = Rectangle(camline)
    rectangle.makeShape()
    rectangle.colorShape()


if __name__ == '__main__':
    main()
    
