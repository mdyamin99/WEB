numbers=[12,56,98,78,56,12,6,98]
numbers_set=set(numbers)
print(numbers_set)
numbers_set.add(55)
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)

for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print("9 exiest")
elif 98 in numbers_set:
    print("98 exiest")

