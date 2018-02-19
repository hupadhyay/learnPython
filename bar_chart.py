import matplotlib.pyplot as myplot
import numpy as np

# define number of bars and gap between each bar.
pos = np.arange(6) + 0.5

# define verticle bar with values, color and align. use 'hbar' for horizontal bar
myplot.bar(pos, (4, 8, 6, 7, 6, 3), align="center", color="gray")

# define title, x and y axis label.
myplot.ylabel('Height in inches', color='red')
myplot.xlabel('Students', color='red')

#define the color of ticks for x and y axis
myplot.tick_params(axis='x', colors='blue')
myplot.tick_params(axis='y', colors='blue')

#give name of bars
myplot.xticks(pos, ['prashant', 'anurag', 'himanshu', 'neeraj', 'chetan', 'bhutani'])


myplot.show()