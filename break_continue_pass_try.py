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
except:
    print("arithmetic exception occur")