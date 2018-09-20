#Facade class
class Car:
    def __init__(self):
        self.engine = Engine()
        self.music = Music()
        self.ac = AC()
        self.oil = Petrol()

    def start(self):
        self.engine.start()
        self.music.powerOn()
        self.ac.powerOn()
        self.oil.startConsumption()

    def stop(self):
        self.engine.stop()
        self.music.powerOff()
        self.ac.powerOff()
        self.oil.stopConsumption()

    def run(self):
        self.engine.run()
        self.music.play()
        self.ac.run()
        self.ac.setTemperature()
        self.oil.consumpting()

class Engine:
    def start(self):
        print("engine has been started")

    def run(self):
        print('Engine is running.')

    def stop(self):
        print("Engine has been stoped")

class Music:
    def powerOn(self):
        print('Music system is start palying')

    def play(self):
        print('Music system is playing')

    def powerOff(self):
        print('Music system is stop playing')
    

class AC:
    def powerOn(self):
        print('AC is ON')

    def run(self):
        print('AC is running')

    def setTemperature(self):
        print('change the temperature of AC')

    def powerOff(self):
        print('AC is Off')

class Petrol:
    def startConsumption(self):
        print('petrol cosuption is started')

    def consumpting(self):
        print('Engine is comsuming petrol')

    def stopConsumption(self):
        print('petrol cosuption is stop')


def main():
    car = Car()
    car.start()
    car.run()
    car.stop()

if __name__=='__main__':
    main()