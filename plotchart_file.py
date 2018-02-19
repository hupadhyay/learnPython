import matplotlib.pyplot as myplot

#Open a file in read mode
file = open("points.txt", "r")

#Create empty list of x and y co-ordinates
x=[]
y=[]

#Read co-ordinate from files.
coord = file.readline()

while(coord != ''):
    print(coord)
    var = coord.split(",")
    x.append(int(var[0]))
    y.append(int(var[1]))
    coord = file.readline()

print(x)
print(y)

#Plot line chart and add title and lables for x and y axis
myplot.plot(x,y)
myplot.title("Rains In January")
myplot.xlabel("Days")
myplot.ylabel("inches")

#Show GUI of plot.
myplot.show()