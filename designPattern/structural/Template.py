from abc import ABC
import abc

class FoodTemplate(ABC):
    @abc.abstractmethod
    def prepare(self):
        pass
    
    @abc.abstractmethod
    def cook(self):
        pass
    
    @abc.abstractmethod
    def eat(self):
        pass

    def dinner(self):
        self.prepare()
        self.cook()
        self.eat()

class MakeTea(FoodTemplate):
    def prepare(self):
        print("pour the water sugar and milk.")
    
    def cook(self):
        print("boil the water mixture with tea leaf.")
    
    def eat(self):
        print("drink tea.")

class MakeChholeBhature(FoodTemplate):
    def prepare(self):
        print("prepare raw materials.")
    
    def cook(self):
        print("cook chhole and bhature.")
    
    def eat(self):
        print("eat chhole and bhature.")


def main():
    tea = MakeTea()
    tea.dinner()

    chhole = MakeChholeBhature()
    chhole.dinner()

if __name__ == '__main__':
    main()