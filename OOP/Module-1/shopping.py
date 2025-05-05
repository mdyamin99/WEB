class Shopping():
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self,item,price,quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove(self,item):
        for num in self.cart:
            if num['item']==item:
                self.cart.remove(num)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item['price'] * item['quantity']
        print(total)
        if total > amount:
            print(f'Please provide {total - amount} more')
        else:
            print(f'Here is your items and extra money: {amount - total}')
    
swapan = Shopping('Alan swapan')
swapan.add_to_cart('Alu',50,6)
swapan.add_to_cart('dim',12,20)
swapan.add_to_cart('rice',50,10)
swapan.remove('dim')
print(swapan.cart)

swapan.checkout(2000)