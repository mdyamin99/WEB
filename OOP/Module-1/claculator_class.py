class Calculator:
    brand = 'Casio MS990'

    def sum(self,num1,num2):
        return num1 + num2
    
    def deduct(self,num1,num2):
        return num1 - num2
    
    def multiply(self,num1,num2):
        return num1 * num2
    
    def divide(self,num1,num2):
        return num1 / num2
    

my_calculator = Calculator()

Sum = my_calculator.sum(10,20)
print(Sum)

Deduct = my_calculator.deduct(30,10)
print(Deduct)

Multiply = my_calculator.multiply(10,20)
print(Multiply)

Divide = my_calculator.divide(30,5)
print(Divide)