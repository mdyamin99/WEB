# encaptulation --> hide details
# access modifier --> public, protected, private

class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name = holder_name   # public attribute
        self._brance = 'banani 11'     # protected attribute
        self.__balance = initial_deposit  # private attribute

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    

rafsun = Bank('Choooto bro', 10000)
rafsun.deposit(40000)
print(rafsun.get_balance())
# print(rafsun._brance)
# print(dir(rafsun))
# print(rafsun._Bank__balance)