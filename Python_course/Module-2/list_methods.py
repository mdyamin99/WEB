numbers = [10,20,30]
numbers.append(40)
print(numbers)

numbers.insert(1,100)
print(numbers)

if 30 in numbers:
    numbers.remove(30)
print(numbers)

last=numbers.pop()
print(last,numbers)

idx=numbers.index(20)
print(idx)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)