for i in range(1, 50):
    counter = 0
    j = 2
    while (j < i):
        if (i % j == 0):
            counter = 1;
        j = j + 1;
    if (counter == 0):
        print("%d is prime number" % i)
