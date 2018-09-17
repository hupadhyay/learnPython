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

class CoffeeDecorator(AbstractCoffee):

    def __init__(self):
        

    def get_cost(self):
        

    def get_ingredients(self):
        pass
   

if __name__ == '__main__':
    cc = ConcreteCoffee();
    cc.get_ingredients();
    cc.get_cost();