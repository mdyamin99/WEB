def full_name(first,last):
    name=f"Full name is: {first} {last}"
    return name

# name=full_name("Alu","Kodu")
name=full_name(last="kodu",first="alu")
print(name)


def famous_name(first, last, **addition):
    name = f' {first} {last}'
    # print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first='Taher', last='Ali', title="Hujur", title2="Shayokh", last2='taheri')
print(name)

def a_lot(num1,num2):
    sum=num1+num2
    mult=num1*num2
    remain=num1-num2
    return sum,mult,remain

everthing=a_lot(55,21)
print(everthing)


numbers =[22,19,19,14,33]
numbers.sort()
print(numbers)
