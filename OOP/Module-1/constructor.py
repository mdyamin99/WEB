class Phone:
    manufactures = 'China'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self,phone,sms):
        text = f'sending to: {phone} {sms}'
        print(text)

    
my_phone = Phone('Kala chan','Oppo',10000)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('She amar jan','iphone',120000)
print(her_phone.owner, her_phone.brand, her_phone.price)

dad_phone = Phone('Abuu', 'Nokia', 3000)
print(dad_phone.owner, dad_phone.brand, dad_phone.price)