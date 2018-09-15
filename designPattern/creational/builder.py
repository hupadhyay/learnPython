#Builder design pattern(Creational)

class Computer:
    def __init__(self, serialVersion):
        self.serialVersion = serialVersion;
        self.ram = None
        self.hdd = None
        self.processor = None
        self.graphics = None
        self.os = None

    def __str__(self):
        return 'Computer Details [RAM : {0}, HDD : {1}, PROCESSOR : {2}, GRAPHICS : {3}, OS: {4}]'.format(self.ram, self.hdd, self.processor, self.graphics, self.os)


class OperatingSystem:
    def __init__(self, name):
        self.name = name;

    def __str__(self):
        return 'Operating System({0})'.format(self.name)

#Builder
class ComputerBuilder:

    def __init__(self):
        print('ComputerBuilder is ready to build computer')
        self.computer = Computer('234234232');

    def configureRam(self, ram):
        self.computer.ram = ram

    def configureHdd(self, hdd):
        self.computer.hdd = hdd

    def configureProcessor(self, processor):
        self.computer.processor = processor

    def configureGraphics(self, graphics):
        self.computer.graphics = graphics

    def installOS(self, os):
        self.computer.os = os

    def getComputer(self):
        return self.computer

#Director
class HwEngineer:
    def __init__(self):
        self.computerBuilder = ComputerBuilder()

    def buildComputer(self):
        self.computerBuilder.configureRam('16GB')
        self.computerBuilder.configureHdd('500GB')
        self.computerBuilder.configureProcessor('i7-8659')
        self.computerBuilder.configureGraphics('Grphics-2gb')
        os = OperatingSystem('MacBook Pro');
        self.computerBuilder.installOS(os)
        return self.computerBuilder.getComputer();

if __name__ == "__main__":
    hwEngg = HwEngineer()
    comp = hwEngg.buildComputer();
    print(comp)
