
import abc
from abc import ABC

#Indian socket interface
class IndianSocketInterface(ABC):
    @abc.abstractmethod
    def voltage(self):
        pass
    
    @abc.abstractmethod
    def current(self):
        pass

    @abc.abstractmethod
    def neutral(self):
        pass

#Implementation of Indian Socket.
class Socket(IndianSocketInterface):
    
    def voltage(self):
        return 220
    
    def current(self):
        return 6.0

    def neutral(self):
        return 1


class USAPowerPlugInterface(ABC):
    @abc.abstractmethod
    def voltage_usa(self):
        pass
    
    @abc.abstractmethod
    def current_usa(self):
        pass

    @abc.abstractmethod
    def neutral_usa(self):
        pass

class Adaptor(USAPowerPlugInterface):
    def __init__(self, socket):
        self.socket = socket

    def voltage_usa(self):
        return self.socket.voltage()
    
    def current_usa(self):
        return self.socket.current()

    def neutral_usa(self):
        return self.socket.neutral()


class Client:
    def __init__(self, adaptor):
        self.adaptor = adaptor
        print('using of usa adaptor')
    
    def callMethod(self):
        print(f'Getting voltage: ' + str(self.adaptor.voltage_usa()))
        print(f'Getting current: ' + str(self.adaptor.current_usa()))
        print(f'Getting neutral: ' + str(self.adaptor.neutral_usa()))

if __name__ == '__main__':
    socket = Socket()
    adaptor = Adaptor(socket)
    client = Client(adaptor)
    client.callMethod()
