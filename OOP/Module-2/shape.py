from math import pi

class Shape:
    def __init__(self,name):
        self.name = name


class Rectangle(Shape):
    def __init__(self, name,length,width):
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    

class Circle(Shape):
    def __init__(self, name,redius):
        self.redius = redius
        super().__init__(name)

    def area(self):
        return pi * self.redius * self.redius
    
Britto = Circle('Britto',10)
print(Britto.area())