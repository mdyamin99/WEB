class Animal:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        print('Animal make some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('gheu gheu')

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('beh beh beh')

    
don = Cat('real don')
don.make_sound()

shepard = Dog('Local Shepard')
shepard.make_sound()

neymar = Goat('J R')
neymar.make_sound()

less = Goat('Gora gori')
less.make_sound()


animals = [don,shepard,neymar,less]
for animal in animals:
    animal.make_sound()