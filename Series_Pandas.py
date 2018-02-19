import pandas as pand

#Declare and define a panda.
s = pand.Series([10, "Namaste", 'P', 23.5])

#Print all series member
print(s)

#Print series value by for loop
for i in s:
    print(i)
    
#Create series with given index.
s = pand.Series([10, 'hello', 12.36], index=['a','b','c'])

#print all series with index
print(s)

#print series vlaue with index is 'b'
print(s['b'])

#Create series from map of cities
mapCity = {"del":500, "lko":300, "vns":750, "cnb":600, "pun":450, "the":900}
cities = pand.Series(mapCity)

#Print the series
print(cities)

#Print the value of perticular city
print(cities["lko"])

#Print the name of city which value is more than 500
print(cities[cities > 500])

#Print the city which value is less than 500
print(cities <500)

#set the value of 700 to the cities which value is less than 500
cities[cities<500] = 700
print(cities)

#divide all vlues of cities by 10
print(cities/10)
