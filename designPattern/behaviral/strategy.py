import abc
from abc import ABC

class Strategy(ABC):
    @abc.abstractmethod
    def execute(self, arg1, arg2):
        pass


class AdditionalStrategy(Strategy):

    def __init__(self):
        print('Additional Strategy Implemeted')

    def execute(self, arg1, arg2):
        print(f'perform addition operation using {arg1} and {arg2}')


class SubstractionStrategy(Strategy):

    def __init__(self):
        print('Subtraction Strategy Implemeted')

    def execute(self, arg1, arg2):
        print(f'perform subtraction operation using {arg1} and {arg2}')


class StrategyExecutor:
    
    def __init__(self, strategy = None):
        self.strategy = strategy

    def execute(self, arg1, arg2):
        if self.strategy is None:
            print('Strategy not implemented')
        else:
            self.strategy.execute(arg1, arg2)

def main():
    executor = StrategyExecutor()
    executor.execute(5,8)

    executor = StrategyExecutor(AdditionalStrategy())
    executor.execute(5,8)

    executor = StrategyExecutor(SubstractionStrategy())
    executor.execute(15,8)

if __name__ == '__main__':
    main()


        
    



