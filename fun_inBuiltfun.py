#Declare function for sum of two numbers
def sum(firstNum, secNum):
    return firstNum + secNum;

#Declare function for multiply of two numbers
def multiply(firstNum, secondNum):
    return firstNum * secondNum

print(sum(34,36))

print(multiply(12, 15))

# using of in built function abs(number).
print(abs(-45))
print(abs(12))

# using of in built function bool(number).
print(bool(0))
print(bool(None))
print(bool(1))
print(bool(45))

#using of dir(<data_type>) functions
string = "Himanshu"
strMethods = dir(string)
print(strMethods)

mylist = ["potato", "tomato", "onion"]
strList = dir(mylist)
print(strList)

#Using of help(<functionName>) fnction
helpUpper = help(list)
print(helpUpper)

#Conversion
#convert from string to integer
print(int('45'))
#convert from string to float
print(float('36.45'))
#convert from integer to string
print(str(12345))
#convert from float to string
print(str(345.56))

#Use of len(), min() and max()

print("Lenght of "+ string + " is: " + str(len(string)))
print("Min value of "+ string + " is: " + str(min(string)))
print("Max value of "+ string + " is: " + str(max(string)))

mylist = [23, 45, 12, 9, 81, 36]
print("Lenght of list is: " + str(len(mylist)))
print("Min value of list is: " + str(min(mylist)))
print("Max value of list is: " + str(max(mylist)))
