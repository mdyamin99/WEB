person={'name': 'Kala pakhi','address': 'Kaliapur','age': 23,'job': 'Facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language']='python'
print(person)
person['name']='Sada pakhi'
print(person)

for key,value in person.items():
    print(key,value)