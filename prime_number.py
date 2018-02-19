for i in range(1, 25):
    counter = 0
    for j in range (2, i):
        if i%j==0:
            counter = 1;
    if(counter == 0):
        print("%d is prime number"%i)
