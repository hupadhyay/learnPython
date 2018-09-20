import abc
from abc import ABC

class IMath(ABC):
    @abc.abstractmethod
    def addition(self, num1, num2):
        pass

    @abc.abstractmethod
    def substraction(self, num1, num2):
        pass
    
    @abc.abstractmethod
    def multiplication(self, num1, num2):
        pass

    @abc.abstractmethod
    def division(self, num1, num2):
        pass

class MathProxy(IMath):
    def __init__(self, math):
        self.math = math

    def addition(self, num1, num2):
        print("Inside proxy: Calling the actual method")
        return self.math.addition(num1, num2)

    def substraction(self, num1, num2):
        print("Inside proxy: Calling the actual method")
        return self.math.substraction(num1, num2)

    def multiplication(self, num1, num2):
        print("Inside proxy: Calling the actual method")
        return self.math.multiplication(num1, num2)

    def division(self, num1, num2):
        print("Inside proxy: Calling the actual method")
        return self.math.division(num1, num2)

class MathImpl(IMath):
 
    def addition(self, num1, num2):
        return num1 + num2

    def substraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2

class MathRemote(IMath):

    def addition(self, num1, num2):
        print("Inside remote proxy: for addition")
        return num1 + num2

    def substraction(self, num1, num2):
        print("Inside remote proxy: for substraction")
        return num1 - num2

    def multiplication(self, num1, num2):
        print("Inside remote proxy: for substraction")
        return num1 * num2

    def division(self, num1, num2):
        print("Inside remote proxy: for division")
        return num1 / num2

def main():
    mathProxy1 = MathProxy(MathImpl())
    print(f'Arithmethic Operation of 9 and 5 is: Addition={mathProxy1.addition(9,5)},' + 
    f'Substraction={mathProxy1.substraction(9,5)}, Multiplication={mathProxy1.multiplication(9, 5)} and' +
    f'Division is {mathProxy1.division(9,5)}')

    print('-----------------------------------------------------')

    mathProxy1 = MathProxy(MathRemote())
    print(f'Arithmethic Operation of 9 and 5 is: Addition={mathProxy1.addition(9,5)},' + 
    f'Substraction={mathProxy1.substraction(9,5)}, Multiplication={mathProxy1.multiplication(9, 5)} and' +
    f'Division is {mathProxy1.division(9,5)}')

if __name__ == '__main__':
    main()