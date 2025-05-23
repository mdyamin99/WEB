from person import*


shop = Shop('mamar shop')
def seller_menu(seller):
    while True:
        print('\nPress 1 for add product')
        print('Press 2 for back to Main Page')

        ch = int(input('\nEnter a Number: '))
        if ch == 2:
            break
        else:
            item_name = input('\nEnter product name: ')
            price = int(input('Enter product price: '))
            quantity = int(input('Enter product quantity: '))
            menu = Product(item_name,price,quantity)
            seller.add_product(shop,menu)


def customer_menu(customer):
    while True:
        print('\n1. View Menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. PayBill')
        print('5. Back to Main page')

        ch = int(input('\nEnter a Number: '))
        if ch == 1:
            customer.view_products(shop)
        elif ch == 2:
            item_name = input('\nEnter item name: ')
            quantity = int(input('Enter item quantity: '))
            customer.buy.add_item(shop,item_name,quantity)
        elif ch == 3:
            customer.view_cart()
        elif ch == 4:
            customer.pay_bill()
        elif ch == 5:
            break


while True:
    print('\n---------- Main Page ----------')
    print('Press 1 for sign Up as a Customer')
    print('Press 2 for sign us as a Seller')
    print('Press 3 for Login')
    choice = int(input('\nEnter a Number: '))
    if choice == 1:
        email = input('Enter Your Email: ')
        password = input('Enter Your Password: ')
        flag = True
        for customer in shop.customers:
            if customer.email == email:
                print('\nThis email address already have an customer account. Please login your account')
                flag = False
                break  
        if flag == True:
            customer = Customer(email,password)
            shop.add_customer(customer)
            customer_menu(customer)
            
    elif choice == 2:
        email = input('\nEnter Your Email: ')
        password = input('Enter Your Password: ')
        flag = True
        for seller in shop.sellers:
            if seller.email == email:
                print('\nThis email address already have an seller account. Please login your account')
                flag = False
                break
        if flag == True:
            seller = Seller(email,password)
            shop.add_seller(seller)
            seller_menu(seller)

    elif choice == 3:
        email = input('\nEnter Your Email: ')
        password = input('Enter Your Password: ')
        flag = True
        for customer in shop.customers:
            if customer.email == email and customer.password == password:
                cus = Customer(email,password)
                flag = False
                customer_menu(cus)
                break

        for seller in shop.sellers:
            if flag == False:
                break
            if seller.email == email and seller.password == password:
                sell = Seller(email,password)
                flag = False
                seller_menu(sell)
                break

        if flag == True:
            print('\nInvalid email or password. Please Sign Up a account or provide currect email and password')



