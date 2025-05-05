class Shop:
    cart = []    # cart is an class attribute

    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)


mehzabeen = Shop('Mehzabeen')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
# print(mehzabeen.cart)

# mehzabeen.cart.clear()

nisho = Shop('Nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)