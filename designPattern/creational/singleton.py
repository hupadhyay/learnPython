
class Application:
    __application = None

    def __init__(self):
        if Application.__application is not None:
            raise Exception("This class is singleton")
        else:
            Application.__application = self;

    @staticmethod
    def getInstance():
        if Application.__application is None:
            Application()

        return Application.__application;


def demo():
    print("Demonstration of demo Application!")

    # This will throw exception
    #app = Application();

    # check singleton
    app = Application.getInstance();
    app1 = Application.getInstance();

    if app == app1:
        print("Same memory reference")

    #This will again throw an exception
    #app = Application()

if __name__ == "__main__":
    demo()
