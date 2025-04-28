def all_sum(num1,num2,*numbers):
    sum=0
    for num in numbers:
        # print(num)
        sum+=num
    return sum

total=all_sum(10,20,30,40,50,60)
print(total)