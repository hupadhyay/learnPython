import matplotlib
import matplotlib.pyplot as myplot

file = open("points.txt", "r")
x=[]
y=[]

coord = file.readline()

while(coord != ''):
    print(coord)
    var = coord.split(",")
    x.append(int(var[0]))
    y.append(int(var[1]))
    coord = file.readline()

print(x)
print(y)

myplot.plot(x,y)
myplot.title("Rains In January")
myplot.xlabel("Days")
myplot.ylabel("inches")

myplot.show()