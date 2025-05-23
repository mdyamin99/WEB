class Person:
    def __init__(self,email,password):
        self.email = email
        self.password = password

class Customer(Person):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.buy = Buy()

    def view_cart(self):
        print('Name\tPrice\tQuantity')
        for item,quantity in self.buy.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total price: {self.buy.total_price()}')

    def pay_bill(self):
        print(f'Total {self.buy.total_price()} paid successfilly')
        self.buy.clear()
    
    def view_products(self,shop):
        shop.menu.view_products()


class Seller(Person):
    def __init__(self, email, password):
        super().__init__(email, password)
        
    def add_product(self,shop,item):
        shop.menu.add_product(item)


class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Shop:
    def __init__(self,name):
        self.name = name
        self.menu = Menu()
        self.customers = []
        self.sellers = []

    def add_customer(self,customer):
        self.customers.append(customer)

    def add_seller(self,seller):
        self.sellers.append(seller)


class Menu:
    def __init__(self):
        self.products = []  # product er object rakhbo

    def add_product(self,product):
        self.products.append(product)

    def view_products(self):
        print('Product Name\tPrice\tQuantity')
        for product in self.products:
            print(f'{product.name}\t{product.price}\t{product.quantity}')

    def find_product(self,name):
        for product in self.products:
            if name.lower()==product.name.lower():
                return product
        return None

class Buy:
    def __init__(self):
        self.items = {}

    def add_item(self,shop,name,quantity):
        item = shop.menu.find_product(name)
        if item:
            if item.quantity < quantity:
                print('Item quantity exeeded!!')
            else:
                item.quantity = quantity
                if item in self.items:
                    self.items[item] += quantity
                else:
                    self.items[item] = quantity
                print('Item added')
        else:
            print('Item not found')

    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())

    def clear(self):
        self.items = {}
    

# product = Product('pizza',80,30)
# seller = Seller('Yamin','100')
# customer = Customer('asd','2134')
# seller.menu.add_product(product)
# # seller.menu.view_products()
# customer.menu.view_products()
