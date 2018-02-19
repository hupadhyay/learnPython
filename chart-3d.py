from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as myplot
from distutils.sysconfig import project_base

figure = myplot.figure()

#define 3d chart
chart = figure.add_subplot(1,1,1, projection='3d')

#creating of test data
x,y,z = axes3d.get_test_data(0.5)

chart.plot_wireframe(x,y,z)

#define x,y and z axis
chart.set_xlabel('x-axis')
chart.set_ylabel('y-axis')
chart.set_zlabel('z-axis')

myplot.show()