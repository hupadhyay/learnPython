import abc
from abc import ABC

class AbstractCoffee(ABC):

    @abc.abstractmethod
    def get_cost(self):
        pass

    @abc.abstractmethod
    def get_ingredients(self):
        pass
   
    def get_tax(self):
        return 0.1*self.get_cost()


class ConcreteCoffee(AbstractCoffee):

    def get_cost(self):
        return 5.0;

    def get_ingredients(self):
        return "cofee power, water";

class IndianCoffee(AbstractCoffee):

    def get_cost(self):
        return 9.0;

    def get_ingredients(self):
        return "spice, ginger, cordmam";


class CoffeeDecorator(AbstractCoffee):

    def __init__(self, decorator):
        self.decorator = decorator

    def get_cost(self):
        return self.decorator.get_cost()

    def get_ingredients(self):
        return self.decorator.get_ingredients()


class SugarCoffeeDecorator(CoffeeDecorator):

    def __init__(self, decorator):
        self.decorator = decorator

    def get_cost(self):
        return self.decorator.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorator.get_ingredients() + ", suger"
   

class MilkCoffeeDecorator(CoffeeDecorator):

    def __init__(self, decorator):
        self.decorator = decorator

    def get_cost(self):
        return self.decorator.get_cost() + 0.50

    def get_ingredients(self):
        return self.decorator.get_ingredients() + ", milk"
   


if __name__ == '__main__':
    mcd = MilkCoffeeDecorator(SugarCoffeeDecorator(ConcreteCoffee()))

    spCoffee = mcd.get_cost() * mcd.get_tax()
    print(f'The cost of coffee is : ' + str(spCoffee))
    print('The ingredients of coffee is : ' + mcd.get_ingredients())

    indCoffee = MilkCoffeeDecorator(SugarCoffeeDecorator(IndianCoffee()))

    spCoffee = indCoffee.get_cost() * indCoffee.get_tax()
    print(f'The cost of coffee is : ' + str(spCoffee))
    print('The ingredients of coffee is : ' + indCoffee.get_ingredients())