# from abc import ABC
from orders import Order

class User():
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self,resturant,employee):
        resturant.add_employee(employee)
        
        
    def view_employee(self,resturant):
        resturant.view_employee()

    def add_menu_item(self,resturant,item):
        resturant.menu.add_menu_item(item)

    def delete_item(self,resturant,item):
        resturant.menu.remove_item(item)

    def view_menu(self,resturant):
        resturant.menu.show_menu()

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self,resturant,):
        resturant.menu.show_menu()
    
    def add_to_cart(self,resturant,item_name,quantity):
        item = resturant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Item quantity exeeded!!')
            else:
                item.quantity = quantity
                self.cart.add_items(item)
                print('Item added')
        else:
            print('Item not found')

    def view_cart(self):
        print('****View Cart****')
        print('Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total Price: {self.cart.total_price}')

    def pay_bill(self):
        print(f'Total {self.cart.total_price} paid successfully')
        self.cart.clear()

        

# ad = Admin('Karim',12733282,'karim@gmail.com','Dhaka')
# ad.add_employee('Sagor',13423223,'s@gmail.com','Khulna',32,'Chef',12000)

# ad.view_employee()
# mn = Menu()
# mn.add_menu_item(item)
# mn.show_menu()

# mamar_res = Restaurant('Mamar Resturant')

# item = FoodItem('Pizza',12.40,20)
# item2 = FoodItem('Burger',10,30)
# admin = Admin('Rahim','rahim@gmail.com',1236728,'Dhaka')
# admin.add_menu_item(mamar_res,item)
# admin.add_menu_item(mamar_res,item2)
# customer1 = Customer('Rahim','rahim@gmail.com',12392,'Dhaka')
# customer1.view_menu(mamar_res)

# item_name = input('Enter Item Name: ')
# item_quantity = int(input('Enter Item Quantity: '))

# customer1.add_to_cart(mamar_res,item_name,item_quantity)
# customer1.view_cart()
