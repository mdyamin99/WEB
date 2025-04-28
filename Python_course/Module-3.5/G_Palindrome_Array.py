n=int(input())
numbers=list(map(int,input().split()))
rev=[]
for i in range(n):
    rev.append(numbers[i])
rev.reverse()
# print(rev)
flag=True
for i in range(0,n):
    if numbers[i]!=rev[i]:
        flag=False
        break
if flag==True:
    print("YES")
else:
    print("NO")