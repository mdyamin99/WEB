class Engine:
    def __init__(self):
        pass

    def start(self):
        print('Engine started')

class Driver:
    def __init__(self):
        pass

class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()

Bus = Car()
Bus.start()