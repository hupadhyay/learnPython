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
    def addObservers(self, TempObserver):
        pass

    @abc.abstractmethod
    def removeObservers(self, TempObserver):
        pass

    @abc.abstractmethod
    def notifyThem(self):
        pass