import pandas as pand

data = {
        'Student':['A', 'B', 'C', 'D', 'E'],
        'Maths':[90,80,75,60,85],
        'Science':[45,55,67,57,36],
        'Game':['ludo', 'cricket', 'hockey', 'chess', 'football']
    }

df = pand.DataFrame(data, columns=['Student','Maths','Science','Game'])

print(df)