import matplotlib.pyplot as myplot;

#define a list with values which sum must be 100.
size= [42,18,28,12]

#define labels for each value component
labels= ['bjp', 'jdu', 'rjd', 'inc']

#define color for each compoenent
colors=['red','green','yellow','pink']

myplot.pie(size, colors=colors, labels=labels)

#maek x and y axis equals.
myplot.axis('equal')

#put the legend at lower left and give title.
myplot.legend(title="legend", loc="lower left")
myplot.show()