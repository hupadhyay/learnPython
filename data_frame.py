import pandas as pand

data = {
        'Student':['A', 'B', 'C', 'D', 'E'],
        'Maths':[90,80,75,60,85],
        'Science':[45,55,67,57,36],
        'Game':['ludo', 'cricket', 'hockey', 'chess', 'football']
    }

df = pand.DataFrame(data, columns=['Student','Maths','Science','Game'])

print('Writing into csv file')
df.to_csv('student.csv')

print('Reading of saved CSV file')
stuCSV = pand.read_csv('student.csv')
print(stuCSV)

print(df)

print('reading of csv file')
df1 = pand.read_csv('percent.csv');
print(df1)

df1 = pand.read_csv('percent.csv', names=["Name", "Class", "%age"], header=0);
print(df1)

print('print only two column')
df2 = pand.read_csv('percent.csv', names=["Name", "Class", "%age"], header=0, usecols=[0,1]);
print(df2)
