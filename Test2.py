import math

class Line(object):
    
    def __init__(self, coor1, coor2):
        print('line initialized.')
        self.coor1 = coor1;
        self.coor2 = coor2;
        
    def distance(self):
        return math.sqrt(math.pow((self.coor2[0]-self.coor1[0]),2) + math.pow((self.coor2[1]-self.coor1[1]),2))
    
    def slop(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
    
    def __str__(self):
        print(f'line with coordinates {self.coor1} and {self.coor2}')
        return f'line with coordinates {self.coor1} and {self.coor2}'
        
line = Line((3,2),(8,10));
print(line)
print(f'distance of line is {line.distance():.2f}')
print(f'slop of line is {line.slop():.2f}')

class Cylinder(object):
    
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return math.pi * math.pow(self.radius,2) * self.height;
    
    def surfaceArea(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)
    
    def __str__(self):
        print(f'Cylinder with height {self.height} and radius {self.radius}.')  
        return f'Cylinder with height {self.height} and radius {self.radius}.'

cyn = Cylinder(2,3)
print(cyn)
print(f'Volume of cylinder is {cyn.volume():.2f}')  
print(f'Surface Area of cylinder is {cyn.surfaceArea():.2f}')  