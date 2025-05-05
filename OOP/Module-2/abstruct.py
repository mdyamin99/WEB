from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print('I Need food')

    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name):
        self.name = name
        self.catagory = 'Monkey'
        super().__init__()

    def eat(self):
        print('Hey nana, I am eating banana')

    def move(self):
        print('Hanging on the brances')

layka = Monkey('Layka')
layka.eat()