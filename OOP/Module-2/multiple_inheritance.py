class Family:
    def __init__(self,address):
        self.address = address


class School:
    def __init__(self,id,level):
        self.id = id
        self.level = level


class Sports:
    def __init__(self,game):
        self.game = game


class Student(Family, School, Sports):
    def __init__(self, address,id,level,game):
        Family.__init__(self,address)
        School.__init__(self,id,level)
        Sports.__init__(self,game)

    def __repr__(self):
        return f'{self.address} {self.id} {self.level} {self.game}'

student = Student('Rajbari',10,12,'Fire')
print(student)

