# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class 

class Gadget:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'
    

class Laptop:
    def __init__(self,memory,ssd):
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'Learning python and practicing'
    
class Phone(Gadget):
    def __init__(self,dual_sim,brand,price,color,origin):
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)

    def phone_call(self,phone,sms):
        return f'Sending SMS to: {phone} with: {sms}'
    
    def __repr__(self)->str:
        return f'Phone: {self.dual_sim} {self.brand} {self.price}'
    

class Camera(Gadget):
    def __init__(self,pixel, brand, price, color, origin):
        self.pixel = pixel
        super().__init__(brand, price, color, origin)

    def change_lense(self):
        pass


my_phone = Phone(True,'iPhone',120000,'Silver','China')
print(my_phone)
print(my_phone.brand)
