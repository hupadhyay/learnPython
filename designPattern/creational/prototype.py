import copy


class Employee:
    def __init__(self, name, age, salary, designation):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation

    def __str__(self):
        return "Employee[name:{}, age:{}, salary:{}, designation:{}]".format(self.name, self.age, self.salary, self.designation)

class Main:
    def __init__(self):
        print('Main class intantiated')

    def makeDuplicate(self):
        emp = Employee("Ramgopal", 34, 5000.0, "SSE");

        #This will make shallow clone. to make deep clone use "deepcopy" function of copy
        emp1 = copy.copy(emp);

        print("Employee Instance: " + str(emp))
        print("Duplicate Employee Instance: "+ str(emp1))

        #This will be false as it will check memory reference.
        if emp == emp1:
            print("Both reference is not equal");

        if str(emp) == str(emp1):
            print("Both string representation is equal")



if __name__ == "__main__":
    main = Main();
    main.makeDuplicate();
