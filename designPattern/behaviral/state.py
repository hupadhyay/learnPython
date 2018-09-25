import abc
from abc import ABC
import random

class Emotional(ABC):
    @abc.abstractmethod
    def expressState():
        pass

   
class Happy(Emotional):

    def __init__(self):
        print('In Happy Mood')

    def expressState(self):
        print('Got Approval! I am very happy.')

class Sad(Emotional):

    def __init__(self):
        print('In Sad Mood')

    def expressState(self):
        print('Got denial! I am sad, Please leave me alone.')

class Confuse(Emotional):

    def __init__(self):
        print('In confuse state')

    def expressState(self):
        print('Got RFE! I am confuse, What to do?')

class H1BVisa():

    def __init__(self):
        print('Submitting request for H1B visa')


    def getResponseFromUSCIS(self):
        val = random.randint(0, 3)
        if val == 0 :
            print('You case was approved')
            return 'approval'
        elif val == 1 :
            print('Our decision was hold on your case. Requested additional document')
            return 'rfe'
        else:
            return 'deny'

    def sendForApproval(self):
        response = self.getResponseFromUSCIS()
        if response == 'approval' :
            state = Happy()
            state.expressState()
        elif response == 'deny':
            state = Sad()
            state.expressState()
        else:
            state = Confuse()
            state.expressState()
            print('send requested document and wait for reply')
            self.sendForApproval()

def main():
    h1b = H1BVisa()
    h1b.sendForApproval()

if __name__ == '__main__':
    main()