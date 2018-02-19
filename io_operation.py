#Write operation
file = open("test.txt", "w");
file.write("Hello Python Input Output Operaiton\n")
file.writelines("this is write line function of python\n")
file.write("This is seconline using writeline function.\n")
file.close();

#Read Operation
def readFunction():
    file = open("test.txt", "r")
    line = file.readline()
    while line != '':
        print(line)
        line = file.readline()

readFunction()

#Append Operation
file = open("test.txt", "a")
file.writelines("this satement is written in append mode.")
file.close()

readFunction()

#If you open file in +w, +a or +r mode you would able to write and read both operation.
