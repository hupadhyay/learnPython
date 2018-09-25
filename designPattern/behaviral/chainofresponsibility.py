import abc
from abc import ABC

class Report(ABC):

    def createHeader(self):
        pass

    def createFooter(self):
        pass

    def createBody(self):
        pass

    def addCopyRights(self):
        pass
    
class HeaderReport(Report):

    def createHeader(self):
        print('Header is created for report')

class FooterReport(HeaderReport):

    def createFooter(self):
        print('Footer is created for report')

class BodyReport(FooterReport):

    def createBody(self):
        print('Body is created for report')

class CopyRightsReport(BodyReport):

    def addCopyRights(self):
        print('copy rights is added to report')


def main():
    report = CopyRightsReport()
    report.createHeader()
    report.createFooter()
    report.createBody()
    report.addCopyRights()


if __name__ == '__main__':
    main()
    
