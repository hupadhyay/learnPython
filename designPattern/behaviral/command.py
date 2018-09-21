import abc
from abc import ABC

class Command(ABC):
    @abc.abstractmethod
    def execute(self):
        pass

class LunchCommand(Command):
    
    def __init__(self, lunch):
        self.lunch = lunch

    def execute(self):
        self.lunch.prepareLunch()

class DinnerCommand(Command):
    
    def __init__(self, dinner):
        self.dinner = dinner

    def execute(self):
        self.dinner.prepareDinner()

class Lunch:
    
    def prepareLunch(self):
        print('preparing lunch of various items.')

class Dinner:

    def prepareDinner(self):
        print('Preparing dinner with Indian food.')

class MealInvoker:

    def __init__(self, command):
        self.command = command

    def invokeCommand(self):
        self.command.execute()

def main():
    lunch = Lunch() #receiver
    dinner = Dinner() #receiver

    lunchCommand = LunchCommand(lunch) #command
    dinnerCommand = DinnerCommand(dinner) #command

    lunchInvoker = MealInvoker(lunchCommand)
    lunchInvoker.invokeCommand()

    dinnerInvoker = MealInvoker(dinnerCommand)
    dinnerInvoker.invokeCommand()


if __name__ == '__main__':
    main()