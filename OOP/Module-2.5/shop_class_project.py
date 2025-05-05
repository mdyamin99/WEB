class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def call(self):
        return {'Product Name': self.name, 'Price': self.price, 'Quantity': self.quantity}

class Shop: 
    cart = []
    def __init__(self,name):
        self.name = name
        self.total_bill=0

    def add_product(self,name,price,quantity):
        product = Product(name,price,quantity)
        self.cart.append(product.call())

    def buy_product(self,name,quantity):
        flag = False
        for item in self.cart:
            if item['Product Name']==name and item['Quantity']>=quantity:
                if quantity < 1:
                    print(f'Congress. You bought {quantity} gm of {name}')
                    self.total_bill += ((item['Price']/100)*quantity)
                else:
                    print(f'Congress. You bought {quantity} kg of {name}')
                    self.total_bill += item['Price']*quantity
                print(f'Total bill: {self.total_bill}')
                item['Quantity']-=quantity
                if item['Quantity'] < 1:
                    self.cart.remove(item)
                flag = True
        if flag==False:
            print(name, 'is not available')

Jamuna = Shop('Jamuna Future Park')
Jamuna.add_product('alu',20,10)
Jamuna.add_product('potol',30,15)
Jamuna.add_product('begun',20,18)

yamin = Shop('Yamin')
yamin.buy_product('alu',0.6)
yamin.buy_product('sdj',10)
yamin.buy_product('begun',10)

amin = Shop('Amin')
amin.buy_product('alu',5)
amin.buy_product('begun',2)
