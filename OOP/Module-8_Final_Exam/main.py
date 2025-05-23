from person import *

restaurant = Restaurant('YFC')


def admin_menu():
    name = input('\nEnter Your Name: ')
    email = input('Enter Your Email: ')
    address = input('Enter Your Address: ')
    admin = Admin(name, email, address)
    print(f'\nWelcome Admin {name}')
    while True:
        print('\n--------Admin Menu--------')
        print('1. Create Customer Account')
        print('2. Remove Customer Account')
        print('3. View All Customer')
        print('4. Manage Restaurant Menu')
        print('5. Exit')

        choice = int(input('Select an option: '))
        if choice == 1:
            name = input('\nEnter Name: ')
            email = input('Enter Email: ')
            address = input('Enter Address: ')
            customer = Customer(name, email, address)
            admin.add_customer(restaurant, customer)
            print(f'\nCustomer {name} added')
        elif choice == 2:
            email = input('\nEnter Customer Email: ')
            admin.remove_customer_account(restaurant, email)
        elif choice == 3:
            admin.view_customer_account(restaurant)
        elif choice == 4:
            while True:
                print('\n1. Add Item')
                print('2. Remove Item')
                print('3. View Item')
                print('4. Update Item Price')
                print('5. Exit')

                ch = int(input('Enter an option: '))
                if ch == 1:
                    item_name = input('\nEnter Item Name: ')
                    item_price = int(input('Enter Item Price: '))
                    food_item = FoodItem(item_name, item_price)
                    admin.add_item(restaurant, food_item)
                elif ch == 2:
                    item_name = input('\nEnter Item Name: ')
                    admin.remove_item(restaurant, item_name)
                elif ch == 3:
                    admin.view_item(restaurant)
                elif ch == 4:
                    item_name = input('\nEnter Item Name: ')
                    update_price = int(input('Enter Item Update Price: '))
                    admin.update_price(restaurant, item_name, update_price)
                elif ch == 5:
                    break
                else:
                    print('\nInvalid Input')
        elif choice == 5:
            break
        else:
            print('\nInvalid Input')


def customer_menu(customer):
    print(f"\n----{customer.name}'s Menu----")
    while True:
        print('1. View Restaurant Menu')
        print('2. View Balance')
        print('3. Add Balance')
        print('4. Place Order')
        print('5. View Past Order')
        print('6. Exit')

        choice = int(input('Select an option: '))
        if choice == 1:
            customer.view_menu(restaurant)
        elif choice == 2:
            customer.check_balance()
        elif choice == 3:
            amount = int(input('\nEnter amount: '))
            customer.add_balance(amount)
        elif choice == 4:
            item_name = input('\nEnter Item Name: ')
            customer.add_to_cart(restaurant, item_name)
        elif choice == 5:
            customer.view_cart()
        elif choice == 6:
            break
        else:
            print('\nInvalid Input')


while True:
    print('\n----Restaurant Management System----')
    print('1. Admin Login')
    print('2. Customer Login')
    print('3. Exit')

    choice = int(input('Select an option: '))
    if choice == 1:
        admin_menu()
    elif choice == 2:
        name = input('\nEnter Customer Username: ')
        flag = True
        for customer in restaurant.customers:
            if customer.name == name:
                flag = False
                cus = Customer(customer.name, customer.email, customer.address)
                customer_menu(cus)
            if flag == False:
                break
    elif choice == 3:
        break
    else:
        print('\nInvalid Input')
