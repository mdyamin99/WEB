numbers = [45,87,96,65,43,90,85,14,26,61,70]

odds=[]
for num in numbers:
    if num%2==1 and num%5==0:
        odds.append(num)
print(odds)

odd_num=[num for num in numbers if num%2==1 and num%5==0]
print(odd_num)

players = ["sakib","musfiq","liton"]
age = [38,37,32]

age_comb = []
for player in players:
    print("Player:",player)
    for num in age:
        age_comb.append([player,num])
print(age_comb)

age_comb2 = [[player,num] for player in players for num in age]
print(age_comb2)