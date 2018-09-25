import abc
from abc import ABC

class TempObserver(ABC):
    @abc.abstractmethod
    def changeTemperature(self, temp):
        pass


class WeatherReport(TempObserver):

    def changeTemperature(self, temp):
        print("Weather Report : temperature = " + str(temp))


class WeatherNews(TempObserver): 

    def changeTemperature(self, temp):
        print("Weather NEWS : temperature = " + str(temp))


class Subject(ABC):
    @abc.abstractmethod
    def addObservers(self, tempObserver):
        pass

    @abc.abstractmethod
    def removeObservers(self, tempObserver):
        pass

    @abc.abstractmethod
    def notifyThem(self):
        pass

class WorkStation(Subject):
    
    def __init__(self):
        self.listObserver = []

    def setTemperature(self, temp):
        self.temperature = temp
        self.notifyThem()

    def addObservers(self, tempObserver):
        self.listObserver.append(tempObserver)

    def removeObservers(self, tempObserver):
        self.listObserver.remove(tempObserver)

    def notifyThem(self):
        for observer in self.listObserver:
            observer.changeTemperature(self.temperature)


def main():
    workStation = WorkStation()
    #register observe
    wr = WeatherReport()
    workStation.addObservers(wr)
    wn = WeatherNews()
    workStation.addObservers(wn)

    # subject state change(event generated)
    workStation.setTemperature(5.0)

    #remove observer
    workStation.removeObservers(wr)

    # again state change
    workStation.setTemperature(9.0)


if __name__ == '__main__':
    main()