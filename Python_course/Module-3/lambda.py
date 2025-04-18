# def doubled(x):
#     return x*2

doubled = lambda num : num*2
square = lambda num : num*num

result = doubled(44)
print(square(9))
print(result)

numbers=[12,56,98,78,56,12,6,98]
double_nums = map(doubled,numbers)
print(numbers)
print(list(double_nums))


actors =[
    {'name': 'sabana', 'age': 65},
    {'name': 'sabnoor', 'age': 45},
    {'name': 'sabila noor', 'age': 30},
    {'name': 'srabonti', 'age': 35},
    {'name': 'shaon', 'age': 47},
]
juniors = filter(lambda actor: actor['age']<40,actors)
Fivers = filter(lambda actor : actor['age'] % 5==0,actors)
print(list(Fivers))
# print(list(juniors))