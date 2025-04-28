n=int(input())
numbers=list(map(int,input().split()))
mx=numbers.index(max(numbers))
mn=numbers.index(min(numbers))
numbers[mx],numbers[mn]=numbers[mn],numbers[mx]
print(*numbers)