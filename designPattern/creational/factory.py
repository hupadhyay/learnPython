#Factory design pattern(Creational)

#Apple computer definition
class AppleComputer:
    def __init__(self):
        print('Apple computer is assembled')

    def __str__(self):
        return 'Apple computer has delivered'

#Dell computer definition
class DellComputer:
    def __init__(self):
        print('Dell computer is assembled')

    def __str__(self):
        return 'Dell computer has delivered'

#HP computer definition
class HPComputer:
    def __init__(self):
        print('HP computer is assembled')

    def __str__(self):
        return 'HP computer has delivered'

#Asus computer definition
class AsusComputer:
    def __init__(self):
        print('Ausu computer is assembled')

    def __str__(self):
        return 'Asus computer has delivered'

#Lenovo computer definition
class LenovoComputer:
    def __init__(self):
        print('Lenovo computer is assembled')

    def __str__(self):
        return 'Lenovo computer has delivered'


#ComputerFactory definition
class ComputerFactory:

    @staticmethod
    def getComputer(name):
        if name == "apple":
            return AppleComputer()
        elif name == "lenovo":
            return LenovoComputer()
        elif name == 'asus':
            return AsusComputer();
        elif name == 'dell':
            return DellComputer();
        elif name == 'hp':
            return HPComputer();
        else:
            return "Product Not Available"

#ComputerFactory client.
class ComputerShop:
    def __init__(self):
        print("Computer shop is ready to sell computers")

    def sellComputer(self):

        while(True):
            compuName = input("Name of company:")
            if compuName == 'quit':
                break;
            else:
                product = ComputerFactory.getComputer(compuName)
                print(product)

if __name__ == "__main__":
    computerShop = ComputerShop();
    computerShop.sellComputer();



