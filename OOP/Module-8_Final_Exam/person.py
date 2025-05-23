class Person:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Customer(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.balance = 0
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.view_item()

    def add_to_cart(self, restaurant, item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            if item.price > self.balance:
                print('\nNot enough money')
            else:
                self.cart.add_to_cart(item)
                self.balance -= item.price
                print('\nItem added')
        else:
            print('\nItem not found')

    def check_balance(self):
        print(f'\nAvailable balance : {self.balance}')

    def view_cart(self):
        print('\n---Past order list---')
        for item in self.cart.carts:
            print(f'{item.name}: ${item.price}')
        print('----------------------')

    def add_balance(self, amount):
        self.balance += amount
        print(f'\nAdded money {amount}. Current balance {self.balance}')


class Admin(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def add_item(self, restaurant, item):
        restaurant.menu.add_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

    def add_customer(self, restaurant, customer):  # customer er object asbe
        restaurant.add_customer(customer)

    def view_customer_account(self, restaurant):
        restaurant.view_customer_account()

    # customer er object asbe
    def remove_customer_account(self, restaurant, customer):
        restaurant.remove_customer_account(customer)

    def view_item(self, restaurant):
        restaurant.menu.view_item()

    def update_price(self, restaurant, item_name, update_price):
        restaurant.menu.update_price(item_name, update_price)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.customers = []  # customer er object

    def add_customer(self, customer):
        self.customers.append(customer)

    def view_customer_account(self):
        print('\nAll Customer Accounts List!!')
        for customer in self.customers:
            print(
                f'Name : {customer.name}, Email : {customer.email}, Address : {customer.address}')

    def find_customer_account(self, customer_email):
        for customer in self.customers:
            if customer.email == customer_email:
                return customer
        return None

    def remove_customer_account(self, customer_email):
        customer = self.find_customer_account(customer_email)
        if customer:
            self.customers.remove(customer)
            print(f'\n{customer.name} account removed')
        else:
            print('\nAccount not found')


class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print('\nItem added')

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('\nItem deleted')
        else:
            print('\nItem not found')

    def view_item(self):
        print('\n---Restaurant Menu---')
        for item in self.items:
            print(f'{item.name}: ${item.price}')
        print('----------------------')

    def update_price(self, item_name, update_price):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            item.price = update_price
            self.items.append(item)
            print(f'\n{item.name} prices updated')
        else:
            print('\nItem not found')


class Order:
    def __init__(self):
        self.carts = []

    def add_to_cart(self, item):
        self.carts.append(item)


# restaurant = Restaurant('Yfc')
# customer = Customer('Yamin', 'yamin', 'Dhaka')
# restaurant.add_customer(customer)
# restaurant.view_customer_account()
