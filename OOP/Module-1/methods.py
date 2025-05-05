def call():
    print('calling someone i dont know')
    return 'call done'

class Phone:
    brand = 'Apple'
    color = 'White'
    price = 25000
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self,phone,sms):
        text = f'send SMS to: {phone} and message: {sms}'
        return text
    

my_phone=Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(1724,'Missy, I missed to miss ypu')
print(result)
call()