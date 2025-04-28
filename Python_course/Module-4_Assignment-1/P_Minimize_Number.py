n=int(input())
numbers=list(map(int,input().split()))
ans=0
cnt=1
while True:
    for j in range(n):
        if numbers[j]%2==1 or numbers[j]<=0:
            cnt=0
            break
        numbers[j]=numbers[j]//2
    if cnt==0: break
    ans+=1
print(ans)