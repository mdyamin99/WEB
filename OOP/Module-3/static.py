# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method and class method

class Shopping:
    cart = []   # class attribute  # static attribute

    def __init__(self,name,location):
        self.name = name            # instance attribute
        self.location = location

    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multiply(a,b):
        result = a*b
        print(result)

    @classmethod
    def hudai_dekhi(self,item):
        print('hudai dekhi kintu kinmu na ac er hawa khaite asci',item)


bashundhara = Shopping('Bashundhara','Not popular location')
bashundhara.purchase('lungi',500,1000)

bashundhara.hudai_dekhi('lungi')
Shopping.hudai_dekhi('Lungi')

# static method
Shopping.multiply(4,6)