# Break example

for i in range (1, 25):
    if i > 5:
        break
    print('value of i is: %d'% i)

# pass example
for i in "hello himanshu":
    if i == ' ':
        break
    else:
        pass
    print(i)

# continue example
for i in "hello himanshu upadhyay, how are you":
    if i == 'u':
        continue
    print(i)

# try and except example
try:
    count = 10
    count = count/0
except ZeroDivisionError:
    print("arithmetic exception occur")
except:
    print("exception occurs")
finally:
    print('finally block executed')
    
    
from fun_inBuiltfun import sum

print(sum(3,5))

from math import sqrt

def myfunc(num):
    return num*num

values = [1,4,9, 16, 25, 36]

new_vals = map(sqrt, values)

for item in new_vals:
    print(item)
    
#Using of lambda expression
new_vals = map(lambda T: T*T,values)
for item in new_vals:
    print(item)
    
list1 = [3,6,9]
list2 = [7,3,9]

new_vals = map(lambda x,y: x+y, list1,list2)
for item in new_vals:
    print(item)

    