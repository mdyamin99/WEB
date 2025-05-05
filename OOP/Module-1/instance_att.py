class Shop:

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []    # cart is an instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)


mehzabeen = Shop('Mehzabeen')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
print(mehzabeen.buyer)
print(mehzabeen.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)